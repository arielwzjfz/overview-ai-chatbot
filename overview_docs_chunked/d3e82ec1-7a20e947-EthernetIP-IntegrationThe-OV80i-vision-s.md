---
title: Ethernet/IP IntegrationThe OV80i vision system supports real-time communication
  with EtherNet/IP-bas
category: PLC Communication2 Articlesin this category
language: English
url: https://docs.overview.ai/docs/clone-ethernetip-integration-1
source_page: https://docs.overview.ai/docs/clone-plc-communication
parent_category: PLC Communication2 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:17.705654'
chunk_id: d3e82ec1
chunk_index: 6
total_chunks: 14
chunk_title: Output Assembly \\PLC -> OV80i\\
chunk_level: 2
chunk_start_line: 142
chunk_end_line: 156
chunked_at: '2025-07-01T17:23:34.467308'
chunking_method: header_based
---

## **Output Assembly \(PLC → OV80i\)**

The output assembly contains control data sent from the PLC to the OV80i. You can use it to trigger inspections, change recipes, or pass in custom parameters.

**Byte**| **Bit 7**| **Bit 6**| **Bit 5**| **Bit 4**| **Bit 3**| **Bit 2**| **Bit 1**| **Bit 0**  
---|---|---|---|---|---|---|---|---  
| | | | | | | |   
**0**| | | | | | |  Recipe Switch Request| Trigger  
**1**| | | | | | | |   
**2**| | | | | | | |   
**3**| | | | | | | |   
**4 - 5**|  Recipe ID \(16-bit integer\)  
**6 - 256**|  Custom Data For NodeRED  
  