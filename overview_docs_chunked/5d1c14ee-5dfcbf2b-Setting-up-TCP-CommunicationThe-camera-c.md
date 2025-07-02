---
title: Setting up TCP CommunicationThe camera can use Node-RED to communicate with
  other devices over TCP.
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/tcp-communication-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:57.476840'
chunk_id: 5d1c14ee
chunk_index: 0
total_chunks: 3
chunk_title: Setting up TCP Communication
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 83
chunked_at: '2025-07-01T17:23:34.304889'
chunking_method: header_based
---

# Setting up TCP Communication

  *  __Updated on 04 Feb 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The camera can use Node-RED to communicate with other devices over TCP.

> **Note**
> 
> The camera's IP address must be in the same range as the device it is communicating with.

  1. Navigate to the **IO Block** to configure the Node-RED logic.

  2. A communication port \(**tcp in**\) must be opened, where we assign the port we want the camera to listen to.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(98\).png)  


  3. To send a response to the port, we need to place a **tcp out** node, assign the IP address of the device we are communicating with, and assign a free port. Refer to the example below:  




