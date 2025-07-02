---
title: Trigger using MQTT CommunicationThe camera can work with Node-RED and MQTT
  requests to communicate w
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/trigger-using-mqtt-communication
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:11.558730'
chunk_id: b650b83d
chunk_index: 0
total_chunks: 2
chunk_title: Trigger using MQTT Communication
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 125
chunked_at: '2025-07-01T17:23:34.256442'
chunking_method: header_based
---

# Trigger using MQTT Communication

  *  __Updated on 29 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The camera can work with Node-RED and MQTT requests to communicate with other devices. The MQTT requests are used to get information, trigger the camera, or send information. It is possible to trigger the camera using an MQTT request, sending a message to a specific topic.

Below is a flow that demonstrates how the function operates:

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(110\).png)

  
You can download and import this flow using the JSON file below:

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Mqtt_Trigger\(2\).json)Mqtt\_Trigger

3.85 KB

**Inject Node:** This initiates the trigger process with a pulse. It can be modified to respond to a condition from the camera, a button on a dashboard, or other logic.

**Set Payload 1** : This triggers a condition in the camera to set its `stream_mode` or `set` topic with the `HMI_Mode` payload. This is the first step in the trigger process.

**Set Payload 2:** This condition is activated after a brief delay \(10ms\). This condition sets the `hmi/10/capture_mode` topic with a `SINGLE` payload. Note that the number in `hmi/NUMBER/capture_mode` must match the active URL of the camera.  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(112\).png)

**Output:** The last block is the output, which in this case is an MQTT message sent to a local host. If you need to send the message to a different host, you can specify it here by using the IP address of the target device.

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
