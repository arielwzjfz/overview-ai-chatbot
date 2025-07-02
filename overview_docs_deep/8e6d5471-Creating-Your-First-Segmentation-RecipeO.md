---
title: "Creating Your First Segmentation RecipeOnce you’ve followed the steps in Creating Your First Recipe to configure the Imaging Setup , Template Image and Alignment , and Inspection Setup , follow the steps below to train a Segmentation model. Label and Train In this section, you’l..."
category: "OV20i"
language: "English"
url: "https://docs.overview.ai/docs/ov80i-creating-your-first-segmentation-recipe"
source_page: "https://docs.overview.ai/start-here-1"
parent_category: "OV80i"
is_individual_article: True
scraped_at: "2025-06-30T17:20:43.905651"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/ov80i-creating-your-first-segmentation-recipe "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/clone-creating-your-first-segmentation-recipe "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/ov80i-creating-your-first-segmentation-recipe "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Creating Your First Segmentation Recipe

  *  __07 Mar 2025



  *  __ Print

  *  __ PDF




 __Contents

# Creating Your First Segmentation Recipe

  *  __Updated on 07 Mar 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Once you’ve followed the steps in [Creating Your First Recipe](/docs/ov80i-creating-your-first-recipe) to configure the **Imaging Setup** , **Template Image and Alignment** , and **Inspection Setup** , follow the steps below to train a **Segmentation** model.

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

## IO Block

In this section, you’ll define the pass/fail logic for your Recipe using Node-RED logic.

  1. Select the **IO Block** tab. Alternatively, select **IO Block** from the **Recipe Editor**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(160\).png)

  2. Define the criteria for the model to pass or fail. For example, specify that the model should fail if the ‘Center X’ coordinate of all detected blobs is not exactly 1000 pixels.   


> **Tip**
> 
> If you want more advanced settings, click **Advanced mode** in the top-right corner and go to [Advanced Mode](/v1/docs/ov80i-creating-your-first-segmentation-recipe#advanced-mode).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(161\).png)




### Advanced Mode

  1. Right-click on the **Classification Block Logic** node and select **Delete Selection**.

![Segmentation IO Block - keychain\(1\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation%20IO%20Block%20-%20keychain\(1\).png)

  2. Right-click and select **Insert > Node > Function**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation IO Insert Node - keychain.png)

  3. Reconnect the nodes.

![Segmentation IO Block - keychain](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation%20IO%20Block%20-%20keychain.png)

  4. Double-click on the **function 1** node.

  5. Copy and paste the desired example code from the code samples below into the **On Message** tab.

### Code sample: Pass if no pixels are detected

Copy and paste the following logic:
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const results = allBlobs.length < 1; // Check if there are no blobs and store the result (true or false)
         
         msg.payload = results; // Set the payload to the result of the check
         
         return msg; // Return the modified message object

### Code sample: Pass if all blobs detected are smaller than the defined threshold

Copy and paste the following logic:
         
         const threshold = 500; // Define the threshold value for pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const allUnderThreshold = allBlobs.every(blob => blob.pixel_count < threshold); // Check if all blobs have a pixel count less than the threshold
         
         msg.payload = allUnderThreshold; // Set the payload to the result of the check
         
         return msg; // Return the modified message object

### Code sample: Pass if the total number of pixels detected is less than the defined threshold

Copy and paste the following logic:
         
         const threshold = 5000; // Define the threshold value for the total pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const totalArea = allBlobs.reduce((sum, blob) => sum + blob.pixel_count, 0); // Calculate the total pixel count of all blobs
         
         msg.payload = totalArea < threshold; // Set the payload to true if the total area is less than the threshold, otherwise false
         
         return msg; // Return the modified message object

  6. Click **Done**.  


  7. Click **Deploy**.  


  8. Continue to [Train Segmentation Model](/v1/docs/ov80i-creating-your-first-segmentation-recipe#train-segmentation-model).




> **Note**
> 
> For more information about the **IO Block** page, see [IO Block and Node-RED Logic](/docs/io-and-node-red-logic).

## Train Segmentation Model

In this section, you’ll train the model using the images labeled earlier.

  1. Select the **Label and Train** tab. Alternatively, select **Label and Train** from the **Recipe Editor**.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(162\).png)  


  2. Click **Train Segmentation Model**.  


  3. Optional step: Adjust the **Number of Iterations \(Epochs\)** to set how many times the labeled images are shown by going to **Advanced Settings > Parameters**.   


> **Note**
> 
> Increasing the number of iterations will improve the model’s accuracy, but will also take longer to train.

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(164\).png)  


  4. Click **Start Training**. A modal will display the progress of the training.   


  5. Once the model is trained, use the **Live Preview Mode** or the [HMI](/docs/hmi) tab to verify the functionality of your Recipe. Place different examples of the object in the camera’s field of vision and verify the model classifies each example correctly.

## Next Steps

Go back to the [setup page](/docs/ov80i-recommended-setup-flow) and select the next step.




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

  * [ OV80i Technical Specifications ](/docs/technical-specifications-ov80i-1) __



Table of contents

    * Label and Train 
    * IO Block 
    * Train Segmentation Model 
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
