---
title: Creating Your First RecipeOnce you’ve mounted the camera and connected to the
  OV80i software, follow
category: OV20i
language: English
url: https://docs.overview.ai/docs/ov80i-creating-your-first-recipe
source_page: https://docs.overview.ai/start-here-1
parent_category: OV80i
is_individual_article: true
scraped_at: '2025-06-30T17:20:42.462110'
chunk_id: c1f2b58d
chunk_index: 4
total_chunks: 8
chunk_title: Template Image and Alignment
chunk_level: 2
chunk_start_line: 136
chunk_end_line: 180
chunked_at: '2025-07-01T17:23:34.080540'
chunking_method: header_based
---

## Template Image and Alignment

In this section, you’ll capture a **Template Image** and have the option to configure an aligner.

> **Note**
> 
> **Template Image and Alignment** is the same for Classification and Segmentation Recipes.

  1. Select the **Template Image and Alignment** tab. Alternatively, select **Template Image and Alignment** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(144\).png)

  2. Select **Capture Template Image**.   


> **Note**
> 
> Once the **Template Image** has been captured, the preview pane \(on the left-hand side\) will display the **Template Image** , not a live preview of the camera’s field of vision. To view a live preview from the camera, scroll down the page and select **Live Preview Mode**. To retake the **Template Image** , ensure the live preview is not enabled and click **Re-Capture Template Image**.

  3. If the object being inspected will not always be in exactly the same position or orientation within the field of view, follow the steps below to configure an **Aligner**. If your application doesn’t require an aligner, toggle the **Skip Aligner** option, click **Save** at the bottom of the page, and continue to [Inspection Setup](/v1/docs/ov80i-creating-your-first-recipe#inspection-setup).  


  4. Under **Template Regions** , select **\+ Rectangle** or **\+ Circle** \(whichever matches the shape of the object being inspected\).  


  5. Reposition/resize the region to fit the object being inspected.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(176\).png)

  6. Under **Settings** , set the **Rotation Range** to **20** degrees. This will allow the aligner to locate the object if it is rotated up to 20 degrees compared to this **Template Image**.  


  7. If required, adjust the **Sensitivity** and **Confidence Threshold**.   


  8. Click **Save** and continue to [Inspection Setup](/v1/docs/ov80i-creating-your-first-recipe#inspection-setup).




> **Note**
> 
> For more information about the **Template Image and Alignment** page, see [Template Image and Alignment](/docs/alignment-block).
