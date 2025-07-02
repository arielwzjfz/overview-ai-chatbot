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
chunk_id: 87aa45fa
chunk_index: 1
total_chunks: 5
chunk_title: Create and Train a New Recipe
chunk_level: 2
chunk_start_line: 99
chunk_end_line: 148
chunked_at: '2025-07-01T17:23:34.360392'
chunking_method: header_based
---

## Create and Train a New Recipe

Instead of one recipe per side, because of the different layouts, we will combine both sides into one recipe so we don’t need to train the same presence/absence model twice.

  1. Create a recipe. In this case, it is a classification recipe but this same principle can be used with segmentation.

  2. Set up the **Template Image and Alignment** for the first view:  


> **Note**
> 
> The Aligner is unavailable when inspecting more than one view on the same recipe. The Template Image and Aligner is only used to set the base image for the **Inspection Setup**.

  3. Draw ROIs for side A. Name them something that helps identify which side they belong to. In this case, we named the ROIs A1-A16.   


  4. Return to the **Template Image and Alignment** to replace the image with side B, either from a new capture or from the library.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(79\).png)

  5. Use the lock icons next to each ROI to avoid moving any ROIs from side A, then draw and name the ROIs for side B.  


> **Note**
> 
> For more complex recipes, repeat this process for as many different views as you want to inspect.

  6. Label and train the classification model using images from both sides A and B. When capturing and labeling side A, do not label the side B ROIs and vice versa.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(84\).png)

Labeling side A, Pass

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(85\).png)

Labeling side A, Fail

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(82\).png)

Labeling side B, Pass

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(83\).png)

Labeling side B, Fail



