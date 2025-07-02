---
title: Creating Your First Classification RecipeOnce you’ve followed the steps in
  Creating Your First Recip
category: OV20i
language: English
url: https://docs.overview.ai/docs/ov80i-creating-your-first-classification-recipe
source_page: https://docs.overview.ai/start-here-1
parent_category: OV80i
is_individual_article: true
scraped_at: '2025-06-30T17:20:43.189974'
chunk_id: dda0fc62
chunk_index: 4
total_chunks: 7
chunk_title: Train Classification Model
chunk_level: 2
chunk_start_line: 160
chunk_end_line: 197
chunked_at: '2025-07-01T17:23:34.230902'
chunking_method: header_based
---

## Train Classification Model

In this section, you’ll train the model using the images labeled earlier.

  1. Select the **Classification Block** tab. Alternatively, select **Classification Block** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(153\).png)

  2. Click **Train Classification Model**.  


  3. Select **Fast** or **Accurate** , depending on how much time you have available, and how accurate you want the model to be.   


> **Note**
> 
> The **Fast** option is great for testing out a proof of concept. It is significantly faster, but is general less accurate and is not optimized. For production use, you will want to use the **Accurate** option.

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(154\).png)

  4. Optional step: Adjust the **Number of Iterations \(Epochs\)** to set how many times the labeled images are shown by going to **Advanced Settings > Parameters**.   


> **Note**
> 
> Increasing the number of iterations will improve the model’s accuracy, but will also take longer to train.

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(155\).png)

  5. Click **Start Training**. A modal will display the progress of the training.

  6. Once the model is trained, use the **Live Preview Mode** or the [HMI](/docs/hmi) tab to verify the functionality of your Recipe. Place different examples of the object in the camera’s field of vision and verify the model classifies each example correctly.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/HMI - keychain.png)
