---
title: Using the SegmenterNote Download the sample recipe here . From the All Recipes
  page, click + New Rec
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-a-segmenter
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:04.710671'
chunk_id: c6e9d387
chunk_index: 4
total_chunks: 7
chunk_title: Pass if all blobs detected are smaller than the defined threshold
chunk_level: 4
chunk_start_line: 202
chunk_end_line: 217
chunked_at: '2025-07-01T17:23:34.075432'
chunking_method: header_based
---

#### Pass if all blobs detected are smaller than the defined threshold

Copy and paste the following logic:
    
    
    const threshold = 500; // Define the threshold value for pixel count
    
    const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
    
    const allUnderThreshold = allBlobs.every(blob => blob.pixel_count < threshold); // Check if all blobs have a pixel count less than the threshold
    
    msg.payload = allUnderThreshold; // Set the payload to the result of the check
    
    return msg; // Return the modified message object
