---
title: Configure pass/fail logic for a classification recipeActivate and edit a classification
  recipe. Make
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/create-a-classifier-node-red-logic-2-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:58.868265'
chunk_id: f09c3e8f
chunk_index: 0
total_chunks: 2
chunk_title: Configure pass/fail logic for a classification recipe
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 134
chunked_at: '2025-07-01T17:23:34.366992'
chunking_method: header_based
---

# Configure pass/fail logic for a classification recipe

  *  __Updated on 07 Mar 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

  1. Activate and edit a classification recipe.  


  2. Make sure all the AI blocks are trained before you edit the Node-RED logic. Click **Configure IO** and then select **Advanced Settings** to enter the Node-RED flow editor.   
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-2yj5gjxp.png)   


  3. Locate the **Classification Block Logic** Node in the default flow, or add it to your flow from the nodes menu on the left. All purple nodes in Node-RED represent Overview Logic Blocks. These blocks are integral to the overall classification logic. For a comprehensive understanding of each block, refer to [_IO Block and Node-RED Logic_](/docs/io-and-node-red-logic).  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-p70q9oo3.png)

  4. From the dropdown menu on the left, select the **Inspection Region/ROI** you wish to include in the logic. You may also set a **Confidence Threshold** for the inspection. You can use the confidence to tune sensitivity, but generally it is not required.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-sagdmq0m.png)

  5. Choose the **Target Class** that the model should identify. For example, select the corresponding target class if you want the model to pass items with a "pass" classification.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-7btf5sqv.png)

  6. If the model requires additional regions of interest, you can add more ROIs to the logic. Additionally, you may select if any or all of the rules must be true in order for the inspection to pass. By default, all rules must pass.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-5o4bmoow.png)

  7. After configuring all necessary settings, click on the **Deploy** button in the upper right corner of the Node-RED editor to save and deploy the logic. Verify that the model operates as expected by testing with sample data from the **HMI** page.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-bfu0nu3f.png)




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
