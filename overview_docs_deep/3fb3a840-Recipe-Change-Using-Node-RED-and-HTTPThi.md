---
title: "Recipe Change Using Node-RED and HTTPThis guide shows you how to change recipes on your OV20 camera using HTTP requests in Node-RED. You'll create a flow that allows dynamic recipe switching through simple API calls. Overview The OV20 camera supports recipe changes via HTTP reque..."
category: "NODE-RED4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/recipe-change-http"
source_page: "https://docs.overview.ai/docs/node-red"
parent_category: "NODE-RED4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:33.332028"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/recipe-change-http "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/receta-cambio-http "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/tutorial-setup "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Recipe Change Using Node-RED and HTTP

  *  __19 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Recipe Change Using Node-RED and HTTP

  *  __Updated on 19 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This guide shows you how to change recipes on your OV20 camera using HTTP requests in Node-RED. You'll create a flow that allows dynamic recipe switching through simple API calls.

* * *

## Overview

The OV20 camera supports recipe changes via HTTP requests, allowing you to programmatically switch between different inspection configurations without manual intervention. This is particularly useful in production environments where different products require different inspection settings, we will be using Node-RED as the tool to activate it.

## Prerequisites

Before you begin, ensure you have:

  * OV20 camera powered and connected
  * Access to Node-RED advanced mode
  * At least two recipes created on your camera
  * Basic understanding of HTTP requests



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28182%29.png)

## Building the Node-RED Flow

### 1\. Create the Base Flow

  1. Open your Node-RED interface
  2. Add an inject node to your workspace
  3. Add a function node to your workspace
  4. Add an HTTP request node
  5. Connect the nodes as shown below



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28183%29.png)

### 2\. Configure the nodes

For the http request to work there needs to me a message object sent to the recipe Endpoint, the configuration of that endpoint, so in the flow we will need to configure the 3 nodes.

  1. Configure the **\[inject\]** node
     * Double click on the inject node
     * **\[msg.payload\]** : `[#Unique recipe number]`
     * Save



I**mportant**

The unique recipe number is not the same as the PLC recipe number. The recipe number can be found at the top of the URL of an active recipe. It will change depending on the recipe, and there won't be two that are the same.  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28184%29.png)

  2. Configure the **\[function\]** node
     * Double click on the function node
     * Insert this logic into the node:


    
    
    let recipeID = msg.payload;
    
    msg.headers = {
        'Content-Type': 'application/json'
    };
    msg.payload = JSON.stringify({ id: recipeID }); 
    return msg;
    
    

  * Save



**Note**

The HTTP POST requires an array of data to be structured correctly. That’s why we use a function to format it properly. The message sent will include both msg.headers and msg.payload; if either is not set up correctly, it won’t work.

  3. Configure the **\[HTTP\]** node


  * Double click on the Http node
  * Setup the **\[method\]** as Post
  * Change the **\[URL\]** to localhost:5001/pipeline/activate



### 3\. Add Response Handling

  1. Add a debug node after the HTTP request node
  2. Configure it to display the complete message object
  3. Deploy your flow to test the connection



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28186%29.png)

## Testing and Verification

To verify your setup works correctly:

  1. Click the button on the inject node to trigger the HTTP request
  2. Check the debug panel for the response
  3. Verify that the camera has switched to the specified recipe



Expected result: If the node configuration is correct, the recipe will change to the one required. If there is any issue on the flow, there will be a response on the debug that shows "success: false".  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28187%29.png)

## Complete Flow Example

For reference, here's the complete flow JSON that you can import into node-RED:
    
    
    [
        {
            "id": "b5238f8d4507ccf4",
            "type": "function",
            "z": "6e6e08c3c76c7987",
            "name": "Set JSON Payload",
            "func": "let recipeID = msg.payload;\n\nmsg.headers = {\n    'Content-Type': 'application/json'\n};\nmsg.payload = JSON.stringify({ id: recipeID }); \nreturn msg;",
            "outputs": 1,
            "noerr": 0,
            "initialize": "",
            "finalize": "",
            "libs": [],
            "x": 350,
            "y": 300,
            "wires": [
                [
                    "8936e614d67306e3",
                    "aa98933f4f267615"
                ]
            ]
        },
        {
            "id": "e224efdee3be4a3e",
            "type": "debug",
            "z": "6e6e08c3c76c7987",
            "name": "Debug Response",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "true",
            "targetType": "full",
            "statusVal": "",
            "statusType": "auto",
            "x": 810,
            "y": 300,
            "wires": []
        },
        {
            "id": "8936e614d67306e3",
            "type": "debug",
            "z": "6e6e08c3c76c7987",
            "name": "Debug Response",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "payload",
            "targetType": "msg",
            "statusVal": "",
            "statusType": "auto",
            "x": 570,
            "y": 260,
            "wires": []
        },
        {
            "id": "4b0e8a7a6eafced8",
            "type": "inject",
            "z": "6e6e08c3c76c7987",
            "name": "Insert number",
            "props": [
                {
                    "p": "payload"
                }
            ],
            "repeat": "",
            "crontab": "",
            "once": false,
            "onceDelay": 0.1,
            "topic": "",
            "payload": "11",
            "payloadType": "str",
            "x": 150,
            "y": 300,
            "wires": [
                [
                    "b5238f8d4507ccf4"
                ]
            ]
        },
        {
            "id": "aa98933f4f267615",
            "type": "http request",
            "z": "6e6e08c3c76c7987",
            "name": "POST to Recipe Endpoint",
            "method": "POST",
            "ret": "txt",
            "paytoqs": "ignore",
            "url": "localhost:5001/pipeline/activate",
            "tls": "",
            "persist": false,
            "proxy": "",
            "insecureHTTPParser": false,
            "authType": "",
            "senderr": false,
            "headers": [],
            "x": 590,
            "y": 300,
            "wires": [
                [
                    "e224efdee3be4a3e"
                ]
            ]
        },
        {
            "id": "449e298c0b326a9a",
            "type": "comment",
            "z": "6e6e08c3c76c7987",
            "name": "Insert the number of recipe in inject",
            "info": "",
            "x": 180,
            "y": 240,
            "wires": []
        },
        {
            "id": "c66c7133edffb7ed",
            "type": "comment",
            "z": "6e6e08c3c76c7987",
            "name": "Sets message for HTTP",
            "info": "",
            "x": 340,
            "y": 340,
            "wires": []
        },
        {
            "id": "bd7fea04b31c534d",
            "type": "comment",
            "z": "6e6e08c3c76c7987",
            "name": "Message post on endpoint for recipe change",
            "info": "",
            "x": 650,
            "y": 340,
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

Table of contents

    * Overview 
    * Prerequisites 
    * Building the Node-RED Flow 
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
