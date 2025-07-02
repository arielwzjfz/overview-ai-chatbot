---
title: Recipe Change Using Node-RED and HTTPThis guide shows you how to change recipes
  on your OV20 camera
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/recipe-change-http
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:33.332028'
chunk_id: 20f2f24d
chunk_index: 7
total_chunks: 9
chunk_title: Testing and Verification
chunk_level: 2
chunk_start_line: 158
chunk_end_line: 171
chunked_at: '2025-07-01T17:23:34.003599'
chunking_method: header_based
---

## Testing and Verification

To verify your setup works correctly:

  1. Click the button on the inject node to trigger the HTTP request
  2. Check the debug panel for the response
  3. Verify that the camera has switched to the specified recipe



Expected result: If the node configuration is correct, the recipe will change to the one required. If there is any issue on the flow, there will be a response on the debug that shows "success: false".  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28187%29.png)
