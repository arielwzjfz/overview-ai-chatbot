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
chunk_id: 22ee2320
chunk_index: 4
total_chunks: 7
chunk_title: 'Code sample: Pass if all blobs detected are smaller than the defined
  threshold'
chunk_level: 3
chunk_start_line: 170
chunk_end_line: 184
chunked_at: '2025-07-01T17:23:34.111538'
chunking_method: header_based
---

### Code sample: Pass if all blobs detected are smaller than the defined threshold

Copy and paste the following logic:
         
         const threshold = 500; // Define the threshold value for pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const allUnderThreshold = allBlobs.every(blob => blob.pixel_count < threshold); // Check if all blobs have a pixel count less than the threshold
         
         msg.payload = allUnderThreshold; // Set the payload to the result of the check
         
         return msg; // Return the modified message object
