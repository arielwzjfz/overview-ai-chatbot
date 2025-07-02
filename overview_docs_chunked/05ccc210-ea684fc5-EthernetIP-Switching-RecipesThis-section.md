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
chunk_id: 05ccc210
chunk_index: 7
total_chunks: 11
chunk_title: '4\\. Allowing Re-initiation:'
chunk_level: 3
chunk_start_line: 122
chunk_end_line: 126
chunked_at: '2025-07-01T17:23:34.312168'
chunking_method: header_based
---

### **4\. Allowing Re-initiation:**

After confirming the match, the system allows for reinitiation of the recipe switching process by resetting the OV20i:O.Data\[0\].1 output bit. This reset ensures that the system is ready for the next recipe switch command.
