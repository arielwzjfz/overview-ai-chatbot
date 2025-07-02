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
chunk_id: cfa7e631
chunk_index: 5
total_chunks: 10
chunk_title: 'Code sample: Pass if all blobs detected are smaller than the defined
  threshold'
chunk_level: 3
chunk_start_line: 171
chunk_end_line: 185
chunked_at: '2025-07-01T17:23:34.423238'
chunking_method: header_based
---

### Code sample: Pass if all blobs detected are smaller than the defined threshold

Copy and paste the following logic:
         
         const threshold = 500; // Define the threshold value for pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const allUnderThreshold = allBlobs.every(blob => blob.pixel_count < threshold); // Check if all blobs have a pixel count less than the threshold
         
         msg.payload = allUnderThreshold; // Set the payload to the result of the check
         
         return msg; // Return the modified message object
