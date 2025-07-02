---
title: Setting up MQTT CommunicationThe camera can work with Node-RED and MQTT requests
  to communicate with
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/setting-up-mqtt-communication-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:00.292983'
chunk_id: 8ca156f7
chunk_index: 0
total_chunks: 2
chunk_title: Setting up MQTT Communication
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 125
chunked_at: '2025-07-01T17:23:34.374569'
chunking_method: header_based
---

# Setting up MQTT Communication

  *  __Updated on 04 Feb 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The camera can work with Node-RED and MQTT requests to communicate with other devices. The MQTT requests are used to get information, trigger the camera, or send information.

> Note
> 
> The camera's IP address must be in the same range as the device it is communicating with.

  1. Navigate to the **IO Block** to configure the Node-RED logic.

  2. A communication port \(**mqtt in**\) must be opened, where we assign the port we want the camera to listen to.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(102\).png)  


  3. Set up the **Server** the camera will be communicating with and the **Topic**.  


  4. To send a response to that port, use the **mqtt out** and set up the **Server** and **Topic** of the message.  





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
