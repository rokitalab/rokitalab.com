---
title: BIOINFORMATICS CORE TEAM
nav:
  order: 4
  tooltip: About the Bioinformatics Core
---

# {% include icon.html icon="fa-solid fa-users" %}BTI Bioinformatics Core Team

{:.center}
The Brain Tumor Institute Bioinformatics Core at Children's National Hospital is a collaborative team of bioinformatics scientists, engineers, and operations staff dedicated to advancing computational methods, developing open-source tools, and providing bioinformatics expertise to support research and clinical initiatives across Children's National Hospital.

{%
  include button.html
  text="Learn more about the BTI Bioinformatics Core"
  icon="fa-solid fa-newspaper"
  link="https://innovationdistrict.childrensnational.org/building-bioinformatics-infrastructure-at-the-brain-tumor-institute/"
%}

{% include section.html %}

## {% include icon.html icon="fa-solid fa-star" %}Leadership

{% include list.html data="coremembers" component="portrait" filter="role == 'pi'" %}
{% include list.html data="coremembers" component="portrait" filter="role == 'ad'" %}
{% include list.html data="coremembers" component="portrait" filter="role == 'pm'" %}

{% include section.html %}

## {% include icon.html icon="fa-solid fa-code" %}Core Team

{:.center}
Our scientists and engineers bring deep expertise across genomics, multi-omics, cloud computing, and data engineering — working collaboratively to support research and clinical initiatives across Children's National Hospital.

{% include list.html data="coremembers" component="portrait" filter="role != 'pi' and role != 'ad' and role != 'pm'" %}

{% include section.html %}

## {% include icon.html icon="fa-solid fa-envelope" %}Contact
Interested in working with the bioinformatics core?
Our documentation site has everything PIs need to get started, including our services and how to submit a project.

{%
  include button.html
  type="docs"
  text="Work with the Core"
  link="https://childrens-bti.github.io/bti-bfx-docs/"
%}

{% include section.html %}

## Funding

{% capture content %}
{% include figure.html image="/images/core/BTI-anon-horizontal.png" alt="Brain Tumor Institute Anonymous Donors" %}

{% include figure.html image="/images/core/aws-logo.png" alt="Amazon Web Services" link="https://aws.amazon.com/government-education/nonprofits/" newtab=true %}

{% include figure.html image="/images/core/kidsfirst.png" alt="Kids First Data Resource Center" link="https://commonfund.nih.gov/KidsFirst" newtab=true %}

{% include figure.html image="/images/core/rally-full-logo.png" alt="Rally Foundation for Childhood Cancer" link="https://rallyfoundation.org/" newtab=true %}

{% include figure.html image="/images/core/GFF.png" alt="Gilbert Family Foundation" link="https://gilbertfamilyfoundation.org/" newtab=true %}

{% endcapture %}

{% include grid.html content=content %}
