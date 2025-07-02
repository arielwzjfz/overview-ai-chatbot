---
title: Setting up TCP CommunicationThe camera can use Node-RED to communicate with
  other devices over TCP.
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/tcp-communication
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:07.538708'
chunk_id: 4e7805d1
chunk_index: 1
total_chunks: 3
chunk_title: Node-RED Logic
chunk_level: 2
chunk_start_line: 85
chunk_end_line: 250
chunked_at: '2025-07-01T17:23:34.272587'
chunking_method: header_based
---

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
