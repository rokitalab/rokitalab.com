---
title: LAB TEAM
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Rokita Lab Team

{:.center}
The Rokita Lab is a highly engaged and collaborative team united by a shared passion for using genomics and computational biology to improve outcomes for children with brain tumors. We are committed to fostering an inclusive environment where diverse perspectives are valued and all team members can thrive.


{% include section.html %}

## Current Lab Members

{% include list.html data="labmembers" component="portrait" filter="role == 'pi'" %}
{% include list.html data="labmembers" component="portrait" filter="role != 'pi'" %}

{% include section.html %}

## Funding

{% capture content %}
{% include figure.html image="/images/team/National_Cancer_Institute_logo.png" alt="National Cancer Institute" link="https://www.cancer.gov/" %}

{% include figure.html image="/images/team/NIH-CFDElogo.png" alt="NIH Common Fund Data Ecosystem" link="https://commonfund.nih.gov/dataecosystem" %}

{% include figure.html image="/images/team/kidsfirst.png" alt="Kids First Data Resource Center" link="https://commonfund.nih.gov/KidsFirst" %}

{% include figure.html image="/images/team/BEST-CCF-logo-compressed.png" alt="The Children's Cancer Foundation" link="https://childrenscancerfoundation.org/" %}

{% include figure.html image="/images/team/ALSFhorizontal.png" alt="Alex's Lemonade Stand Foundation for Childhood Cancer" link="https://www.alexslemonade.org/" %}

{% include figure.html image="/images/team/SBF_Conquer-Logo_rgb.png" alt="St. Baldrick's Foundation" link="https://www.stbaldricks.org/" %}

{% include figure.html image="/images/team/BTI-anon-horizontal.png" alt="Brain Tumor Institute Anonymous Donors" %}

{% include figure.html image="/images/team/aws-logo.png" alt="Amazon Web Services" link="https://aws.amazon.com/government-education/nonprofits/" %}

{% include figure.html image="/images/team/GFF.png" alt="Gilbert Family Foundation" link="https://gilbertfamilyfoundation.org/" %}

{% endcapture %}

{% include grid.html content=content %}
