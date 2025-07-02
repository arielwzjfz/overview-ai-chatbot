---
title: "Trigger Using MQTT and Node-RedThis guide walks you through configuring and using MQTT communication to trigger your OV20i camera using Node-RED. By the end, you'll be able to remotely trigger image capture and processing through MQTT messages. Overview MQTT (Message Queuin..."
category: "NODE-RED4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/trigger-using-mqtt"
source_page: "https://docs.overview.ai/docs/node-red"
parent_category: "NODE-RED4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:32.642481"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/trigger-using-mqtt "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/trigger-using-mqtt "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/trigger-using-mqtt "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Trigger Using MQTT and Node-Red

  *  __15 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Trigger Using MQTT and Node-Red

  *  __Updated on 15 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This guide walks you through configuring and using MQTT communication to trigger your OV20i camera using Node-RED. By the end, you'll be able to remotely trigger image capture and processing through MQTT messages.

* * *

## Overview

MQTT \(Message Queuing Telemetry Transport\) is a lightweight messaging protocol ideal for IoT devices. Using MQTT with your OV20i camera enables remote triggering and communication with other systems in your network. This approach is particularly useful in production environments where you need to integrate the camera with other automated systems.

## Prerequisites

Before you begin, ensure you have:

  * OV20i camera connected to your network
  * Node-RED installed and configured
  * An MQTT broker set up \(You can set it up in Node-Red\)
  * Basic understanding of Node-RED flows
  * Camera configured with a working recipe
  * Trigger in the camera needs to be set up as Manual trigger in Image Setup.



**Note**

If you haven't set up MQTT communication yet, refer to the Setting Up MQTT Communication guide first.

## Setting Up the MQTT Trigger Flow

### 1\. Configure the MQTT Broker Connection

  1. Open your Node-RED editor in your browser
  2. Drag an MQTT-in node from the palette to your workspace
  3. Double-click the node to open its properties
  4. Click the pencil icon next to the Server field to add a new broker
  5. Configure the broker with these settings:


  * Name: Camera MQTT Broker
  * Server: Your broker's IP address \(e.g., 192.168.1.100\) or localhost
  * Port: 1883 \(default MQTT port\)
  * Client ID: Generate a unique ID \(You can leave it empty for autogenerate\)  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28193%29.png)  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28192%29.png)


  6. Click Add to save the broker configuration



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



## Testing and Verification

To verify your setup works correctly:

  1. Click the button on the inject node to trigger the MQTT request
  2. Check the debug panel
  3. Verify that the camera has taken a picture, a easy way to confirm it will be that there is a new message on debug from the AllBlocksOutput



## Complete Flow Example

For reference, here's the complete flow JSON that you can import into node-RED:
    
    
    [
        {
            "id": "80474d6fc128742d",
            "type": "mqtt out",
            "z": "6e6e08c3c76c7987",
            "name": "",
            "topic": "",
            "qos": "0",
            "retain": "",
            "respTopic": "",
            "contentType": "",
            "userProps": "",
            "correl": "",
            "expiry": "",
            "broker": "5628611a59df452b",
            "x": 850,
            "y": 860,
            "wires": []
        },
        {
            "id": "51e487a95039d080",
            "type": "change",
            "z": "6e6e08c3c76c7987",
            "name": "Set Payload 1",
            "rules": [
                {
                    "p": "topic",
                    "t": "set",
                    "pt": "msg",
                    "to": "stream_mode/set",
                    "tot": "str"
                },
                {
                    "p": "payload",
                    "t": "set",
                    "pt": "msg",
                    "to": "HMI_MODE",
                    "tot": "str"
                }
            ],
            "action": "",
            "property": "",
            "from": "",
            "to": "",
            "reg": false,
            "x": 680,
            "y": 860,
            "wires": [
                [
                    "80474d6fc128742d"
                ]
            ]
        },
        {
            "id": "a6d5a4132ed1f39d",
            "type": "change",
            "z": "6e6e08c3c76c7987",
            "name": "Set Payload 2",
            "rules": [
                {
                    "p": "topic",
                    "t": "set",
                    "pt": "msg",
                    "to": "hmi/10/capture_mode",
                    "tot": "str"
                },
                {
                    "p": "payload",
                    "t": "set",
                    "pt": "msg",
                    "to": "single",
                    "tot": "str"
                }
            ],
            "action": "",
            "property": "",
            "from": "",
            "to": "",
            "reg": false,
            "x": 680,
            "y": 900,
            "wires": [
                [
                    "80474d6fc128742d"
                ]
            ]
        },
        {
            "id": "25f5166b2886fcc7",
            "type": "delay",
            "z": "6e6e08c3c76c7987",
            "name": "",
            "pauseType": "delay",
            "timeout": "10",
            "timeoutUnits": "milliseconds",
            "rate": "1",
            "nbRateUnits": "1",
            "rateUnits": "second",
            "randomFirst": "1",
            "randomLast": "5",
            "randomUnits": "seconds",
            "drop": false,
            "allowrate": false,
            "outputs": 1,
            "x": 510,
            "y": 900,
            "wires": [
                [
                    "a6d5a4132ed1f39d"
                ]
            ]
        },
        {
            "id": "1435d7b97a321f86",
            "type": "inject",
            "z": "6e6e08c3c76c7987",
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
            "topic": "",
            "payload": "",
            "payloadType": "date",
            "x": 320,
            "y": 860,
            "wires": [
                [
                    "25f5166b2886fcc7",
                    "51e487a95039d080"
                ]
            ]
        },
        {
            "id": "5628611a59df452b",
            "type": "mqtt-broker",
            "name": "",
            "broker": "localhost",
            "port": "1883",
            "clientid": "",
            "autoConnect": true,
            "usetls": false,
            "protocolVersion": "4",
            "keepalive": "60",
            "cleansession": true,
            "birthTopic": "",
            "birthQos": "0",
            "birthRetain": "false",
            "birthPayload": "",
            "birthMsg": {},
            "closeTopic": "",
            "closeQos": "0",
            "closeRetain": "false",
            "closePayload": "",
            "closeMsg": {},
            "willTopic": "",
            "willQos": "0",
            "willRetain": "false",
            "willPayload": "",
            "willMsg": {},
            "userProps": "",
            "sessionExpiry": ""
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

  * [ Recipe Change Using Node-RED and HTTP ](/docs/recipe-change-http) __



Table of contents

    * Overview 
    * Prerequisites 
    * Setting Up the MQTT Trigger Flow 
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
