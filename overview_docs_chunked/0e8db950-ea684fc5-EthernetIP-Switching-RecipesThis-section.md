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
chunk_id: 0e8db950
chunk_index: 8
total_chunks: 11
chunk_title: '5\\. Error Detection:'
chunk_level: 3
chunk_start_line: 126
chunk_end_line: 149
chunked_at: '2025-07-01T17:23:34.312184'
chunking_method: header_based
---

### **5\. Error Detection:**

The ladder logic also includes error detection mechanisms. If an error occurs during the recipe switch process, it is detected by monitoring the OV20i:I.Data\[1\].1 input bit. The error is flagged by setting the Error\_Detected bit high, which can be used to trigger an alert or halt the process until the issue is resolved.

> **Summary of Key Points**
> 
>   * **Camera Connection:** Ensure proper connection between the camera and PLC.
> 
>   * **Recipe Number:** Move the desired recipe number to Camera\_1:O.Data\[4\].
> 
>   * **RECIPE\_SWITCH Trigger:** Use Recipe\_ONS to trigger the switch while ensuring the camera is not busy \(Camera\_1:I.Data\[1\].6\).
> 
>   * **Latch Recipe Switch Request:** Set and latch Camera\_1:O.Data\[0\].1 for the switch request.
> 
>   * **Verify Recipe and Acknowledge:** Confirm match between Camera\_1:I.Data\[8\] and Camera\_1:O.Data\[4\] and check Camera\_1:I.Data\[0\].2.
> 
>   * **Unlatch Request:** Unlatch Camera\_1:O.Data\[0\].1 after confirmation.
> 
>   * **Error Monitoring:** Watch for Camera\_1:I.Data\[1\].1 to handle any errors.
> 
> 

