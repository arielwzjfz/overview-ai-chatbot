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
chunk_id: '46870407'
chunk_index: 1
total_chunks: 7
chunk_title: Classification Block
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 105
chunked_at: '2025-07-01T17:23:34.230857'
chunking_method: header_based
---

## Classification Block

In this section, you’ll capture several images of the object and label \(classify\) the ROIs to train the model. You’ll need to capture at least five images for each class. By default, the classes are “Pass” and “Fail”. You can rename these or add other classes.

  1. Select the **Classification Block** tab. Alternatively, select **Classification Block** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(149\).png)

> **Note**
> 
> The preview pane \(on the left-hand side\) displays a live preview, until an image is captured or is selected using the **Navigation** menu.

  2. Under **Inspection Types** , click **Edit** to rename the default classes or add additional classes. Once you have all the classes you need the camera to identify, continue to the next step.  


  3. With the object in the camera’s field of vision, select **Capture**.  


  4. A Region of Interest \(ROI\) will appear over the image. Click on the ROI to cycle through the different classes and select the class that applies to this image \(**Pass** or **Fail** by default\).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(150\).png)

  5. Place another example of the same object in the camera’s field of vision and repeat steps 3 and 4 until you have added at least five labeled examples for each class type \(**Pass** or **Fail** by default\).  


> **Tip**
> 
> The model will be more accurate if each image is different \(do not repeat the same image\).  
>   
> Double check that each capture is labeled correctly as this is what will be used to train the model.

  6. Continue to [IO Block](/v1/docs/ov80i-creating-your-first-classification-recipe#io-block).




> **Note**
> 
> For more information about the **Classification Block** page, see [Classification Block](/docs/classification-block).
