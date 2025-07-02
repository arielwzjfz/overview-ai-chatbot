---
title: Troubleshooting the camera connectionIf you’re having difficulty connecting
  to the camera, first ens
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/communication-troubleshooting
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:08.917545'
chunk_id: 481ed291
chunk_index: 1
total_chunks: 5
chunk_title: The camera is not connecting with the configured IP
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 94
chunked_at: '2025-07-01T17:23:34.198249'
chunking_method: header_based
---

## The camera is not connecting with the configured IP

When connecting your computer to the camera, it's important to ensure both devices are on the same subnet. If your computer and camera have different subnet configurations, your computer may not be able to locate the camera, and the connection may fail. To avoid this issue, check your computer's ethernet adapter TCP/IP settings and ensure that they match the subnet configuration of the camera. If they don't match, you can change the settings to match the camera's subnet configuration. Once both devices are on the same subnet, you should be able to establish a proper connection and access the camera's software.  


> **Tip**
> 
> For help configuring your ethernet adapter’s IP address, refer to the links below:
> 
> [Windows - Change TCP/IP settings \(Microsoft Support\)](https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace)
> 
> [Mac - Change TCP/IP settings \(Apple Support\)](https://support.apple.com/guide/mac-help/change-tcpip-settings-on-mac-mh14129/mac)

  * IP addresses are formatted as **XXX.XXX.XXX.YYY**. It is usually defined by your IT department, where the **XXX.XXX.XXX** should be identical across all devices, and **YYY** is device-specific, so choose an IP for your computer that is not used by any other device on the line.

  * For example, if you want to create a subnet for all your cameras on the line, you can use the IP address range of **192.168.0.1** to **192.168.0.254**. This subnet can be identified by the subnet mask of **255.255.255.0**. Devices within this subnet will have IP addresses like **192.168.0.1** , **192.168.0.2** , and so on, and your laptop IP should be **192.168.0.YYY** \(where **YYY** is unique and not taken by any other device\).

  * Similarly, if you want to create a different subnet for your barcode readers, you can use the IP address range of **192.168.1.1** to **192.168.1.254**. This subnet can be identified by the subnet mask of **255.255.255.0**. Devices within this subnet will have IP addresses like **192.168.1.1** , **192.168.1.2** , and so on, and your laptop IP should be **192.168.1.YYY** \(where **YYY** is unique and not taken by any other device\).  
  
![image\(45\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(45\).png)  


> **Tip**
> 
> For more help on this subject, see [Allocating IP Addresses: 7 Best Practices for 2024](https://www.redswitches.com/blog/ip-address/#:~:text=Best%20practices%20for%20IP%20address,%2C%20Public%20IP%20addresses%2C%20etc.).



