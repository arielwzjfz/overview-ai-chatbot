---
title: Using the ClassifierNote Download the sample recipe here . From the All Recipes
  page, click + New Re
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-a-basic-single-roi-classifier-1
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:04.008412'
chunk_id: eb947c13
chunk_index: 1
total_chunks: 3
chunk_title: Configure pass/fail logic
chunk_level: 2
chunk_start_line: 162
chunk_end_line: 238
chunked_at: '2025-07-01T17:23:34.133936'
chunking_method: header_based
---

## Configure pass/fail logic

In the steps below, we’ll walk you through configuring pass/fail logic for a classification recipe using Node-RED logic.

> **Note**
> 
> Ensure all the **AI Blocks** are trained \(green\) before editing the **IO Block**.
> 
> ![Recipe Editor - AI Blocks trained](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Recipe%20Editor%20-%20AI%20Blocks%20trained.png)

  1. Navigate to **IO Block** using the breadcrumb menu or select **Configure I/O** from the **Recipe Editor** page.

![Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Recipe%20Editor%20Breadcrumb%20Menu.png)

  2. Locate the **Classification Block Logic** Node in the default flow, or add it to your flow from the nodes menu on the left. All purple nodes in Node-RED represent Overview Logic Blocks. These blocks are integral to the overall classification logic. For a comprehensive understanding of each block, refer to [_IO Block and Node-RED Logic_](/docs/io-and-node-red-logic).

![create-a-classifier-node-red-logic-2-image-p70q9oo3](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-p70q9oo3.png)

  3. Double-click on the node to edit it. From the **Inspection Region / ROI** dropdown menu on the left, select the ROI you wish to include in the logic. You can also set a confidence threshold for the inspection. You can use the confidence to tune sensitivity, but generally it is not required.

![create-a-classifier-node-red-logic-2-image-sagdmq0m](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-sagdmq0m.png)

  4. Select a **Target Class** that the model should identify. For example, select the corresponding target class if you want the model to pass items with a "pass" classification.

![create-a-classifier-node-red-logic-2-image-7btf5sqv](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-7btf5sqv.png)

  5. If the model requires additional regions of interest, you can add more ROIs to the logic. Additionally, you can select if any or all of the rules must be true in order for the inspection to pass. By default, all rules must pass.

![create-a-classifier-node-red-logic-2-image-5o4bmoow](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/create-a-classifier-node-red-logic-2-image-5o4bmoow.png)

  6. After configuring all necessary settings, click **Done** in the top-right corner and then click on **Deploy** in the top-right corner of the Node-RED editor to save and deploy the logic. Verify that the model operates as expected by testing with sample data from the **HMI** page.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(118\).png)




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
