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

We develop open source resources that can drive innovation and accelerate the discovery of novel therapeutic strategies for pediatric brain tumor research. 

**OpenPBTA**: With Alex’s Lemonade Stand Foundation’s [Childhood Cancer Data Lab](https://www.alexslemonade.org/childhood-cancer-data-lab), Dr. Rokita co-led the creation of the [Open Pediatric Brain Tumor Atlas (OpenPBTA)](https://pubmed.ncbi.nlm.nih.gov/37492101/), an open-source reproducible analysis platform consisting of nearly 50 scalable modules to analyze pediatric brain tumor data.

**OpenPedCan**: The pan-cancer expansion counterpart of OpenPBTA is the [Open Pediatric Cancer (OpenPedCan) Project](https://github.com/d3b-center/OpenPedCan-analysis). OpenPedCan became the foundational data layer of the [NCI’s pediatric Molecular Targets Platform](https://moleculartargets.ccdi.cancer.gov/) and is used to support clinical trial decision-making for the [Pediatric Neuro-Oncology Consortium (PNOC)](https://pnoc.us/), therapeutic development, and discovery and translational research.

**AutoGVP**: In collaboration with [Dr. Sharon Diskin](https://diskinlab.org/) at CHOP, we created [AutoGVP](https://github.com/diskin-lab-chop/AutoGVP), a dockerized tool to assess germline variant pathogenicity based on current ACMG guidelines. We also created a [pathogenicity preprocessing CAVATICA application](https://cavatica.sbgenomics.com/public/apps/cavatica/apps-publisher/d3b-diskin-pathogenicity-preprocess-wf) to add ClinVar, InterVar, ANNOVAR, and AutoPVS1 annotations to the germline VCFs prior to running AutoGVP.

**annoFuse**: We created an R package, [annoFuse](https://github.com/d3b-center/annoFuse) and companion RShiny application, [ShinyFuse](https://shiny.imbei.uni-mainz.de:3838/shinyFuse/) to prioritize putative oncogenic fusions and visually explore fusion calls and breakpoints across a cohort.

### Integrative Multi-omics Approach

Our research harnesses the power of integrative multi-omics to unravel the complexities of pediatric brain tumors. 
By combining data from genomics, transcriptomics, and proteomics, we uncover critical insights into the biology of these aggressive cancers.

**RNA splicing mechanisms underlying oncogenesis**: We investigate the role of RNA splicing in driving tumor formation and progression in pediatric brain tumors.

**Identification of novel targets**: We have developed a workflow to identify and prioritize splice-derived peptides as new candidate tumor-specific vulnerabilities, paving the way for personalized immunotherapeutic treatment strategies for pediatric brain tumor patients.

**Germline risk variants**: In collaboration with [Dr. Sharon Diskin](https://diskinlab.org/), our team characterizes patient and parental germlines to pinpoint pathogenic variants that predispose patients to brain tumor development, offering new insights into how these variants influence tumor biology.

### Health Disparities
We are deeply passionate about exploring the impact of social determinants of health, race, ethnicity, and genetic-based ancestry on pediatric brain tumors.
In collaboration with [Dr. Cassie Kline](https://www.chop.edu/doctors/kline-cassie), we [recently](https://www.medrxiv.org/content/10.1101/2024.06.14.24308885v2) identified significant associations between genetic ancestry superpopulations, prevalence of CNS tumor histologies and molecular subtypes, patient overall and event-free survival, and upfront treatment approaches.

{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filters="group: featured" %}

{% include section.html %}

## More

{% include list.html component="card" data="projects" filters="group: " style="small" %}
