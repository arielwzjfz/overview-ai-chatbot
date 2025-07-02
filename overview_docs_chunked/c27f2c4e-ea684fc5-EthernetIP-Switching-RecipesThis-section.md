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
chunk_id: c27f2c4e
chunk_index: 5
total_chunks: 11
chunk_title: '2\\. Initiating the Recipe Switch:'
chunk_level: 3
chunk_start_line: 112
chunk_end_line: 116
chunked_at: '2025-07-01T17:23:34.312135'
chunking_method: header_based
---

### **2\. Initiating the Recipe Switch:**

The process begins with activating the "Recipe\_Switch" push button \(PB\). This action triggers a one-shot \(ONS\) signal, which initiates the recipe switch by setting the OV20i:O.Data\[0\].1 output bit high. This output is likely connected to the camera system to begin the recipe-switching process.
