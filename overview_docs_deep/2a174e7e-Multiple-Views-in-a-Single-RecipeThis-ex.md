---
title: "Multiple Views in a Single RecipeThis example shows you how to set up a single recipe that can inspect different parts, angles, or views without switching to other recipes. There are a variety of reasons to do this, but two primary use cases are: when there isn't enough tim..."
category: "Walkthroughs10 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/multiple-views-one-recipe-1"
source_page: "https://docs.overview.ai/docs/clone-walkthroughs"
parent_category: "Walkthroughs10 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:56.066147"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/multiple-views-one-recipe-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/multiple-views-one-recipe-1 "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/multiple-views-one-recipe-1 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Multiple Views in a Single Recipe

  *  __07 Mar 2025



  *  __ Print

  *  __ PDF




 __Contents

# Multiple Views in a Single Recipe

  *  __Updated on 07 Mar 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This example shows you how to set up a single recipe that can inspect different parts, angles, or views without switching to other recipes. There are a variety of reasons to do this, but two primary use cases are:

  1. when there isn't enough time between captures to change recipe,

  2. when performing the same inspection on multiple parts or angles of a part \(eg., presence/absence of studs on five different positions in a car body\). In this case, this method prevents the need to train the same model \(stud presence/absence\) multiple times across different recipes.




  
**Importable Example flow for download:**

> **Note**
> 
> Configuration inside Classification Block Logic nodes will be lost on import.

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/flows \(2\).json)flows \(2\)

7.76 KB

This example is a simple version with two views and one inspection type, but you can use this same technique for an unlimited number of inspection types and views. This inspection we will look for the presence/absence of bits on two sides of a drill bit case. One side has five bits on the bottom, and the other side has eight bits on both the top and bottom. We will call the side with 16 bits side A and five bits side B.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(77\).png)

Side A \(16 bits\)

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(76\).png)

Side B \(five bits\)

## Create and Train a New Recipe

Instead of one recipe per side, because of the different layouts, we will combine both sides into one recipe so we don’t need to train the same presence/absence model twice.

  1. Create a recipe. In this case, it is a classification recipe but this same principle can be used with segmentation.

  2. Set up the **Template Image and Alignment** for the first view:  


> **Note**
> 
> The Aligner is unavailable when inspecting more than one view on the same recipe. The Template Image and Aligner is only used to set the base image for the **Inspection Setup**.

  3. Draw ROIs for side A. Name them something that helps identify which side they belong to. In this case, we named the ROIs A1-A16.   


  4. Return to the **Template Image and Alignment** to replace the image with side B, either from a new capture or from the library.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(79\).png)

  5. Use the lock icons next to each ROI to avoid moving any ROIs from side A, then draw and name the ROIs for side B.  


> **Note**
> 
> For more complex recipes, repeat this process for as many different views as you want to inspect.

  6. Label and train the classification model using images from both sides A and B. When capturing and labeling side A, do not label the side B ROIs and vice versa.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(84\).png)

Labeling side A, Pass

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(85\).png)

Labeling side A, Fail

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(82\).png)

Labeling side B, Pass

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(83\).png)

Labeling side B, Fail




## Configure Node-RED Logic

  1. Navigate to the **IO Block** \(**Configure IO** from the Recipe Editor\) and select **Advanced Settings** to open your Node-RED flow. Create a source to tell the OV80i which side is currently being inspected. This can be robot position data, information from the PLC, or anything else you want to use. In the example below, we will simulate this using two **Inject nodes** , one that sends the string "A" and one that sends the string "B".

  2. Since the side data coming in might be momentary, but we want to check to see which side is active, we will store the state data using a **Flow variable** , which will persist until the next side information is received. Hook your data source up to a function block containing the following code:  

         
         flow.set('side',msg.payload);
         return msg;

  
![image\(86\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(86\).png)

  3. You can test to see if your side data is being properly stored by opening up the **context** data sidebar, sending a message, and then hitting **refresh** on the **Flow variable pane**. The flow data pane will only update when manually refreshed using the small **refresh** button.  
  
![image\(87\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(87\).png)  
  


  4. Once the side data is properly stored in the **Flow variable** , add a **switch node** connected to **All Block Outputs**. This will be the block that routes the message with the inspection data according to which side is active in the **Flow variable**. Configure it to look at the **Flow variable** and route the message to port 1 if A is active and 2 if B is active.  
  
![image\(88\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(88\).png)

> **Note**
> 
> For more complex recipes, repeat this process for as many different views as you want to inspect.

  5. Connect each output port of the **switch** to a **Classification Block Logic block** , and configure each one according to the rules you want to inspect for that side. The **switch node** will only route a message to one of the nodes at a time. The image below shows the configuration for the B-side port of the switch. Notice it doesn't reference any of the A ROIs, so the logic will ignore that side's results when the inspection is routed through this node.  
  
![image\(89\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(89\).png)  
  


  6. Finally, hook the **logic blocks** up to the **Inspection Pass/Fail block**. This allows the results to show up on the HMI, as well as be passed to any attached PLC or other flow component.  





## Test the Recipe

This completes the Node-RED flow and now it's time to test the recipe end-to-end. 

  1. First, we will send the A-side command using our Node-RED **inject node**. Then we will use the HMI to inspect a good part. Notice how despite one of the B-side regions failing, the whole inspection passed.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(91\).png)

  2. Now when we remove a drill bit on the A-side, and inspect again, we get the failure result we want.  


  3. Moving on to the B-side, we send the B signal using our Node-RED **inject** and **refresh** the **Flow variable** section in the **context data pane** to make sure that it’s stored.  


  4. Now when we flip to the B-side of a good part, we see that the inspection passes despite the A-side regions all failing.  





Congratulations\! You now know how to use one recipe and model across multiple views of a part. This will allow complex inspections at high speeds and tight integration with robots. It will also save you significant time that would be spent training multiple models that do the same inspection, just on different views.

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

  * [ Adding data to an existing recipe and retraining ](/docs/adding-data-to-an-existing-recipe-and-retraining-1) __



Table of contents

    * Create and Train a New Recipe 
    * Configure Node-RED Logic 
    * Test the Recipe 



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
