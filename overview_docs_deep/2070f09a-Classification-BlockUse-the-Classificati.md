---
title: "Classification BlockUse the Classification Block page to train a deep learning model to determine what’s inside an Inspection Region . Preview The preview pane (on the left-hand side) displays a live preview until an image is captured or is selected using the..."
category: "Software Setup15 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/classification-block"
source_page: "https://docs.overview.ai/docs/software-setup"
parent_category: "Software Setup15 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:15.012373"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/classification-block "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/classification-block "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/classification-block "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Classification Block

  *  __15 Nov 2024



  *  __ Print

  *  __ PDF




 __Contents

# Classification Block

  *  __Updated on 15 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Use the Classification Block page to train a deep learning model to determine what’s inside an [Inspection Region](/v1/docs/roi-block).

## Preview

The preview pane \(on the left-hand side\) displays a live preview until an image is [captured](/v1/docs/classification-block#captureimport) or is selected using the [**Navigation**](/v1/docs/classification-block#navigation) menu.

## Capture/Import

**Capture:** This lets you take a new Capture and use it to train a model.

> **Note**
> 
> While in Live Preview Mode, clicking on one of the labels under Inspection Types will trigger a Capture and label all ROIs of that type to that label class.

**Import From Library:** This lets you add images stored in your [Library](/v1/docs/library) and use them for model training.

## Navigation

**View All ROIs:** This modal shows each ROI cropped from its parent image. This is useful for visualizing all training data together on a grid-style page and can also efficiently be used to re-label data. This can be done in two ways:

  1. Click on an image to view information about that ROI, such as the parent image and Inspection Type. You can also change its label here.

  2. Select multiple images by clicking on the checkbox for each image. Then, you can configure the selected images using the options at the bottom of the page \(**Label Selected ROIs** , **Unlabel Selected ROIs** , **Clear Selection**\).




**< Prev:** Click to view the previous captured image.

**> Next:** Click to view the next captured image.

## Inspection Types

Click ✏️ **Edit** above a group to edit or add the labels for each Inspection Type. You can also change the label color and name and add/remove classes.

There are two ways of labeling new data:

  1. Clicking the labels in the Inspection Types panel will label all ROIs of that Inspection Type to that label class. This can be useful when most labels are of the same class.

  2. Clicking the ROIs on the image window will cycle through all valid labels for that inspection type.




## Train Classification Model

There are two modes a model can train. **Fast** and **Accurate**.

**Fast:** It is useful when iterating on the problem. It trains significantly faster, but it is generally less accurate. It will also run slower in production as it is not optimized.

**Accurate:** Production grade model.

**Number of Iterations:** Use the arrows on the right-hand side of the field to increase or decrease how many times the labeled images are shown to the model to help it learn.

**Advanced Settings:** Click to access image augmentation options \(flip image, adjust rotation range, image brightness, and contrast\).

## Live Preview Mode

Click to preview aligner results or model results \(after training it\).

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

  * [ Label And Train \(Segmentation\) ](/docs/segmentation-block) __



Table of contents

    * Preview 
    * Capture/Import 
    * Navigation 
    * Inspection Types 
    * Train Classification Model 
    * Live Preview Mode 



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
