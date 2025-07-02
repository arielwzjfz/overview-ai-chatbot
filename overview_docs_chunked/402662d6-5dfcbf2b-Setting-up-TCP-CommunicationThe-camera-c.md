---
title: Setting up TCP CommunicationThe camera can use Node-RED to communicate with
  other devices over TCP.
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/tcp-communication-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:57.476840'
chunk_id: 402662d6
chunk_index: 1
total_chunks: 3
chunk_title: Node-RED Logic
chunk_level: 2
chunk_start_line: 83
chunk_end_line: 248
chunked_at: '2025-07-01T17:23:34.304911'
chunking_method: header_based
---

## Node-RED Logic
    
    
    [
        {
            "id": "85237e29b8e86d05",
            "type": "tcp in",
            "z": "c0ed903576d54694",
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
            "x": 780,
            "y": 160,
            "wires": [
                [
                    "8aac7b8d6e607f2c"
                ]
            ]
        },
        {
            "id": "f2652272e23aef9f",
            "type": "inject",
            "z": "c0ed903576d54694",
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
            "x": 190,
            "y": 160,
            "wires": [
                [
                    "a93161abf53cadef"
                ]
            ]
        },
        {
            "id": "8d1350846af1f18b",
            "type": "debug",
            "z": "c0ed903576d54694",
            "name": "debug 2",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "false",
            "statusVal": "",
            "statusType": "auto",
            "x": 520,
            "y": 160,
            "wires": []
        },
        {
            "id": "a93161abf53cadef",
            "type": "function",
            "z": "c0ed903576d54694",
            "name": "function 1",
            "func": "msg.payload = \"....\";\nreturn msg;\n",
            "outputs": 1,
            "timeout": 0,
            "noerr": 0,
            "initialize": "",
            "finalize": "",
            "libs": [],
            "x": 340,
            "y": 160,
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
            "z": "c0ed903576d54694",
            "name": "",
            "host": "192.168.0.100",
            "port": "49255",
            "beserver": "client",
            "base64": false,
            "end": false,
            "tls": "",
            "x": 570,
            "y": 220,
            "wires": []
        },
        {
            "id": "8aac7b8d6e607f2c",
            "type": "debug",
            "z": "c0ed903576d54694",
            "name": "debug 6",
            "active": true,
            "tosidebar": true,
            "console": false,
            "tostatus": false,
            "complete": "false",
            "statusVal": "",
            "statusType": "auto",
            "x": 960,
            "y": 200,
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
