---
title: "PROFINETThis guide will walk you through setting up PROFINET on your OV20i. Enabling PROFINET The first step will be to connect to the OV20i software and navigate to the Industrial Ethernet menu on the left-hand side. From this menu, complete the..."
category: "PLC Communication5 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/plc-communication-profinet"
source_page: "https://docs.overview.ai/docs/ethernet"
parent_category: "PLC Communication5 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:24.226867"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/plc-communication-profinet "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/plc-communication-profinet "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/plc-communication-profinet "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



PROFINET

  *  __17 Dec 2024



  *  __ Print

  *  __ PDF




 __Contents

# PROFINET

  *  __Updated on 17 Dec 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This guide will walk you through setting up PROFINET on your OV20i.

## Enabling PROFINET

The first step will be to connect to the OV20i software and navigate to the **Industrial Ethernet** menu on the left-hand side. From this menu, complete the following steps:

  1. Select **PROFINET** protocol to enable communication with your PLC \(top left\).

> **Note**
> 
> The Industrial Ethernet menu allows you to enable PROFINET as a global setting for the OV20i. After PROFINET has been selected, you will still need to enable PLC Triggering and the Inspection Pass/Fail function in the Recipe Editor \(more details below\) for any recipes that will be controlled by your PLC.

  2. Note your OV20i’s network settings in the **Device Information** window. We recommend you set a Static IP for the device. For instructions on that process, see [Connecting via an Ethernet Network](https://docs.overview.ai/docs/electrical-and-communication#connecting-via-an-ethernet-network).

  3. Change the PROFINET Device Name to whatever you would like. Hit save. These should be unique if you have multiple OV20i’s communicating with the same PLC.

  4. Download the GSD file.

  5. To enable PLC Triggering for a given recipe, navigate to the **Recipe Editor** and then to the **Imaging Setup** menu. Under **Trigger Settings** , select **PLC Trigger** to allow the PLC to trigger the camera using the PROFINET output assembly bit.

> **Note**
> 
> Once PLC Trigger has been selected, the camera will no longer be able to trigger manually from the software or provide a live camera view—only the PLC Trigger will capture a new image. For this reason you may find it helpful to keep Manual Trigger enabled while getting the cameras mounted and working on the AI Blocks, and switch over to a PLC Trigger when you are ready to control captures via the PLC.

  6. The Inspection Pass function in the PROFINET input assembly will always be set to 0 for new recipes by default. You can use the[IO Block](/docs/io-and-node-red-logic)to define pass/fail conditions for a recipe, which will set the Inspection Pass bit to equal 1 for passing images and 0 for failing images. You can use the Classification Block Logic node in the IO Block to configure pass/fail conditions without writing any scripts—see Classification Block Logic Setup for details. You can also use the IO Block to send and receive custom data for more complex inspections.




### PROFINET Tag Mapping

Use the following IO Module Reference Table to start communicating with your OV20i.

### GSDML file for TIA portal

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/OV20i_GSDML \(1\).zip)OV20i\_GSDML \(1\)

5.46 KB

> **💡 Keep in mind**
> 
> To assign a permanent static IP to the camera, users must set it in TIAPortal during the standard procedure for setting up a PROFINET device. If users wish to revert to the default IP address \(192.168.0.100\) and disable PROFINET, they should connect via microUSB at 192.168.55.1, deactivate PROFINET, switch to DHCP with Fallback, and then reboot the camera.

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

  * [ UR Communication - TCP/IP ](/docs/ur-communication-tcpip) __



Table of contents

    * Enabling PROFINET 



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
