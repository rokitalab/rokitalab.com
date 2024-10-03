---
title: Research
nav:
  order: 2
  tooltip: Present and past research
---

# {% include icon.html icon="fa-solid fa-wrench" %}Research

{% include tags.html tags="publication, preprint, resource, tool, open source, disparities" %}

{% include search-info.html %}

Below are some of our present and past research projects.

### Tool and Resource Development

OpenPBTA: With Alex’s Lemonade Stand Foundation’s [Childhood Cancer Data Lab](https://www.alexslemonade.org/childhood-cancer-data-lab), Dr. Rokita co-led the creation of the [Open Pediatric Brain Tumor Atlas (OpenPBTA)](https://pubmed.ncbi.nlm.nih.gov/37492101/), an open-source reproducible analysis platform consisting of nearly 50 scalable modules to analyze pediatric brain tumor data.

OpenPedCan: The pan-cancer expansion counterpart of OpenPBTA is the [Open Pediatric Cancer (OpenPedCan) Project](https://github.com/d3b-center/OpenPedCan-analysis). OpenPedCan became the foundational data layer of the [NCI’s pediatric Molecular Targets Platform](https://moleculartargets.ccdi.cancer.gov/) and is used to support clinical trial decision-making for the [Pediatric Neuro-Oncology Consortium (PNOC)](https://pnoc.us/), therapeutic development, and discovery and translational research.

AutoGVP: In collaboration with the [Diskin Lab](https://diskinlab.org/) at CHOP, we created [AutoGVP](https://github.com/diskin-lab-chop/AutoGVP), a dockerized tool to assess germline variant pathogenicity based on current ACMG guidelines. We also created a [pathogenicity preprocessing CAVATICA application](https://cavatica.sbgenomics.com/public/apps/cavatica/apps-publisher/d3b-diskin-pathogenicity-preprocess-wf) to add ClinVar, InterVar, ANNOVAR, and AutoPVS1 annotations to the germline VCFs prior to running AutoGVP.

annoFuse and ShinyFuse: We created an R package, [annoFuse](https://github.com/d3b-center/annoFuse) and companion RShiny application, [ShinyFuse](https://shiny.imbei.uni-mainz.de:3838/shinyFuse/) to prioritize putative oncogenic fusions and visually explore fusion calls and breakpoints across a cohort.


{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filters="group: featured" %}

{% include section.html %}

## More

{% include list.html component="card" data="projects" filters="group: " style="small" %}
