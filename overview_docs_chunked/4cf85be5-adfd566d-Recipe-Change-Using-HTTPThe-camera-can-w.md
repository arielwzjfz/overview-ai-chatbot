---
title: Recipe Change - Using HTTPThe camera can work with Node-RED and an HTTP endpoint
  to request a recipe
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/recipe-change-using-http-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:59.574035'
chunk_id: 4cf85be5
chunk_index: 0
total_chunks: 2
chunk_title: Recipe Change - Using HTTP
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 136
chunked_at: '2025-07-01T17:23:34.155803'
chunking_method: header_based
---

# Recipe Change - Using HTTP

  *  __Updated on 04 Feb 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The camera can work with Node-RED and an HTTP endpoint to request a recipe change. Since the port is open, other devices can also request a recipe change from the camera. Below is a flow that demonstrates how the function operates:

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(114\).png)

  
You can download and import this flow using the JSON file below:

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/RecipeChangeV18.json)RecipeChangeV18

3.17 KB

  
**Inject Node:** This block is an inject setup where we send the recipe number. It is possible to open this port for TCP or MQTT to send a message from another device.

> Note
> 
> The recipe ID is found in the URL.  
>   
> ![image\(113\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(113\).png)

  
**Function Node:** This function sets up the correct syntax for the message. It takes the recipe number from the **Inject node** and formats it properly for the POST request.

**HTTP Request Node:** Set up the endpoint where the message will be sent.

**Debug Nodes:** These nodes are used to monitor the message flow. If the message is not received correctly, there will be a bad response.

> Note
> 
> Example of a bad response:  
>   
> ![image\(115\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(115\).png)

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
