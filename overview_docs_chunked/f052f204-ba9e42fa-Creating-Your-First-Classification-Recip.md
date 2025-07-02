---
title: Creating Your First Classification RecipeOnce you’ve followed the steps in
  Creating Your First Recip
category: OV20i
language: English
url: https://docs.overview.ai/docs/ov80i-creating-your-first-classification-recipe
source_page: https://docs.overview.ai/start-here-1
parent_category: OV80i
is_individual_article: true
scraped_at: '2025-06-30T17:20:43.189974'
chunk_id: f052f204
chunk_index: 3
total_chunks: 7
chunk_title: Advanced Mode
chunk_level: 3
chunk_start_line: 125
chunk_end_line: 160
chunked_at: '2025-07-01T17:23:34.230888'
chunking_method: header_based
---

### Advanced Mode

For this simple example, we’ll set the logic so that the ROI must be classified as “Pass” for the capture to result in a PASS. Other examples are available in [IO Block and Node-RED Logic](/docs/ov80i-io-block-and-node-red-logic).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/IO Block - keychain.png)

  1. Double-click on **Classification Block Logic** to open the edit tab.

![image-1728660513967](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image-1728660513967.png)

  2. Click **\+ add** at the bottom of the tab.  


  3. Under **Inspection Region / ROI** , select the relevant ROI you want to base the pass/fail logic on from the drop-down menu.  


  4. Under **Target Class** , select the class you want the logic to consider as a “pass” from the drop-down menu \(by default, this will be **pass\_\[Inspection Type Name\]**\).

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Edit node window - keychain.png)

  5. Click **Done**.  


  6. Click **Deploy**.  


  7. Continue to [Train Classification Model](/v1/docs/ov80i-creating-your-first-classification-recipe#train-classification-model).




> **Note**
> 
> For more information about the **IO Block** page, see [IO Block and Node-RED Logic](/docs/ov80i-io-block-and-node-red-logic).
