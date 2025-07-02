---
title: Ethernet/IP - IntegrationThe OV20i vision system supports real-time communication
  with EtherNet/IP-b
category: PLC Communication5 Articlesin this category
language: English
url: https://docs.overview.ai/docs/plc-communication-ethernetip-connections
source_page: https://docs.overview.ai/docs/ethernet
parent_category: PLC Communication5 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:21.420898'
chunk_id: 90aefb51
chunk_index: 12
total_chunks: 14
chunk_title: 'How it works:'
chunk_level: 3
chunk_start_line: 184
chunk_end_line: 270
chunked_at: '2025-07-01T17:23:34.407935'
chunking_method: header_based
---

### **How it works:**

  * Placed between All Blocks Output Data and Send Data to PLC in the Node-RED flow![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image-1746911020782.png)

  * Automatically populates a structured ROI region starting at **byte 16** in the input assembly

  * Supports up to 4 ROIs per inspection

  * Each ROI includes:

    * ROI ID

    * Pass/fail bit

    * Confidence score

    * Reserved bytes for future use




> ⚠️ Format Data for PLC Node works with Classification Recipes Only

**Byte**| **Bit 7**| **Bit 6**| **Bit 5**| **Bit 4**| **Bit 3**| **Bit 2**| **Bit 1**| **Bit 0**  
---|---|---|---|---|---|---|---|---  
| | | | | | | |   
**16**| | | | | | | |  Aligner Success  
**17 - 18**|  Aligner Confidence \(unsigned 16-bit integer\)  
**19 - 20**|  Aligner Angle \(signed 16-bit integer\)  
**21 - 23**|  Aligner: Reserved for Future Data  
**24**|  ROI 0 ID \(8-bit integer\)  
**25**| | | | | | | |  ROI 0 Pass  
**26 - 27**|  ROI 0 Confidence \(unsigned 16-bit integer\)  
**28 - 31**|  ROI 0: Reserved for Future Data  
**32**|  ROI 1 ID \(8-bit integer\)  
**33**| | | | | | | |  ROI 1 Pass  
**34 - 35**|  ROI 1 Confidence \(unsigned 16-bit integer\)  
**36 - 39**|  ROI 1: Reserved for Future Data  
**40**|  ROI 2 ID \(8-bit integer\)  
**41**| | | | | | | |  ROI 2 Pass  
**42 - 43**|  ROI 2 Confidence \(unsigned 16-bit integer\)  
**44 - 47**|  ROI 2: Reserved for Future Data  
**48**|  ROI 3 ID \(8-bit integer\)  
**49**| | | | | | | |  ROI 3 Pass  
**50 - 51**|  ROI 3 Confidence \(unsigned 16-bit integer\)  
**52 - 55**|  ROI 3: Reserved for Future Data  
  
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
