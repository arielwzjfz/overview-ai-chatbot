---
title: "Troubleshooting the camera connectionIf you’re having difficulty connecting to the camera, first ensure you’ve followed the steps in Connecting to the OV20i Software correctly and can’t use the USB-C port for communication. The camera is not connecting with the configured IP When c..."
category: "Walkthroughs14 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/communication-troubleshooting"
source_page: "https://docs.overview.ai/docs/how-to-guides"
parent_category: "Walkthroughs14 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:08.917545"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/communication-troubleshooting "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/communication-troubleshooting "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/communication-troubleshooting "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Troubleshooting the camera connection

  *  __29 Nov 2024



  *  __ Print

  *  __ PDF




 __Contents

# Troubleshooting the camera connection

  *  __Updated on 29 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

If you’re having difficulty connecting to the camera, first ensure you’ve followed the steps in [Connecting to the OV20i Software](https://docs.overview.ai/v1/docs/electrical-and-communication#connecting-to-the-ov20i-software) correctly and can’t use the USB-C port for communication.

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




## The camera is not connecting to Profinet/Ethernet IP

If all the TCP/IP settings are correct but you are still unable to ping or connect to the camera, the best way to connect would be through the micro USB port on the camera:

  1. Remove the rubber side flap on the OV20i to expose the auxiliary connections. Connect a micro USB cable from the camera \(see image\) to the computer you will use to connect to the OV20i.

  2. Open your browser and enter the IP address **192.168.55.1** to connect to the OV20i software.  


> **Note**
> 
> This IP address never changes and does not require configuration of your network adapter.




## The camera is still not connecting

There is a possibility that the camera’s IP is not unique.

To ensure effective communication between devices on a network, it's important to assign unique IP addresses to each device, including your camera. This is because sharing IP addresses can cause conflicts and disrupt connectivity. To avoid these conflicts, you can use an IP scanner tool to detect any shared IP addresses and adjust the IP settings of one or more devices. By assigning unique IP addresses to every device, you can optimize the performance of your camera and other networked devices and establish a seamless connection. This will help you get the most out of your camera and ensure your network operates smoothly.  


> 💡 **Keep in mind**
> 
> Your network might be utilizing the same IP as the camera, like **192.168.0.100** \(some routers have the same default IP\). This can cause a confusion as there is an IP conflict, so it is best to connect with a Micro USB and change the IP to unique IP setting.

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

  * [ Configure pass/fail logic for a classification recipe ](/docs/create-a-classifier-node-red-logic-2) __



Table of contents

    * The camera is not connecting with the configured IP 
    * The camera is not connecting to Profinet/Ethernet IP 
    * The camera is still not connecting 



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
