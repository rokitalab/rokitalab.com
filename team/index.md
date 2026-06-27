---
title: LAB TEAM
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Rokita Lab Team

{:.center}
The Rokita Lab is a highly engaged and collaborative team united by a shared passion for using genomics and computational biology to improve outcomes for children with brain tumors. We are committed to fostering an environment where every member is valued, respected, and empowered to do their best work. Our team spans a rich mix of expertise and backgrounds — including bioinformatics scientists, bench scientists, postdocs, students, and engineers — all working together toward a common mission.

{% include section.html %}

## Current Lab Members

{% include list.html data="labmembers" component="portrait" filter="role == 'pi'" %}
{% include list.html data="labmembers" component="portrait" filter="role != 'pi'" %}

{% include section.html %}

## Funding

{% capture content %}
{% include figure.html image="/images/team/National_Cancer_Institute_logo.png" alt="National Cancer Institute" link="https://www.cancer.gov/" newtab=true %}

{% include figure.html image="/images/team/NIH-CFDElogo.png" alt="NIH Common Fund Data Ecosystem" link="https://commonfund.nih.gov/dataecosystem" newtab=true %}

{% include figure.html image="/images/team/kidsfirst.png" alt="Kids First Data Resource Center" link="https://commonfund.nih.gov/KidsFirst" newtab=true %}

{% include figure.html image="/images/team/BEST-CCF-logo-compressed.png" alt="The Children's Cancer Foundation" link="https://childrenscancerfoundation.org/" newtab=true %}

{% include figure.html image="/images/team/ALSFsquare.png" alt="Alex's Lemonade Stand Foundation for Childhood Cancer" link="https://www.alexslemonade.org/" newtab=true %}

{% include figure.html image="/images/team/SBF_Conquer-Logo-Tall_rgb.png" alt="St. Baldrick's Foundation" link="https://www.stbaldricks.org/" newtab=true %}

{% include figure.html image="/images/team/BTI-anon-horizontal.png" alt="Brain Tumor Institute Anonymous Donors" %}

{% include figure.html image="/images/team/aws-logo.png" alt="Amazon Web Services" link="https://aws.amazon.com/government-education/nonprofits/" newtab=true %}

{% include figure.html image="/images/team/GFF.png" alt="Gilbert Family Foundation" link="https://gilbertfamilyfoundation.org/" newtab=true %}

{% endcapture %}

{% include grid.html content=content %}
