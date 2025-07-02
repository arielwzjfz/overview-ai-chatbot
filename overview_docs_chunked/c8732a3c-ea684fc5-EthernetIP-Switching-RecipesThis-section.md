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
chunk_id: c8732a3c
chunk_index: 4
total_chunks: 11
chunk_title: '1\\. Moving the Recipe Value:'
chunk_level: 3
chunk_start_line: 108
chunk_end_line: 112
chunked_at: '2025-07-01T17:23:34.312118'
chunking_method: header_based
---

### **1\. Moving the Recipe Value:**

A MOVE instruction transfers the current recipe value from a PLC tag to the camera tag \(OV20i:[O.Data](http://O.Data)\[4\]\). This action ensures that the correct recipe data is sent to the camera for processing.
