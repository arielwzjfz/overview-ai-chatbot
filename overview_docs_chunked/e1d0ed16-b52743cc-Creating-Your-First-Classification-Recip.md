---
title: Creating Your First Classification RecipeOnce you’ve followed the steps in
  Creating Your First Recip
category: Start Here7 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-your-first-classification-recipe
source_page: https://docs.overview.ai/docs/start-here
parent_category: Start Here7 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:19:44.171018'
chunk_id: e1d0ed16
chunk_index: 1
total_chunks: 4
chunk_title: Classification Block
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 131
chunked_at: '2025-07-01T17:23:34.483986'
chunking_method: header_based
---

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
