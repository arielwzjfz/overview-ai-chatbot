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
chunk_id: 593a167f
chunk_index: 5
total_chunks: 7
chunk_title: 'Code sample: Pass if the total number of pixels detected is less than
  the defined threshold'
chunk_level: 3
chunk_start_line: 184
chunk_end_line: 250
chunked_at: '2025-07-01T17:23:34.111554'
chunking_method: header_based
---

### Code sample: Pass if the total number of pixels detected is less than the defined threshold

Copy and paste the following logic:
         
         const threshold = 5000; // Define the threshold value for the total pixel count
         
         const allBlobs = msg.payload.segmentation.blobs; // Extract the blobs from the payload's segmentation data
         
         const totalArea = allBlobs.reduce((sum, blob) => sum + blob.pixel_count, 0); // Calculate the total pixel count of all blobs
         
         msg.payload = totalArea < threshold; // Set the payload to true if the total area is less than the threshold, otherwise false
         
         return msg; // Return the modified message object

  7. Click **Done**.  


  8. Click **Deploy**.  





> **Note**
> 
> For more information about the **IO Block** page, see [IO Block and Node-RED Logic](/docs/io-and-node-red-logic).

Was this article helpful?

__Yes __No

Thank you for your feedback\! Our team will get back to you

How can we improve this article?

Your feedback

Need more information

Difficult to understand

Inaccurate or irrelevant content

Missing/broken link

Others

Comment

Comment \(Optional\)

Character limit : 500

Please enter your comment

Email \(Optional\)

Email

Notify me about change  


Please enter a valid email

Cancel
