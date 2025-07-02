---
title: Using the SegmenterNote Download the sample recipe here . From the All Recipes
  page, click + New Rec
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-a-segmenter
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:04.710671'
chunk_id: 452ec033
chunk_index: 1
total_chunks: 7
chunk_title: Configure pass/fail logic
chunk_level: 2
chunk_start_line: 154
chunk_end_line: 187
chunked_at: '2025-07-01T17:23:34.075374'
chunking_method: header_based
---

## Configure pass/fail logic

In the steps below, we’ll walk you through configuring pass/fail logic for a segmentation recipe using Node-RED logic.

> **Note**
> 
> Ensure all the **AI Blocks** are trained \(green\) before editing the **IO Block**.
> 
> ![Recipe Editor - Segmenter AI Blocks trained](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Recipe%20Editor%20-%20Segmenter%20AI%20Blocks%20trained.png)

  1. Navigate to **IO Block** using the breadcrumb menu or select **Configure I/O** from the **Recipe Editor** page.

![Segmeneter Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmeneter%20Recipe%20Editor%20Breadcrumb%20Menu.png)

  2. Delete the **Classification Block Logic** and build the following Node-RED flow by dragging in nodes from the left-hand side and connecting them.

![basic-segmenter-logic-using-node-red-image-djwdg0q6](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/basic-segmenter-logic-using-node-red-image-djwdg0q6.png)

  3. Double-click the **function 1****** node, then copy and paste the desired example code from the sections below into the **On Message** tab.

![image\(100\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(100\).png)

  4. Click **Done**.

  5. Click **Deploy**.

  6. Navigate to the **HMI** and test your logic.

### 



