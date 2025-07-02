---
title: "Trigger using MQTT CommunicationThe camera can work with Node-RED and MQTT requests to communicate with other devices. The MQTT requests are used to get information, trigger the camera, or send information. It is possible to trigger the camera using an MQTT request, sending a mess..."
category: "Walkthroughs10 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/trigger-using-mqtt-communication-1"
source_page: "https://docs.overview.ai/docs/clone-walkthroughs"
parent_category: "Walkthroughs10 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:00.991127"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/trigger-using-mqtt-communication-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/trigger-using-mqtt-communication-1 "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/trigger-using-mqtt-communication-1 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Trigger using MQTT Communication

  *  __04 Feb 2025



  *  __ Print

  *  __ PDF




 __Contents

# Trigger using MQTT Communication

  *  __Updated on 04 Feb 2025



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

###### What's Next

  * [ Send custom data from PLC to camera ](/docs/send-customdata-from-plc-to-camera-1) __



ENTER

ESC

 __

__

Eddy AI, facilitating knowledge discovery through conversational intelligence

Search Limit Exceeded. Please upgrade the plan.

Answer copied\!

__

__ __

No results found

Provide more context or information so that I can better understand and assist you
