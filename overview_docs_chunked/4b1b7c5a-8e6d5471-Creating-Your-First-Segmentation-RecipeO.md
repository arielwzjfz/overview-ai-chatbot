---
title: Creating Your First Segmentation RecipeOnce you’ve followed the steps in Creating
  Your First Recipe
category: OV20i
language: English
url: https://docs.overview.ai/docs/ov80i-creating-your-first-segmentation-recipe
source_page: https://docs.overview.ai/start-here-1
parent_category: OV80i
is_individual_article: true
scraped_at: '2025-06-30T17:20:43.905651'
chunk_id: 4b1b7c5a
chunk_index: 4
total_chunks: 10
chunk_title: 'Code sample: Pass if no pixels are detected'
chunk_level: 3
chunk_start_line: 159
chunk_end_line: 171
chunked_at: '2025-07-01T17:23:34.423223'
chunking_method: header_based
---

### Code sample: Pass if no pixels are detected

Copy and paste the following logic:
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const results = allBlobs.length < 1; // Check if there are no blobs and store the result (true or false)
         
         msg.payload = results; // Set the payload to the result of the check
         
         return msg; // Return the modified message object
