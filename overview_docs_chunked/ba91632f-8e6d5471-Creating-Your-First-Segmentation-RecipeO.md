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
chunk_id: ba91632f
chunk_index: 6
total_chunks: 10
chunk_title: 'Code sample: Pass if the total number of pixels detected is less than
  the defined threshold'
chunk_level: 3
chunk_start_line: 185
chunk_end_line: 214
chunked_at: '2025-07-01T17:23:34.423252'
chunking_method: header_based
---

### Code sample: Pass if the total number of pixels detected is less than the defined threshold

Copy and paste the following logic:
         
         const threshold = 5000; // Define the threshold value for the total pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const totalArea = allBlobs.reduce((sum, blob) => sum + blob.pixel_count, 0); // Calculate the total pixel count of all blobs
         
         msg.payload = totalArea < threshold; // Set the payload to true if the total area is less than the threshold, otherwise false
         
         return msg; // Return the modified message object

  6. Click **Done**.  


  7. Click **Deploy**.  


  8. Continue to [Train Segmentation Model](/v1/docs/ov80i-creating-your-first-segmentation-recipe#train-segmentation-model).




> **Note**
> 
> For more information about the **IO Block** page, see [IO Block and Node-RED Logic](/docs/io-and-node-red-logic).
