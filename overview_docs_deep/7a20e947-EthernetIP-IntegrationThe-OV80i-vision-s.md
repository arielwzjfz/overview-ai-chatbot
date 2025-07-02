---
title: "Ethernet/IP IntegrationThe OV80i vision system supports real-time communication with EtherNet/IP-based PLCs. This guide explains how to configure cyclic I/O connections, map data structures, and use Overview’s Node-RED tools to access both global and ROI-level inspection ..."
category: "PLC Communication2 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/clone-ethernetip-integration-1"
source_page: "https://docs.overview.ai/docs/clone-plc-communication"
parent_category: "PLC Communication2 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:17.705654"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/clone-ethernetip-integration-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/clone-ethernetip-integration-2 "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/clone-ethernetip-integration-3 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Ethernet/IP Integration

  *  __16 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Ethernet/IP Integration

  *  __Updated on 16 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

The OV80i vision system supports real-time communication with EtherNet/IP-based PLCs. This guide explains how to configure cyclic I/O connections, map data structures, and use Overview’s Node-RED tools to access both global and ROI-level inspection results.

* * *

## **Overview**

The OV80i functions as an EtherNet/IP **adapter** , while your PLC operates as a **scanner** \(or master\). Once configured, the devices exchange structured data every cycle using a compact and predictable format.

### **Supported Features**

  * **Cyclic I/O communication -** 20–10,000 ms cycle time support

  * **Data throughput -** Up to 256 bytes in each direction

  * **Custom data handling -** Read/write Node-RED data as part of the active recipe




* * *

## **Network Setup**

  1. Assign a static IP address to the OV80i.

  2. Ensure both the OV80i and your PLC are on the same subnet.

  3. Make sure EtherNet/IP traffic is allowed on your network.

  4. Put the OV80i into Ethernet/IP Mode by selecting it on the Industrial Ethernet tab in the sidebar.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(232\).png)




* * *

## **PLC Configuration**

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/OV80i_EDS.zip)OV80i\_EDS

26.81 KB

  1. Download the OV80i EDS file and import it into your PLC development environment

  2. Add the OV80i as a new EtherNet/IP device using the EDS file.

  3. Set the **Input and Output Assembly instances** and **Requested Packet Interval \(RPI\)**.

  4. Map assembly data to appropriate tags in your PLC.

  5. Confirm data is being exchanged in real-time.




* * *

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
  
## **Timing and Handshake Behavior**

![250510_EtherNetIPTriggering_TimingDiagram.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/250510_EtherNetIPTriggering_TimingDiagram\(8\).png)

## **Custom Data Support**

The OV80i can accept or return additional custom data as part of your Node-RED flow.

### **PLC → OV80i**

  * Write external flags, thresholds, or counters to influence logic in Node-RED




### **OV80i → PLC**

  * Return calculated values, measurements, timestamps, or conditional outputs




Custom data fits into the extended portion of the assemblies, starting after the core signals and recipe info.

## **ROI Result Breakdown \(Classification Recipes Only\)**

For classification recipes, you can expose **per-ROI results** to the PLC using Overview’s custom Node-RED node: **Format data for PLC****.**

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

###### What's Next

  * [ Ethernet/IP - Triggering ](/docs/trigger-using-a-plc-ethernet-1) __



Table of contents

    * Overview 
    * Network Setup 
    * PLC Configuration 
    * Input Assembly \(OV80i → PLC\) 
    * Output Assembly \(PLC → OV80i\) 
    * Timing and Handshake Behavior 
    * Custom Data Support 
    * ROI Result Breakdown \(Classification Recipes Only\) 



ENTER

ESC

 __

__

Eddy AI, facilitating knowledge discovery through conversational intelligence

Search Limit Exceeded. Please upgrade the plan.

Answer copied\!

__

__ __

No results found

Provide more context or information so that I can better understand and assist you
