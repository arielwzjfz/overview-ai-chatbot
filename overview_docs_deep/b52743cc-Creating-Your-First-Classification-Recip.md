---
title: "Creating Your First Classification RecipeOnce you’ve followed the steps in Creating Your First Recipe to configure the Imaging Setup , Template Image and Alignment , and Inspection Setup , follow the steps below to train a Classification model. Classification Block In this section..."
category: "Start Here7 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/creating-your-first-classification-recipe"
source_page: "https://docs.overview.ai/docs/start-here"
parent_category: "Start Here7 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:19:44.171018"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/creating-your-first-classification-recipe "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/creating-your-first-classification-recipe "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/creating-your-first-classification-recipe "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Creating Your First Classification Recipe

  *  __09 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Creating Your First Classification Recipe

  *  __Updated on 09 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Once you’ve followed the steps in [Creating Your First Recipe](/docs/creating-your-first-recipe) to configure the **Imaging Setup** , **Template Image and Alignment** , and **Inspection Setup** , follow the steps below to train a **Classification** model.

## Classification Block

In this section, you’ll capture several images of the object and label \(classify\) the ROIs and train the model. You’ll need to capture at least five images for each class. By default, the classes are “Pass” and “Fail”. You can rename these or add other classes.

  1. From the **Inspection Setup** page, use the breadcrumb menu to select **Classification Block**. Alternatively, select **Classification Block** from the **Recipe Editor**.

![Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Recipe%20Editor%20Breadcrumb%20Menu.png)

> **Note**
> 
> The preview pane \(on the left-hand side\) displays a live preview, until an image is captured or is selected using the **Navigation** menu.

  2. Under **Inspection Types** , click **Edit** to rename the default classes or add additional classes. Once you have all the classes you need the camera to identify, continue to the next step.  


  3. With the object in the camera’s field of vision, select **Capture**.  


  4. A Region of Interest \(ROI\) will appear over the image. Click on the ROI to cycle through the different classes and select the class that applies to this image \(**Pass** or **Fail** by default\).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Classification Block - keychain.png)

  5. Place another example of the same object in the camera’s field of vision and repeat steps 3 and 4 until you have added at least five labeled examples for each class type \(**Pass** or **Fail** by default\).  


> **Tip**
> 
> The model will be more accurate if each image is different \(do not repeat the same image\).  
>   
> Double check that each capture is labeled correctly as this is what will be used to train the model.

  6. Click **Train Classification Model**.  


  7. Select **Fast** or **Accurate** , depending on how much time you have available, and how accurate you want the model to be.   


> **Note**
> 
> The **Fast** option is great for testing out a proof of concept. It is significantly faster, but is generally less accurate and is not optimized. For production use, you will want to use the **Accurate** option.

  
![creating-a-basic-single-roi-classifier-1-image-sg8rk9mf](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-basic-single-roi-classifier-1-image-sg8rk9mf.png)

  8. Adjust the **Number of Iterations** using the arrows on the right-hand side of the field to set how many times the labeled images are shown to the model to help it learn.  


> **Note**
> 
> Increasing the number of iterations will improve the model’s accuracy, but will also take longer to train.

  9. Click **Start Training**. A modal will display the progress of the training.

  10. Once the model is trained, use the **Live Preview Mode** or the [HMI](/docs/hmi) tab to verify the functionality of your Recipe. Place different examples of the object in the camera’s field of vision and verify the model classifies each example correctly.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/HMI - keychain.png)




> **Note**
> 
> For more information about the **Classification Block** page, see [Classification Block](/docs/classification-block).  
>   
> To define the pass/fail logic for your Recipe, go to [IO Block](/v1/docs/creating-your-first-classification-recipe#io-block).

## IO Block

In this section, you’ll define the pass/fail logic for your Recipe. For this simple example, we’ll set the logic so that the ROI must be classified as “Pass” for the capture to result in a PASS. Other examples are available in [IO Block and Node-RED Logic](/docs/io-and-node-red-logic).

  1. From the **Classification Block** page, use the breadcrumb menu to select **IO Block**. Alternatively, select **Configure IO** from the **Recipe Editor**.

![Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Recipe%20Editor%20Breadcrumb%20Menu.png)

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/IO Block - keychain.png)

  2. Double-click on **Classification Block Logic** to open the edit tab.

![image-1728660513967](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image-1728660513967.png)

  3. Click **\+ add** at the bottom of the tab.  


  4. Under **Inspection Region / ROI** , select the relevant ROI you want to base the pass/fail logic on from the drop-down menu.  


  5. Under **Target Class** , select the class you want the logic to consider as a “pass” from the drop-down menu \(by default, this will be **pass\_\[Inspection Type Name\]**\).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Edit node window - keychain.png)

  6. Click **Done**.  


  7. Click **Deploy**.




> **Note**
> 
> For more information about the **IO Block** page, see [IO Block and Node-RED Logic](/docs/io-and-node-red-logic).

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

  * [ Creating Your First Segmentation Recipe ](/docs/creating-your-first-segmentation-recipe) __



Table of contents

    * Classification Block 
    * IO Block 



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
