---
title: Ethernet/IP - Switching RecipesThis section outlines the process for changing
  the recipe in the came
category: PLC Communication5 Articlesin this category
language: English
url: https://docs.overview.ai/docs/plc-communication-ethernetip-recipe-switch
source_page: https://docs.overview.ai/docs/ethernet
parent_category: PLC Communication5 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:22.116905'
chunk_id: 05e0123f
chunk_index: 6
total_chunks: 11
chunk_title: '3\\. Confirming Recipe Switch Completion:'
chunk_level: 3
chunk_start_line: 116
chunk_end_line: 122
chunked_at: '2025-07-01T17:23:34.312152'
chunking_method: header_based
---

### **3\. Confirming Recipe Switch Completion:**

Once the camera processes the recipe switch, the system waits for confirmation. The OV20i:I.Data\[0\].2 input bit goes high to indicate that the recipe switch is complete.

Simultaneously, the system compares the current recipe data \(OV20i:I.Data\[8\]\) with the expected recipe value \(OV20i:O.Data\[4\]\) using an EQ \(Equal\) instruction. If the values match, the Recipe\_Match bit is set high, confirming that the correct recipe has been loaded.
