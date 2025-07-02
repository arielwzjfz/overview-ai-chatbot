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
chunk_id: 2033fd26
chunk_index: 3
total_chunks: 7
chunk_title: 'Code sample: Pass if no pixels are detected'
chunk_level: 3
chunk_start_line: 158
chunk_end_line: 170
chunked_at: '2025-07-01T17:23:34.111522'
chunking_method: header_based
---

### Code sample: Pass if no pixels are detected

Copy and paste the following logic:
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const results = allBlobs.length < 1; // Check if there are no blobs and store the result (true or false)
         
         msg.payload = results; // Set the payload to the result of the check
         
         return msg; // Return the modified message object
