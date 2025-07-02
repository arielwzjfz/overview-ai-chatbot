---
title: Multiple Views in a Single RecipeThis example shows you how to set up a single
  recipe that can inspe
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/multiple-views-one-recipe
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:05.414696'
chunk_id: 67e765e1
chunk_index: 3
total_chunks: 5
chunk_title: Test the Recipe
chunk_level: 2
chunk_start_line: 187
chunk_end_line: 248
chunked_at: '2025-07-01T17:23:34.360426'
chunking_method: header_based
---

## Test the Recipe

This completes the Node-RED flow and now it's time to test the recipe end-to-end. 

  1. First, we will send the A-side command using our Node-RED **inject node**. Then we will use the HMI to inspect a good part. Notice how despite one of the B-side regions failing, the whole inspection passed.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(91\).png)

  2. Now when we remove a drill bit on the A-side, and inspect again, we get the failure result we want.  


  3. Moving on to the B-side, we send the B signal using our Node-RED **inject** and **refresh** the **Flow variable** section in the **context data pane** to make sure that it’s stored.  


  4. Now when we flip to the B-side of a good part, we see that the inspection passes despite the A-side regions all failing.  





Congratulations\! You now know how to use one recipe and model across multiple views of a part. This will allow complex inspections at high speeds and tight integration with robots. It will also save you significant time that would be spent training multiple models that do the same inspection, just on different views

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
