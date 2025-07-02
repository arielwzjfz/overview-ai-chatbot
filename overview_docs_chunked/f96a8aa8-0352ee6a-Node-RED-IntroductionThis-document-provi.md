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
chunk_id: f96a8aa8
chunk_index: 7
total_chunks: 21
chunk_title: Context Storage
chunk_level: 4
chunk_start_line: 102
chunk_end_line: 124
chunked_at: '2025-07-01T17:23:34.237225'
chunking_method: header_based
---

#### Context Storage

Node-RED provides a method for storing information that can be shared between different nodes without relying on messages that pass through a flow.

The 'scope' of a particular context value determines who can access it:

Scope Type| Visibility| Use Case  
---|---|---  
Node Context| Only visible to the node that set the value| Storing node-specific temporary state information  
Flow Context| Visible to all nodes on the same flow \(tab\)| Sharing data between nodes within the same flow  
Global Context| Visible to all nodes across all flows| Application-wide state or configuration  
  
**Benefits of Context Storage**

  * Data Persistence - Store data between message flows
  * Scope Flexibility - Different levels of data sharing
  * State Management - Maintain application state across nodes



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28202%29.png)
