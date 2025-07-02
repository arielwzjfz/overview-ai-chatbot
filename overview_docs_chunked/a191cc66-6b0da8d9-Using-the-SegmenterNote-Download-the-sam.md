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
chunk_id: a191cc66
chunk_index: 3
total_chunks: 7
chunk_title: Pass if no pixels are detected
chunk_level: 4
chunk_start_line: 189
chunk_end_line: 202
chunked_at: '2025-07-01T17:23:34.075414'
chunking_method: header_based
---

#### Pass if no pixels are detected

Copy and paste the following logic:
    
    
    const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
    
    const results = allBlobs.length < 1; // Check if there are no blobs and store the result (true or false)
    
    msg.payload = results; // Set the payload to the result of the check
    
    return msg; // Return the modified message object
