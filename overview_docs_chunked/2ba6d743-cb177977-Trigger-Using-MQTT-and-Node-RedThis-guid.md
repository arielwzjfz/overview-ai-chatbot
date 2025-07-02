---
title: Trigger Using MQTT and Node-RedThis guide walks you through configuring and
  using MQTT communication
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/trigger-using-mqtt
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:32.642481'
chunk_id: 2ba6d743
chunk_index: 5
total_chunks: 9
chunk_title: 2\\. Configure the flow
chunk_level: 3
chunk_start_line: 111
chunk_end_line: 150
chunked_at: '2025-07-01T17:23:34.492083'
chunking_method: header_based
---

### 2\. Configure the flow

For the MQTT request to work there needs to me a message object sent to the different topics, for that we create a flow that explains the setup, in which there needs to be 2 messages, the first one is to put the camera in a HMI mode, and the second one asking to trigger the camera.

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28194%29.png)

  1. Configure the **\[Inject\]** node

     * Double click on the inject node
     * **\[msg.payload\]** : It can be left as a timestamp, as the inject will work on this exercise as the start point or pulse for the trigger.
     * Save
  2. Configure the first **\[Change\]** node

     * Double click on the change node
     * Set up these 2 rules:
       * Click on add -> SET -> msg.topic to the value of : \[stream\_mode/set\]
       * Click on add again -> SET -> msg.payload to the value of: \[HMI\_MODE\]
     * Save  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28195%29.png)
  3. Configure the second **\[Change\]** node

     * Double click on the change node
     * Set up these 2 rules:
       * Click on add -> SET -> msg.topic to the value of : \[hmi/?/capture\_mode\]
       * Click on add again -> SET -> msg.payload to the value of: \[single\]
     * Save  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28196%29.png)



**Important**

The unique recipe number is not the same as the PLC recipe number. The recipe number can be found at the top of the URL of an active recipe. It will change depending on the recipe, and there won't be two that are the same.  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28184%29.png)

  4. Connect to the **\[Mqtt In\]** node you already configured


