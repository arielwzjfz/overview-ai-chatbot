---
title: Recipe Change Using Node-RED and HTTPThis guide shows you how to change recipes
  on your OV20 camera
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/recipe-change-http
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:33.332028'
chunk_id: 5ff124e5
chunk_index: 5
total_chunks: 9
chunk_title: 2\\. Configure the nodes
chunk_level: 3
chunk_start_line: 98
chunk_end_line: 148
chunked_at: '2025-07-01T17:23:34.003566'
chunking_method: header_based
---

### 2\. Configure the nodes

For the http request to work there needs to me a message object sent to the recipe Endpoint, the configuration of that endpoint, so in the flow we will need to configure the 3 nodes.

  1. Configure the **\[inject\]** node
     * Double click on the inject node
     * **\[msg.payload\]** : `[#Unique recipe number]`
     * Save



I**mportant**

The unique recipe number is not the same as the PLC recipe number. The recipe number can be found at the top of the URL of an active recipe. It will change depending on the recipe, and there won't be two that are the same.  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28184%29.png)

  2. Configure the **\[function\]** node
     * Double click on the function node
     * Insert this logic into the node:


    
    
    let recipeID = msg.payload;
    
    msg.headers = {
        'Content-Type': 'application/json'
    };
    msg.payload = JSON.stringify({ id: recipeID }); 
    return msg;
    
    

  * Save



**Note**

The HTTP POST requires an array of data to be structured correctly. That’s why we use a function to format it properly. The message sent will include both msg.headers and msg.payload; if either is not set up correctly, it won’t work.

  3. Configure the **\[HTTP\]** node


  * Double click on the Http node
  * Setup the **\[method\]** as Post
  * Change the **\[URL\]** to localhost:5001/pipeline/activate


