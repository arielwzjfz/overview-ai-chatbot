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
chunk_id: 4372a923
chunk_index: 2
total_chunks: 4
chunk_title: IO Block
chunk_level: 2
chunk_start_line: 131
chunk_end_line: 206
chunked_at: '2025-07-01T17:23:34.484001'
chunking_method: header_based
---

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
