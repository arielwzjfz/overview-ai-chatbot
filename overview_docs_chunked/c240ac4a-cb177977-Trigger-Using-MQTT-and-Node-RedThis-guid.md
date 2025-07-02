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
chunk_id: c240ac4a
chunk_index: 4
total_chunks: 9
chunk_title: 1\\. Configure the MQTT Broker Connection
chunk_level: 3
chunk_start_line: 90
chunk_end_line: 111
chunked_at: '2025-07-01T17:23:34.492066'
chunking_method: header_based
---

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


