---
title: Creating Your First Segmentation RecipeOnce you’ve followed the steps in Creating
  Your First Recipe
category: Start Here7 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-your-first-segmentation-recipe
source_page: https://docs.overview.ai/docs/start-here
parent_category: Start Here7 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:19:44.855808'
chunk_id: e40c459d
chunk_index: 2
total_chunks: 7
chunk_title: IO Block
chunk_level: 2
chunk_start_line: 134
chunk_end_line: 158
chunked_at: '2025-07-01T17:23:34.111506'
chunking_method: header_based
---

## IO Block

In this section, you’ll define the pass/fail logic for your Recipe using Node-RED logic.

  1. From the **Label and Train** page, use the breadcrumb menu to select **IO Block**. Alternatively, select **Configure IO** from the **Recipe Editor**.

![Segmeneter Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmeneter%20Recipe%20Editor%20Breadcrumb%20Menu.png)

  2. Right-click on the **Classification Block Logic** node and select **Delete Selection**.

![Segmentation IO Block - keychain\(1\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation%20IO%20Block%20-%20keychain\(1\).png)

  3. Right-click and select **Insert > Node > Function**.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation IO Insert Node - keychain.png)

  4. Reconnect the nodes.

![Segmentation IO Block - keychain](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmentation%20IO%20Block%20-%20keychain.png)

  5. Double-click on the **function 1** node.

  6. Copy and paste the desired example code from the code samples below into the **On Message** tab.
