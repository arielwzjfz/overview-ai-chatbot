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
chunk_id: 5f516f5c
chunk_index: 9
total_chunks: 13
chunk_title: 3\\. Configure the Email Node
chunk_level: 3
chunk_start_line: 150
chunk_end_line: 170
chunked_at: '2025-07-01T17:23:34.116651'
chunking_method: header_based
---

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
