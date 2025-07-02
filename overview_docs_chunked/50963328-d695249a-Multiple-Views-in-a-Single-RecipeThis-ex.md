---
title: Multiple Views in a Single RecipeThis example shows you how to set up a single
  recipe that can inspe
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/multiple-views-one-recipe
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:05.414696'
chunk_id: '50963328'
chunk_index: 0
total_chunks: 5
chunk_title: Multiple Views in a Single Recipe
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 99
chunked_at: '2025-07-01T17:23:34.360366'
chunking_method: header_based
---

# Multiple Views in a Single Recipe

  *  __Updated on 29 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This example shows you how to set up a single recipe that can inspect different parts, angles, or views without switching to other recipes. There are a variety of reasons to do this, but two primary use cases are:

  1. when there isn't enough time between captures to change recipe,

  2. when performing the same inspection on multiple parts or angles of a part \(eg., presence/absence of studs on five different positions in a car body\). In this case, this method prevents the need to train the same model \(stud presence/absence\) multiple times across different recipes.




**Example Recipe for download:**

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/OVModel.v0.recipe_21_Multi Position Example_with_library_data.zip)OVModel

8.89 MB

  
**Importable Example flow for download:**

> **Note**
> 
> Configuration inside Classification Block Logic nodes will be lost on import.

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/flows \(2\).json)flows \(2\)

7.76 KB

This example is a simple version with two views and one inspection type, but you can use this same technique for an unlimited number of inspection types and views. This inspection we will look for the presence/absence of bits on two sides of a drill bit case. One side has five bits on the bottom, and the other side has eight bits on both the top and bottom. We will call the side with 16 bits side A and five bits side B.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(77\).png)

Side A \(16 bits\)

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(76\).png)

Side B \(five bits\)
