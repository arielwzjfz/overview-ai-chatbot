---
title: "Creating Your First RecipeOnce you’ve mounted the camera and connected to the OV80i software, follow the steps below to create your first recipe. From the All Recipes page, click + New Recipe in the top-right corner. The Add A New Recipe modal will a..."
category: "OV20i"
language: "English"
url: "https://docs.overview.ai/docs/ov80i-creating-your-first-recipe"
source_page: "https://docs.overview.ai/start-here-1"
parent_category: "OV80i"
is_individual_article: True
scraped_at: "2025-06-30T17:20:42.462110"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/ov80i-creating-your-first-recipe "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/clone-creating-your-first-recipe "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/ov80i-creating-your-first-recipe "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Creating Your First Recipe

  *  __07 Mar 2025



  *  __ Print

  *  __ PDF




 __Contents

# Creating Your First Recipe

  *  __Updated on 07 Mar 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Once you’ve mounted the camera and connected to the OV80i software, follow the steps below to create your first recipe.

  1. From the **All Recipes** page, click **\+ New Recipe** in the top-right corner.

  2. The **Add A New Recipe** modal will appear.

     1. Enter a **Name** for the Recipe \(required\). This name will appear on the **All Recipes** page.   


     2. Select the **Recipe Type** from the drop-down menu \(required\). See below for help selecting the Recipe Type.

### Should I Select Classification or Segmentation?

Create a **Classification** Recipe to train a deep-learning model to categorize an image into different classes based on its visual characteristics.

Create a **Segmentation** Recipe to train a deep-learning model to take an image and segment classes at a pixel level based on labeled defects. By operating at a pixel level, this tool is useful for inspections that need finer-grained control over labels.

     3. Enter a **Description** for the Recipe \(optional\). This will appear on the **All Recipes** page and at the top of the **Recipe Editor** page.  


  3. Click **OK** to create the new Recipe.   


  4. The new Recipe will be listed on the **All Recipes** page \(Inactive\).




## Open the Recipe Editor

To edit the Recipe, the Recipe needs to be active.

  1. Click******Activate** to the right-hand side of the Recipe.

  2. Then click **Activate and go to editor** to confirm.

  3. Continue to [Imaging Setup](/v1/docs/ov80i-creating-your-first-recipe#imaging-setup) below.




> **Note**
> 
> For more information about the **Recipe Editor** , see [Recipe Editor](/docs/recipe-editor).

## Imaging Setup

In this section, you’ll set up the camera to achieve a clear image of the object being inspected.

> **Note**
> 
> **Imaging Setup** is the same for Classification and Segmentation Recipes.

  1. To configure the **Imaging Setup** , click **Configure Imaging** at the lower left-hand side of the page.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(171\).png)

  2. Place the object being inspected in the camera’s field of vision, using the live preview to verify it’s in shot.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(175\).png)

  3. Adjust the **Camera Settings** on the right-hand side as required to achieve a clear image of the object.  


> **Note**
> 
> For more information about **Imaging Setup** options, see [Imaging Setup](/docs/imaging-setup).

  4. Click **Save Imaging Settings** at the bottom-right of the page and continue to [Template Image and Alignment](/v1/docs/ov80i-creating-your-first-recipe#template-image-and-alignment).




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

## Inspection Setup

In this section, you’ll configure what you want the camera to inspect \(**Inspection Types**\) and where on the object you want it to perform the inspection \(**Inspection Regions**\).

> **Note**
> 
> **Inspectoin Setup** is the same for Classification and Segmentation Recipes.

  1. Select the **Inspection Setup** tab. Alternatively, select **Inspection Setup** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(147\).png)

> **Note**
> 
> The preview pane \(on the left-hand side\) displays the **Template Image** , not a live preview of the camera’s field of vision. To view a live preview from the camera, scroll down the page and select **Live Preview Mode**. To add or edit **Inspection Types** and **Inspection Regions** , ensure the live preview is not enabled.

  2. Under **Inspection Types** , “Inspection Type 1” will appear by default. Click **Edit** to rename it.  
  
![A screenshot of the default Inspection Types on the Inspection Setup page.](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/18_90 Inspection Setup - Default Inspection Types.png)  


> **Note**
> 
> **Inspection Types** refer the different types \(classes\) of inspections being performed and allow you to group visually similar **Inspection Regions** \(ROIs\). **Inspection Regions** \(ROIs\) refer to the area\(s\) where the inspection should be performed.

  3. Under **Inspection Regions** , click **\+ Add Inspection Region**.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Add Inspection Region button.png)

  4. Reposition and resize the yellow box on screen to fit the specific area of the object you want to inspect.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(148\).png)

> **Note**
> 
> By default, the **Inspection Region** will be named “New ROI”. Click **Edit** to change the name.

  5. Add as many **Inspection Types** and **Inspection regions** as required for this Recipe.   


  6. Click **Save** at the bottom of the page and continue to [Next Steps](/v1/docs/ov80i-creating-your-first-recipe#next-steps).




> **Note**
> 
> For more information about the **Inspection Setup** page, see [Inspection Setup](/docs/roi-block).

## Next Steps

If you selected a **Classification** Recipe type, continue to [Creating Your First Classification Recipe](/docs/ov80i-creating-your-first-classification-recipe).

If you selected a **Segmentation** Recipe type, continue to [Creating Your First Segmentation Recipe](/docs/ov80i-creating-your-first-segmentation-recipe).

Was this article helpful?

__Yes __No

Thank you for your feedback\! Our team will get back to you

How can we improve this article?

Your feedback

Need more information

Difficult to understand

Inaccurate or irrelevant content

Missing/broken link

Others

Comment

Comment \(Optional\)

Character limit : 500

Please enter your comment

Email \(Optional\)

Email

Notify me about change  


Please enter a valid email

Cancel

###### What's Next

  * [ Creating Your First Classification Recipe ](/docs/ov80i-creating-your-first-classification-recipe) __



Table of contents

    * Open the Recipe Editor 
    * Imaging Setup 
    * Template Image and Alignment 
    * Inspection Setup 
    * Next Steps 



ENTER

ESC

 __

__

Eddy AI, facilitating knowledge discovery through conversational intelligence

Search Limit Exceeded. Please upgrade the plan.

Answer copied\!

__

__ __

No results found

Provide more context or information so that I can better understand and assist you
