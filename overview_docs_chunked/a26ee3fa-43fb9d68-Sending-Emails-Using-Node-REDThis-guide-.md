---
title: Sending Emails Using Node-REDThis guide walks you through configuring Node-RED
  to send automated ema
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/sending-email-with-node-red
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:31.897298'
chunk_id: a26ee3fa
chunk_index: 11
total_chunks: 13
chunk_title: Complete Flow Example
chunk_level: 2
chunk_start_line: 182
chunk_end_line: 277
chunked_at: '2025-07-01T17:23:34.116679'
chunking_method: header_based
---

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
