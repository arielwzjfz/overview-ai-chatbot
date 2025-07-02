---
title: Creating Your First Segmentation RecipeOnce you’ve followed the steps in Creating
  Your First Recipe
category: Start Here7 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-your-first-segmentation-recipe
source_page: https://docs.overview.ai/docs/start-here
parent_category: Start Here7 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:19:44.855808'
chunk_id: 44fe3041
chunk_index: 1
total_chunks: 7
chunk_title: Label and Train
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 134
chunked_at: '2025-07-01T17:23:34.111489'
chunking_method: header_based
---

## Label and Train

In this section, you’ll capture several images of the object, label defects using the brush tool, and train the model. You’ll need to capture and label at least 10 images.

  1. From the **Inspection Setup** page, use the breadcrumb menu to select **Label and Train**. Alternatively, select **Label and Train** from the **Recipe Editor**.

![Segmeneter Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmeneter%20Recipe%20Editor%20Breadcrumb%20Menu.png)

> **Note**
> 
> The preview pane \(on the left-hand side\) displays a live preview, until an image is captured or is selected using the **Navigation** menu.

  2. Under **Inspection Types** , click **Edit** to rename the default class \(**fail\_\[Inspection Type Name\]**\) or add additional classes. Once you have all the classes you need the camera to identify, continue to the next step.  


  3. With the object in the camera’s field of vision, select **Capture**.  


  4. Use the **Brush** tool to highlight the defects on the object you want the camera to identify.  


> **Tip**
> 
> Use the **Eraser** tool to remove any unwanted highlights.

  5. If you’ve added other classes, select the applicable **Brush Class** from the drop-down menu.   


  6. Click **Save Annotations**.  


![Segmentation Annotation - keychain\(1\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation%20Annotation%20-%20keychain\(1\).png)

  7. Place another example of the same object in the camera’s field of vision and repeat steps 3-6 until you have added at least 10 labeled examples \(or if you’ve added additional classes, at least five examples of each class\).  


> **Tip**
> 
> The model will be more accurate if each image is different \(do not repeat the same image\).  
>   
> Double check that each capture is labeled correctly as this is what will be used to train the model.

  8. Click **Train Segmentation Model**.  


  9. Adjust the **Number of Iterations** using the arrows on the right-hand side of the field to set how many times the labeled images are shown to the model to help it learn.

> **Note**
> 
> Increasing the number of iterations will improve the model’s accuracy, but will also take longer to train.

  
![creating-a-segmenter-image-d3t5mlho](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-d3t5mlho.png)

  10. Click **Start Training**. A modal will display the progress of the training.   


  11. Once the model is trained, use the **Live Preview Mode** or the [HMI](/docs/hmi) tab to verify the functionality of your Recipe. Place different examples of the object in the camera’s field of vision and verify the model classifies each example correctly.




> **Note**
> 
> For more information about the **Label and Train** page, see [Label And Train \(Segmentation\)](/docs/segmentation-block).
> 
>   
> To define the pass/fail logic for your Recipe, go to [IO Block](/v1/docs/creating-your-first-segmentation-recipe#io-block).
