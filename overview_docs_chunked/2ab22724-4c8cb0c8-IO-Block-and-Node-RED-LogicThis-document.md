---
title: IO Block and Node-RED LogicThis document provides reference information about
  the custom nodes devel
category: OVERVIEW SOFTWARE4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/io-block-and-node-red-logic
source_page: https://docs.overview.ai/docs/overview-software
parent_category: OVERVIEW SOFTWARE4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:21.225134'
chunk_id: 2ab22724
chunk_index: 10
total_chunks: 14
chunk_title: Output Nodes
chunk_level: 3
chunk_start_line: 183
chunk_end_line: 215
chunked_at: '2025-07-01T17:23:34.087222'
chunking_method: header_based
---

### Output Nodes

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28213%29.png)

**1\. Purpose and Functionality**  
Output nodes control the digital outputs on the M12 connector of the OV20i, turning pins on or off based on boolean values to communicate with external systems.

**2\. Key Features**

  * Direct control of hardware output pins
  * Simple boolean operation \(true = ON, false = OFF\)
  * Integration with industrial equipment
  * Consistent performance with minimal configuration



**3\. Configuration Options**

Parameter| Description| Default  
---|---|---  
Output Pin| Which physical pin to control| DO0 - DO1  
Initial State| Starting state of the output| OFF  
Pin \#| Pigtail| Default  
---|---|---  
10| Violet| Output 1  
11| Gray / Pinkt| Output 2  
  
**Important**

There is no pulse configuration from the DO as itself, so you need to add a trigger to create a pulse.  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28211%29.png)
