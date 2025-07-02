---
title: "Template Image and AlignmentUse the Template Image and Alignment page to capture a Template Image as a reference for your inspection program, and use pattern-matching to locate and orient parts for relative inspection. Preview If a Template Image has not yet been capt..."
category: "Software Setup15 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/alignment-block"
source_page: "https://docs.overview.ai/docs/software-setup"
parent_category: "Software Setup15 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:14.333995"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/alignment-block "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/alignment-block "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/alignment-block "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Template Image and Alignment

  *  __14 Nov 2024



  *  __ Print

  *  __ PDF




 __Contents

# Template Image and Alignment

  *  __Updated on 14 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Use the Template Image and Alignment page to capture a Template Image as a reference for your inspection program, and use pattern-matching to locate and orient parts for relative inspection.

## Preview

If a **Template Image** has not yet been captured for this recipe, the preview pane \(on the left-hand side\) displays a live preview of the camera’s field of vision.

Once the **Template Image** has been captured, the preview pane will display the **Template Image** , not a live preview of the camera’s field of vision. To view a live preview from the camera, scroll down the page and select **Live Preview Mode**. To retake the **Template Image** , ensure the live preview is not enabled and click **Re-Capture Template Image**.

## Capture/Re-Capture

**Re-Capture Template Image:** Click to change the Template Image.

**Capture Template Image:** Click to capture \(or re-capture\) a Template Image. Capturing a Template Image is a required step for ALL recipes.

**Import From Library:** Click to select an existing image from the [Library](/docs/library) as the Template Image.

> **Note**
> 
> By default, the Import From Library modal will filter images by Recipe. Use the drop-down menu to select another recipe or clear the filter and click **Search** to find images from other Recipes.
> 
> ![Import From Library clear Filter by Recipe](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Import%20From%20Library%20clear%20Filter%20by%20Recipe.png)

## Skip Aligner

Select to disable the aligner and use fixed-position [Regions of Interest](/v1/docs/roi-block). This is recommended for applications with parts that are fixtured or presented to the camera very repeatably.

## Template Regions

**\+ Rectangle** / **\+ Circle:** Click to add a Template Region to the Template Image. The OV20i will detect edges inside these Template Regions and try to locate parts by matching similar edge patterns. Click on a Template Region to stretch or change the size of the shape, rotate, or delete. Click and drag the Template Region to reposition it.

**Ignore Template Region:** Click to access a brush tool that can be used to erase unwanted edges from any Template Region. This is used to mask out unwanted edge noise and focus the Alignment on clear, repeatable edge patterns. Click **Finish** to save.

## Settings

**Rotation Range:** Enter an angle of 0-180 degrees to define the amount of rotation the aligner will tolerate. Set this to 180 to find parts rotated at any angle. Set this to 0 to find only parts that match the Template Image angle.

**Sensitivity:** Adjust the slider to increase/decrease edge-finding sensitivity. Higher sensitivity settings will find more edges, and lower sensitivity settings will find fewer edges.

**Confidence Threshold:** Use this slider to set the minimum confidence required for an Alignment to be considered valid \(1% indicates an identical match\). This threshold should fall between 0.6-0.9 for consistent alignment.

## Live Preview Mode

Select to run the aligner in real-time allowing you to test its performance and confidence on different situations and parts.

## Alignment Best Practices

> **Alignment Best Practices**
> 
>   1. When placing Template Regions, focus on edges that are simple, unique, and consistently visible across all parts. Try to avoid edges that may be obscured by defects, or edge patterns that vary from part to part.
> 
>   2. Edges found inside a Template Region are highlighted green. Red highlights indicate that there are not enough edges found for valid alignment. You can increase sensitivity or add more Template Regions to increase the edge count \(below\).
> 
>   3. Use the Ignore Template Region tool to filter out edge noise from the Alignment. “Edge noise” includes any highlighted edges that do not represent a simple, unique, and consistently visible pattern. For example, a Template Region might inappropriately highlight textured surfaces, reflections, debris, or other features as edges in your Template Image.
> 
> 


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(9\).png)

In this example, we are attempting to align to some of the white outlines printed on the circuit board, because they should be visible even if other components are broken or missing. In this case, the 1st Template Region does not have enough edges.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(11\).png)

Adding more Template Regions increases the number of edges for Alignment. In this case, a 2nd Template Region has been added over the circular feature in the lower left corner, but the highlights remain red because not enough edges are found.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(12\).png)

Increasing the sensitivity finds more edges in the existing Template Regions. It’s recommended to use the lowest Sensitivity setting that still finds adequate edges to avoid unwanted noise in the pattern.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(13\).png)

**Left:** Before using the Ignore Template Regions tool, the edge finder highlights some shiny areas and resistor edges that are not _simple, unique, and consistently visible._**Right** : After applying the Ignore Template Regions tool, the unwanted noise is masked by the red regions so the aligner will only pay attention to the white printed line patterns.

> **Tips**
> 
>   1. If Alignment is inconsistent or fails when testing on different parts, your Template Regions may be set up on a pattern that is not simple enough, or not consistently visible across all parts. Try reducing the amount of edges, or choosing a different pattern to focus on for Alignment.
> 
>   2. If Alignment has frequent “false positives” where it matches to something other than the part you want to find, you may have chosen a pattern that is not unique enough. Try increasing the Confidence Threshold to screen out the false positives, or add Template Regions and/or Sensitivity to make your Alignment pattern more specific.
> 
> 


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

  * [ Inspection Setup ](/docs/roi-block) __



Table of contents

    * Preview 
    * Capture/Re-Capture 
    * Skip Aligner 
    * Template Regions 
    * Settings 
    * Live Preview Mode 
    * Alignment Best Practices 



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
