"""
utility functions for cite process and plugins
"""

import re
import subprocess
import json
from urllib.request import Request, urlopen
import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from datetime import date, datetime
from rich import print
from diskcache import Cache


# cache for time-consuming network requests
cache = Cache("./_cite/.cache")


# clear expired items from cache
cache.expire()


def log_cache(func):
    """
    decorator to use around memoized function to log if cached or or not
    """

    def wrap(*args):
        key = func.__cache_key__(*args)
        if key in cache:
            log(" (from cache)", level="INFO", newline=False)
        return func(*args)

    return wrap


def log(message="\n--------------------\n", indent=0, level="", newline=True):
    """
    log to terminal, color determined by indent and level
    """

    colors = {
        0: "[orange1]",
        1: "[salmon1]",
        2: "[violet]",
        3: "[sky_blue1]",
        "ERROR": "[#F43F5E]",
        "WARNING": "[#EAB308]",
        "SUCCESS": "[#10B981]",
        "INFO": "[grey70]",
    }
    prefixes = {
        "ERROR": "🚫 ERROR: ",
        "WARNING": "⚠️ WARNING: ",
    }
    color = get_safe(colors, level, "") or get_safe(colors, indent, "") or "[white]"
    prefix = get_safe(prefixes, level, "")
    if newline:
        print()
    print(indent * "    " + color + prefix + str(message) + "[/]", end="", flush=True)


def label(entry):
    """
    get "label" of dict entry (for logging purposes)
    """

    return str(list(entry.keys())[0]) + ": " + str(list(entry.values())[0])


def get_safe(item, path, default=None):
    """
    safely access value in nested lists/dicts
    """

    for part in str(path).split("."):
        try:
            part = int(part)
        except ValueError:
            part = part
        try:
            item = item[part]
        except (KeyError, IndexError, AttributeError, TypeError):
            return default
    return item


def list_of_dicts(data):
    """
    check if data is list of dicts
    """

    return isinstance(data, list) and all(isinstance(entry, dict) for entry in data)


