---
title: Creating Your First Segmentation RecipeOnce you’ve followed the steps in Creating
  Your First Recipe
category: OV20i
language: English
url: https://docs.overview.ai/docs/ov80i-creating-your-first-segmentation-recipe
source_page: https://docs.overview.ai/start-here-1
parent_category: OV80i
is_individual_article: true
scraped_at: '2025-06-30T17:20:43.905651'
chunk_id: ae3dc63f
chunk_index: 7
total_chunks: 10
chunk_title: Train Segmentation Model
chunk_level: 2
chunk_start_line: 214
chunk_end_line: 243
chunked_at: '2025-07-01T17:23:34.423268'
chunking_method: header_based
---

## Train Segmentation Model

In this section, you’ll train the model using the images labeled earlier.

  1. Select the **Label and Train** tab. Alternatively, select **Label and Train** from the **Recipe Editor**.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(162\).png)  


  2. Click **Train Segmentation Model**.  


  3. Optional step: Adjust the **Number of Iterations \(Epochs\)** to set how many times the labeled images are shown by going to **Advanced Settings > Parameters**.   


> **Note**
> 
> Increasing the number of iterations will improve the model’s accuracy, but will also take longer to train.

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(164\).png)  


  4. Click **Start Training**. A modal will display the progress of the training.   


  5. Once the model is trained, use the **Live Preview Mode** or the [HMI](/docs/hmi) tab to verify the functionality of your Recipe. Place different examples of the object in the camera’s field of vision and verify the model classifies each example correctly.
