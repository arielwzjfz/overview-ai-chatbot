---
title: "Setting up MQTT CommunicationThe camera can work with Node-RED and MQTT requests to communicate with other devices. The MQTT requests are used to get information, trigger the camera, or send information. Note The camera's IP address must be in the same range as the device ..."
category: "Walkthroughs10 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/setting-up-mqtt-communication-1"
source_page: "https://docs.overview.ai/docs/clone-walkthroughs"
parent_category: "Walkthroughs10 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:00.292983"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/setting-up-mqtt-communication-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/setting-up-mqtt-communication-1 "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/setting-up-mqtt-communication-1 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Setting up MQTT Communication

  *  __04 Feb 2025



  *  __ Print

  *  __ PDF




 __Contents

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

###### What's Next

  * [ Trigger using MQTT Communication ](/docs/trigger-using-mqtt-communication-1) __



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
