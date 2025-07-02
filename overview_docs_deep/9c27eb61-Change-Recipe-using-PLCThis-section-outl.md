---
title: "Change Recipe using PLCThis section outlines the process for changing the recipe in the camera using PLC logic. Each step and corresponding action are detailed to ensure proper integration and functionality. Note Make sure that the Recipe switch is not always ..."
category: "Walkthroughs14 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/change-recipe-using-plc"
source_page: "https://docs.overview.ai/docs/how-to-guides"
parent_category: "Walkthroughs14 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:08.231914"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/change-recipe-using-plc "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/change-recipe-using-plc "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/change-recipe-using-plc "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Change Recipe using PLC

  *  __27 Jan 2025



  *  __ Print

  *  __ PDF




 __Contents

# Change Recipe using PLC

  *  __Updated on 27 Jan 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This section outlines the process for changing the recipe in the camera using PLC logic. Each step and corresponding action are detailed to ensure proper integration and functionality.

> **Note**
> 
> Make sure that the Recipe switch is not always high before triggering.

**_Steps to Change Recipe_**

  1. Connect the Camera to the PLC. Refer to [Ethernet/IP - Establishing Communication](/docs/plc-communication-ethernetip-connections).




**_Important tags and steps_**

  * Set the recipe number you want to use by moving it to the Camera\_1:O.Data\[4\] register.

  * Trigger the RECIPE\_SWITCH

  * Check Camera\_1:I.Data\[1\].6 to ensure the camera is not busy before triggering the recipe switch. Use a one-shot rising edge signal Recipe\_ONS to trigger the switch.

  * Latch the Recipe Switch Request, Camera\_1:O.Data\[0\].1 to send the recipe switch request.

  * Verify Recipe Match and Acknowledgment

  * Once both conditions are met, the recipe match is confirmed.

  * Unlatch the Recipe Switch Request




** _Error Handling_**

  * After confirming the recipe match, unlatch the Camera\_1:O.Data\[0\].1 bit to complete the recipe switch process.

  * Monitor for errors during the process.

  * If an error occurs, Camera\_1:I.Data\[1\].1 will turn true.




**_Key Points_**

  * Camera Connection: Ensure proper connection between the camera and PLC.

  * Recipe Number: Move the desired recipe number to Camera\_1:O.Data\[4\].

  * RECIPE\_SWITCH Trigger: Use Recipe\_ONS to trigger the switch while ensuring the camera is not busy \(Camera\_1:I.Data\[1\].6\).

  * Latch Recipe Switch Request: Set and latch Camera\_1:O.Data\[0\].1 for the switch request.

  * Verify Recipe and Acknowledge: Confirm match between Camera\_1:I.Data\[8\] and Camera\_1:O.Data\[4\] and check Camera\_1:I.Data\[0\].2.

  * Unlatch Request: Unlatch Camera\_1:O.Data\[0\].1 after confirmation.

  * Error Monitoring: Watch for Camera\_1:I.Data\[1\].1 to handle any errors.




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

  * [ Troubleshooting the camera connection ](/docs/communication-troubleshooting) __



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
