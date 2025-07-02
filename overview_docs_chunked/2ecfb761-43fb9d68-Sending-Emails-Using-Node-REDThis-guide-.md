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
chunk_id: 2ecfb761
chunk_index: 8
total_chunks: 13
chunk_title: 2\\. Configure the Inject Node
chunk_level: 3
chunk_start_line: 135
chunk_end_line: 150
chunked_at: '2025-07-01T17:23:34.116638'
chunking_method: header_based
---

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
