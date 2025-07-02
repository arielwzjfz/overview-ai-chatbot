---
title: "Sending Messages to Microsoft Teams with Node-REDThis guide walks you through how to send inspection messages — including clickable images — from the OV20i camera to a Microsoft Teams channel using a webhook. By the end of this process, your OV20i will be able to post formatted notifications direc..."
category: "NODE-RED4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/sending-messages-to-microsoft-teams-with-node-red"
source_page: "https://docs.overview.ai/docs/node-red"
parent_category: "NODE-RED4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:31.163749"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/sending-messages-to-microsoft-teams-with-node-red "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/sending-messages-to-microsoft-teams-with-node-red "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/sending-messages-to-microsoft-teams-with-node-red "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Sending Messages to Microsoft Teams with Node-RED

  *  __14 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Sending Messages to Microsoft Teams with Node-RED

  *  __Updated on 14 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This guide walks you through how to send inspection messages — including clickable images — from the OV20i camera to a Microsoft Teams channel using a webhook. By the end of this process, your OV20i will be able to post formatted notifications directly into Teams.

* * *

## Overview

The OV20i includes Node-RED as part of its onboard interface, allowing you to automate notifications and share results in real time. Microsoft Teams supports incoming webhooks that receive messages in JSON format. By setting up a webhook in a Teams channel and configuring the Node-RED flow on the OV20i, you can push updates with image links directly into a shared team workspace.

## Prerequisites

Before you begin, ensure you have:

  * Your OV20i is connected to the plant network using a static IP or one provided by IT.
  * Microsoft Teams is accessible from the same network as the OV20i.
  * You have a Teams channel where you want to receive notifications.
  * Node-RED is running on the OV20i and accessible from your browser.



**Important**

The OV20i must be on the same network as your computer and Teams to send data. Ensure it receives a valid IP address from your IT team.

## Microsoft Teams Integration

### 1\. Create a Webhook in Microsoft Teams

  1. Open Microsoft Teams and go to the channel where you want to receive messages.
  2. Click the three dots \(•••\) next to the channel name >Manage channel > Connectors.
  3. Search for Incoming Webhook and click Add.
  4. Choose a name \(e.g., OV20i Inspection Alerts\) and optionally upload an icon.
  5. Click Create and copy the generated webhook URL. Save it — you'll use it in Node-RED.



## OV20i Node-Red

Required Nodes in Node-RED:

  * inject
  * function
  * http request
  * \(optional\) debug



### 1\. Inject

Use this for manual testing.

### 2\. Function Node

Use this function to format the message.
    
    
    msg.headers = {
        "Content-Type": "application/json"
    };
    
    msg.payload = {
        text: "You got a new message from your OV20i"
    };
    
    return msg;
    
    

You can also use msg.payload.image\_url if the image is coming dynamically from the inspection data, that way you can click on the link and open the image in a new window.
    
    
    let imageUrl = msg.payload.image_url;
    
    msg.headers = {
        "Content-Type": "application/json"
    };
    
    msg.payload = {
        text: `Inspection Image(${imageUrl})`
    };
    
    return msg;
    

### 3\. HTTP Request Node

  * Method: POST
  * URL: Paste the Teams webhook URL here
  * Return: UTF-8 string



### 4\. Debug Node \(Optional\)

Use this to verify if the message was sent successfully.

### Message Format Notes

  * Microsoft Teams only supports basic Markdown in webhook messages.
  * The image must be accessible from the machine running Teams. Ensure it's reachable via the network.



## Testing and Verification

  1. Click the button on the left side of the inject node
  2. Check the debug panel for any error messages
  3. Verify that the message was received at the destination address



## Drawing of connection to use Internet on your OV20i

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28229%29.png)

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

  * [ Sending Emails Using Node-RED ](/docs/sending-email-with-node-red) __



Table of contents

    * Overview 
    * Prerequisites 
    * Microsoft Teams Integration 
    * OV20i Node-Red 
    * Testing and Verification 
    * Drawing of connection to use Internet on your OV20i 



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
