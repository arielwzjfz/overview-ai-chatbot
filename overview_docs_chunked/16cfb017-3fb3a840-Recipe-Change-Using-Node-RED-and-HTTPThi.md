---
title: Recipe Change Using Node-RED and HTTPThis guide shows you how to change recipes
  on your OV20 camera
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/recipe-change-http
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:33.332028'
chunk_id: 16cfb017
chunk_index: 8
total_chunks: 9
chunk_title: Complete Flow Example
chunk_level: 2
chunk_start_line: 171
chunked_at: '2025-07-01T17:23:34.003619'
chunking_method: header_based
---

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
