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
chunk_id: fa6902b9
chunk_index: 5
total_chunks: 14
chunk_title: Input Assembly \\OV80i -> PLC\\
chunk_level: 2
chunk_start_line: 122
chunk_end_line: 142
chunked_at: '2025-07-01T17:23:34.467294'
chunking_method: header_based
---

## **Input Assembly \(OV80i → PLC\)**

The input assembly contains data sent from the OV80i to the PLC on every cycle. This includes system status, inspection results, recipe information, and optional ROI breakdowns.

**Byte**| **Bit 7**| **Bit 6**| **Bit 5**| **Bit 4**| **Bit 3**| **Bit 2**| **Bit 1**| **Bit 0**  
---|---|---|---|---|---|---|---|---  
| | | | | | | |   
**0**|  Online / Startup Complete| | | | | Recipe Switch Ack| Trigger Ack| Trigger Ready  
**1**| |  Busy| | | | | Recipe Switch Error| Trigger Error  
**2**| | | | | |  Inspection Pass| Inspection Completed / Result Available| Exposure Complete  
**3**| | | | | | | |   
**4**| | | | | | | |   
**5**| | | | | | | |   
**6 - 7**| | | | | | | |   
**8 - 9**|  Current Recipe ID \(16-bit integer\)  
**10 - 11**| | | | | | | |   
**12 - 13**|  Inspection ID \(16-bit integer\)  
**14 - 15**| | | | | | | |   
**16 - 256**|  ROI Results Assembly or Custom Data from NodeRED  
  