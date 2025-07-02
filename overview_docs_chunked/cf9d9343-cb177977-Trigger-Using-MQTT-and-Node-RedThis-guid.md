---
title: Trigger Using MQTT and Node-RedThis guide walks you through configuring and
  using MQTT communication
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/trigger-using-mqtt
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:32.642481'
chunk_id: cf9d9343
chunk_index: 7
total_chunks: 9
chunk_title: Complete Flow Example
chunk_level: 2
chunk_start_line: 160
chunk_end_line: 380
chunked_at: '2025-07-01T17:23:34.492117'
chunking_method: header_based
---

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
