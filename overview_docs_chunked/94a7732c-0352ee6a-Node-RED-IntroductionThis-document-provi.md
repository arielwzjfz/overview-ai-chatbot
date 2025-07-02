---
title: Node-RED IntroductionThis document provides an introduction to Node-RED as
  implemented in the OV20i
category: OVERVIEW SOFTWARE4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/node-red-introduction
source_page: https://docs.overview.ai/docs/overview-software
parent_category: OVERVIEW SOFTWARE4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:21.925899'
chunk_id: 94a7732c
chunk_index: 11
total_chunks: 21
chunk_title: Dashboard Capabilities
chunk_level: 4
chunk_start_line: 187
chunk_end_line: 224
chunked_at: '2025-07-01T17:23:34.237281'
chunking_method: header_based
---

#### Dashboard Capabilities

The Node-RED Dashboard provides a web-based interface for monitoring and controlling your camera system through a customizable UI.

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28204%29.png)

**Key Components**

  * Layout Manager - Organize UI components
  * UI Nodes - Add specific interface elements
  * Theme Customization - Personalize appearance



**Common UI Elements**

  * Buttons - Trigger actions like recipe changes
  * Charts - Visualize inspection metrics over time
  * Gauges - Monitor values within a range
  * Text displays - Show current camera status
  * Sliders - Adjust parameters in real-time



**Steps to Create a Dashboard**

  1. Add UI Nodes to Flows  
Drag and drop UI nodes from the palette into your flows to define the data and controls you want to include in the dashboard
  2. Configure UI Nodes  
Configure the properties of each UI node, such as labels, ranges, and data sources
  3. Arrange Components  
Use the layout manager to arrange the UI components on the dashboard, creating a logical and user-friendly layout
  4. Deploy and Access Dashboard  
Deploy your flows and access the dashboard by navigating to the appropriate URL \(typically **\[http://\{hostname\}/ui\]**\)


