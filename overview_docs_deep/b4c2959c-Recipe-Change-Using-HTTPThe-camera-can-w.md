---
title: "Recipe Change - Using HTTPThe camera can work with Node-RED and an HTTP endpoint to request a recipe change. Since the port is open, other devices can also request a recipe change from the camera. Below is a flow that demonstrates how the function operates: You can dow..."
category: "Walkthroughs14 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/recipe-change-using-http"
source_page: "https://docs.overview.ai/docs/how-to-guides"
parent_category: "Walkthroughs14 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:10.239913"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/recipe-change-using-http "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/recipe-change-using-http "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/recipe-change-using-http "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Recipe Change - Using HTTP

  *  __29 Nov 2024



  *  __ Print

  *  __ PDF




 __Contents

# Recipe Change - Using HTTP

  *  __Updated on 29 Nov 2024



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

###### What's Next

  * [ Setting up MQTT Communication ](/docs/setting-up-mqtt-communication) __



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
