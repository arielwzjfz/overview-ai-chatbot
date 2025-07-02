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
chunk_id: 6102694d
chunk_index: 1
total_chunks: 10
chunk_title: Label and Train
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 121
chunked_at: '2025-07-01T17:23:34.423177'
chunking_method: header_based
---

## Label and Train

In this section, you’ll capture several images of the object and label defects using the brush tool. You’ll need to capture and label at least 10 images.

  1. Select the **Label and Train** tab. Alternatively, select **Label and Train** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(156\).png)

> **Note**
> 
> The preview pane \(on the left-hand side\) displays a live preview, until an image is captured or is selected using the **Navigation** menu.

  2. Under **Inspection Types** , click **Edit** to rename the default class \(**fail\_\[Inspection Type Name\]**\) or add additional classes. Once you have all the classes you need the camera to identify, continue to the next step.  


  3. With the object in the camera’s field of vision, select **Capture**.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(157\).png)

  4. Use the **Brush** tool to highlight the defects on the object you want the camera to identify.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(158\).png)  


> **Tip**
> 
> Use the **Eraser** tool to remove any unwanted highlights.

  5. If you’ve added other classes, select the applicable **Brush Class** from the drop-down menu.   


  6. Click **Save Annotations**.  
  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(159\).png)

  7. Place another example of the same object in the camera’s field of vision and repeat steps 3-6 until you have added at least 10 labeled examples \(or if you’ve added additional classes, at least five examples of each class\).  


> **Tip**
> 
> The model will be more accurate if each image is different \(do not repeat the same image\).  
>   
> Double check that each capture is labeled correctly as this is what will be used to train the model.

  8. Continue to [IO Block](/v1/docs/ov80i-creating-your-first-segmentation-recipe#io-block).




> **Note**
> 
> For more information about the **Label and Train** page, see [Label And Train \(Segmentation\)](/docs/segmentation-block).