def format_date(_date):
    """
    format date as YYYY-MM-DD, or no date if malformed
    """

    if isinstance(_date, int):
        return datetime.fromtimestamp(_date // 1000.0).strftime("%Y-%m-%d")
    if isinstance(_date, (date, datetime)):
        return _date.strftime("%Y-%m-%d")
    try:
        return datetime.strptime(_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return ""


def load_data(path):
    """
    read data from yaml or json file
    """

    # convert to path object
    path = Path(path)

    # check if file exists
    if not path.is_file():
        raise Exception("Can't find file")

    # try to open file
    try:
        file = open(path, encoding="utf8")
    except Exception as e:
        raise Exception(e or "Can't open file")

    # try to parse as yaml
    try:
        with file:
            data = yaml.load(file, Loader=SafeLoader)
    except Exception:
        raise Exception("Can't parse file. Make sure it's valid YAML.")

    # if no errors, return data
    return data


def save_data(path, data):
    """
    write data to yaml file
    """

    # convert to path object
    path = Path(path)

    # try to open file
    try:
        file = open(path, mode="w")
    except Exception:
        raise Exception("Can't open file for writing")

    # prevent yaml anchors/aliases (pointers)
    yaml.Dumper.ignore_aliases = lambda *args: True

    # try to save data as yaml
    try:
        with file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        raise Exception("Can't save YAML to file")

    # write warning note to top of file
    note = "# DO NOT EDIT, GENERATED AUTOMATICALLY"
    try:
        with open(path, "r") as file:
            data = file.read()
        with open(path, "w") as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception("Can't write to file")


@log_cache
@cache.memoize(name="manubot", expire=90 * (60 * 60 * 24))
def cite_with_manubot(_id):
    """
    generate citation data for source id with Manubot
    """

    # run Manubot
    try:
        commands = ["manubot", "cite", _id, "--log-level=WARNING"]
        output = subprocess.Popen(commands, stdout=subprocess.PIPE).communicate()
    except Exception as e:
        log(e, indent=3)
        raise Exception("Manubot could not generate citation")

    # parse results as json
    try:
        manubot = json.loads(output[0])[0]
    except Exception:
        raise Exception("Couldn't parse Manubot response")

    # new citation with only needed info
    citation = {}

    # original id
    citation["id"] = _id

    # title
    citation["title"] = get_safe(manubot, "title", "").strip()

    # authors
    citation["authors"] = []
    for author in get_safe(manubot, "author", {}):
        given = get_safe(author, "given", "").strip()
        family = get_safe(author, "family", "").strip()
        if given or family:
            citation["authors"].append(" ".join([given, family]))

    # publisher
    container = get_safe(manubot, "container-title", "").strip()
    collection = get_safe(manubot, "collection-title", "").strip()
    publisher = get_safe(manubot, "publisher", "").strip()
    citation["publisher"] = container or publisher or collection or ""

    # extract date part
    def date_part(citation, index):
        try:
            return citation["issued"]["date-parts"][0][index]
        except (KeyError, IndexError, TypeError):
            return ""

    # date
    year = date_part(manubot, 0)
    if year:
        # fallbacks for month and day
        month = date_part(manubot, 1) or "1"
        day = date_part(manubot, 2) or "1"
        citation["date"] = format_date(f"{year}-{month}-{day}")
    else:
        # if no year, consider date missing data
        citation["date"] = ""

    # link
    citation["link"] = get_safe(manubot, "URL", "").strip()

    # return citation data
    return citation


# publisher names and doi prefixes of preprint servers
preprint_publishers = r"rxiv|research square|ssrn|preprints"
preprint_doi_prefixes = ["10.1101/", "10.64898/", "10.48550/", "10.21203/", "10.2139/"]

# titles of supplementary material deposited as its own record, e.g. "Supplementary Figure S1 from ..."
supplement_title = r"^(data|supplement(al|ary)\b.*?) from "


def clean_title(title):
    """
    trim and collapse whitespace in title
    """

    return re.sub(r"\s+", " ", str(title or "")).strip()


def title_key(title):
    """
    normalized title for finding the same work cited from different sources
    """

    return re.sub(r"[^a-z0-9]", "", clean_title(title).lower())


def is_preprint(citation):
    """
    check if citation is a preprint, from explicit type, publisher, or doi
    """

    if get_safe(citation, "type", "") == "preprint":
        return True
    if re.search(preprint_publishers, str(get_safe(citation, "publisher", "")), re.I):
        return True
    _id = str(get_safe(citation, "id", ""))
    return any(_id.startswith(f"doi:{prefix}") for prefix in preprint_doi_prefixes)


def is_supplement(citation):
    """
    check if citation is supplementary material rather than a work itself
    """

    return bool(re.search(supplement_title, clean_title(get_safe(citation, "title", "")), re.I))


def dedupe_citations(citations):
    """
    merge citations of the same work (matched by title) into one, preferring
    manually defined entries, then published works over preprints,
    then pubmed records, then the earliest date
    returns deduped citations and list of (dropped id, kept id) pairs
    """

    # fields to carry over from dropped duplicates if the kept citation lacks them
    carry = ["tags", "repo", "image", "buttons", "description"]

    def rank(citation):
        manual = get_safe(citation, "plugin", "") == "sources.py"
        pubmed = get_safe(citation, "plugin", "") == "pubmed.py"
        # then prefer pubmed records, then the earliest date (the original, not a later correction)
        return (
            not manual,
            is_preprint(citation),
            not pubmed,
            get_safe(citation, "date", "") or "9999",
        )

    # group citations by title, leaving untitled citations alone
    groups = {}
    for index, citation in enumerate(citations):
        key = title_key(get_safe(citation, "title", "")) or f"untitled-{index}"
        groups.setdefault(key, []).append(citation)

    result = []
    dropped = []
    for group in groups.values():
        group = sorted(group, key=rank)
        kept = group[0]
        for other in group[1:]:
            for field in carry:
                if field in other and not kept.get(field):
                    kept[field] = other[field]
            dropped.append((other["id"], kept["id"]))
        result.append(kept)

    # restore original order
    order = {id(citation): index for index, citation in enumerate(citations)}
    result.sort(key=lambda citation: order[id(citation)])

    return result, dropped


@log_cache
@cache.memoize(name="pubmed-title", expire=90 * (60 * 60 * 24))
def pubmed_title(pmid):
    """
    get title of pubmed record, for when Manubot returns none
    """

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    response = json.loads(urlopen(Request(url=url)).read())
    return clean_title(get_safe(response, "result", {}).get(str(pmid), {}).get("title", "")).rstrip(".")
