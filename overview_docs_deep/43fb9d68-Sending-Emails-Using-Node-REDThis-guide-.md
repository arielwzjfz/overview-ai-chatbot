---
title: "Sending Emails Using Node-REDThis guide walks you through configuring Node-RED to send automated emails. By the end, you'll be able to trigger email notifications from your OV20i camera or other systems. Overview Node-RED's email capabilities allow you to send automated n..."
category: "NODE-RED4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/sending-email-with-node-red"
source_page: "https://docs.overview.ai/docs/node-red"
parent_category: "NODE-RED4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:31.897298"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/sending-email-with-node-red "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/sending-email-with-node-red "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/sending-email-with-node-red "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Sending Emails Using Node-RED

  *  __15 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Sending Emails Using Node-RED

  *  __Updated on 15 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This guide walks you through configuring Node-RED to send automated emails. By the end, you'll be able to trigger email notifications from your OV20i camera or other systems.

* * *

## Overview

Node-RED's email capabilities allow you to send automated notifications, alerts, and reports from your industrial systems. By connecting email functionality to your OV20i camera, you can receive notifications about detection results, system status, or errors without constant monitoring.

**Important**

Version 1.0 of this document currently supports Gmail only. We are working on providing the steps for Microsoft Outlook integration.

## Prerequisites

Before you begin, ensure you have:

  * Node-RED installed and running
  * A Gmail account to use as the sender
  * App password generated for your Gmail account \(standard passwords won't work\)
  * Basic understanding of Node-RED flows



**Important**

For security reasons, Google requires using app passwords instead of your regular account password. This is a one-time setup process.

**Download**

You may need to download the "node-red-node-email" template from Node-RED if the email nodes are not already installed on the camera.

## Creating a Gmail App Password

### 1\. Enable 2-Step Verification

  1. Sign in to your Google Account
  2. Go to your Google Account settings
  3. Select Security from the left menu
  4. Under "Signing in to Google," select 2-Step Verification
  5. Follow the prompts to turn on 2-Step Verification



### 2\. Generate an App Password

  1. After enabling 2-Step Verification, go back to the Security page
  2. Select App passwords \(under "Signing in to Google"\)
  3. Select Mail as the app and Other as the device
  4. Enter a name \(e.g., "Node-RED Email"\)
  5. Click Generate
  6. Google will display a 16-character app password
  7. Copy this password and store it securely – you'll need it for Node-RED



**Note**

This 16-character password will only be shown once. If you lose it, you'll need to generate a new one.

## Setting Up the Email Flow

### 1\. Create the Basic Flow

  1. Open your Node-RED editor in a web browser
  2. Drag an inject node from the palette to your workspace
  3. Drag an email node from the output section of the palette
  4. Connect the inject node to the email node



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28200%29.png)

### 2\. Configure the Inject Node

  1. Double-click the inject node to open its properties
  2. Set a meaningful name \(e.g., "Email Trigger"\)
  3. Configure the payload to contain your email content:
     * Set Payload type to "string"
     * Enter your email body text
  4. Configure the topic to be your email subject:
     * Add a property named "topic"
     * Set its value to your desired email subject



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28198%29.png)

### 3\. Configure the Email Node

  1. Double-click the email node to open its properties
  2. Enter the following settings:
     * Name: Descriptive name for the node
     * To: Recipient email address
     * Server: smtp.gmail.com
     * Port: 465
     * Check Use secure connection
     * Auth type: Basic
     * Userid: Your full Gmail address
     * Password: The 16-character app password you generated earlier
  3. Check **"Check server certificate is valid"**
  4. Click **"Done"** to save the configuration
  5. Deploy your flow by clicking the Deploy button



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28199%29.png)

## Testing and Verification

  1. Click the button on the left side of the inject node
  2. Check the debug panel for any error messages
  3. Verify that the email was received at the destination address



**Note**

If you don't see the email immediately, check your spam folder as automated emails may sometimes be filtered.

## Complete Flow Example

For reference, here's the complete flow JSON that you can import into node-RED:
    
    
    [
        {
            "id": "ef9235fbfbe42254",
            "type": "e-mail",
            "z": "0931aa6716e829f0",
            "server": "smtp.gmail.com",
            "port": "465",
            "authtype": "BASIC",
            "saslformat": true,
            "token": "oauth2Response.access_token",
            "secure": true,
            "tls": true,
            "name": "",
            "dname": "Test Email",
            "x": 870,
            "y": 140,
            "wires": []
        },
        {
            "id": "e3439dddd299c8d7",
            "type": "inject",
            "z": "0931aa6716e829f0",
            "name": "",
            "props": [
                {
                    "p": "payload"
                },
                {
                    "p": "topic",
                    "vt": "str"
                }
            ],
            "repeat": "",
            "crontab": "",
            "once": false,
            "onceDelay": 0.1,
            "topic": "Email testing. ",
            "payload": "Hey, im a OV20i! ",
            "payloadType": "str",
            "x": 650,
            "y": 140,
            "wires": [
                [
                    "ef9235fbfbe42254"
                ]
            ]
        }
    ]
    
    

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

  * [ Trigger Using MQTT and Node-Red ](/docs/trigger-using-mqtt) __



Table of contents

    * Overview 
    * Prerequisites 
    * Creating a Gmail App Password 
    * Setting Up the Email Flow 
    * Testing and Verification 
    * Complete Flow Example 



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
