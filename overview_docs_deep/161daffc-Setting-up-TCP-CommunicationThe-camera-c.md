---
title: "Setting up TCP CommunicationThe camera can use Node-RED to communicate with other devices over TCP. Note The camera's IP address must be in the same range as the device it is communicating with. Navigate to the IO Block to configure the Node-RED logic. A commu..."
category: "Walkthroughs14 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/tcp-communication"
source_page: "https://docs.overview.ai/docs/how-to-guides"
parent_category: "Walkthroughs14 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:07.538708"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/tcp-communication "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/tcp-communication "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/tcp-communication "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Setting up TCP Communication

  *  __30 Jun 2025



  *  __ Print

  *  __ PDF




 __Contents

# Setting up TCP Communication

  *  __Updated on 30 Jun 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The camera can use Node-RED to communicate with other devices over TCP.

> **Note**
> 
> The camera's IP address must be in the same range as the device it is communicating with.

  1. Navigate to the **IO Block** to configure the Node-RED logic.

  2. A communication port \(**tcp in**\) must be opened, where we assign the port we want the camera to listen to.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(98\).png)  


  3. To send a response to the port, we need to place a **tcp out** node, assign the IP address of the device we are communicating with, and assign a free port.

Refer to the example below:  





## Node-RED Logic
    
    
    [
        {
            "id": "85237e29b8e86d05",
            "type": "tcp in",
            "z": "0fd07e9ea67b62bb",
            "name": "",
            "server": "server",
            "host": "",
            "port": "49155",
            "datamode": "stream",
            "datatype": "utf8",
            "newline": "",
            "topic": "",
            "trim": false,
            "base64": false,
            "tls": "",
            "x": 980,
            "y": 1000,
            "wires": [
                [
                    "8aac7b8d6e607f2c"
                ]
            ]
        },
        {
            "id": "f2652272e23aef9f",
            "type": "inject",
            "z": "0fd07e9ea67b62bb",
            "name": "Part 1",
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
            "x": 390,
            "y": 1000,
            "wires": [
                [
                    "a93161abf53cadef"
                ]
            ]
        },
        {
            "id": "8d1350846af1f18b",
            "type": "debug",
            "z": "0fd07e9ea67b62bb",
            "name": "debug 2",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "false",
            "statusVal": "",
            "statusType": "auto",
            "x": 720,
            "y": 1000,
            "wires": []
        },
        {
            "id": "a93161abf53cadef",
            "type": "function",
            "z": "0fd07e9ea67b62bb",
            "name": "function 1",
            "func": "msg.payload = \"....\";\nreturn msg;\n",
            "outputs": 1,
            "timeout": 0,
            "noerr": 0,
            "initialize": "",
            "finalize": "",
            "libs": [],
            "x": 540,
            "y": 1000,
            "wires": [
                [
                    "8d1350846af1f18b",
                    "6c867cbe2ea47239"
                ]
            ]
        },
        {
            "id": "6c867cbe2ea47239",
            "type": "tcp out",
            "z": "0fd07e9ea67b62bb",
            "name": "",
            "host": "192.168.0.100",
            "port": "49155",
            "beserver": "client",
            "base64": false,
            "end": false,
            "tls": "",
            "x": 770,
            "y": 1060,
            "wires": []
        },
        {
            "id": "8aac7b8d6e607f2c",
            "type": "debug",
            "z": "0fd07e9ea67b62bb",
            "name": "debug 6",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "false",
            "statusVal": "",
            "statusType": "auto",
            "x": 1160,
            "y": 1040,
            "wires": []
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

  * [ Change Recipe using PLC ](/docs/change-recipe-using-plc) __



Table of contents

    * Node-RED Logic 



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
