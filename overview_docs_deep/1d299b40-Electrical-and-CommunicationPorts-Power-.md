---
title: "Electrical and CommunicationPorts Power I/O Connector Pinout and Wiring Important If wire color coding varies, refer to the labels for the correct pinout. Note When active, output sinks to GND. Max 200mA. When not active, output is floating. ..."
category: "Hardware Setup2 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/electrical-and-communication-1"
source_page: "https://docs.overview.ai/docs/hardware-setup-1"
parent_category: "Hardware Setup2 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:54.651956"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/electrical-and-communication-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/electrical-and-communication-1 "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/electrical-and-communication-1 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Electrical and Communication

  *  __16 Jun 2025



  *  __ Print

  *  __ PDF




 __Contents

# Electrical and Communication

  *  __Updated on 16 Jun 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

## Ports

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(139\).png)

Port Type| Description  
---|---  
USB Type A| Optionally used for Wifi dongle  
HDMI| Not used  
USB type C| Optionally used for ethernet dongle  
M12 A-Coded 12 Pin| Power I/O \(see [Power I/O Connector Pinout and Wiring](/v1/docs/electrical-and-communication-1#power-io-connector-pinout-and-wiring)\)  
M12 X-Coded Ethernet| Used for camera programming, network communication, and PLC communication  
Micro USB| Used for camera programming  
  
### Power I/O Connector Pinout and Wiring

> **Important**
> 
> If wire color coding varies, refer to the labels for the correct pinout.

> **Note**
> 
>   1. When active, output sinks to GND. Max 200mA. When not active, output is floating. Requires an external power supply.
> 
>   2. Pull to GND to activate input.
> 
>   3. Pull to GND to reboot the camera. This is not needed for most applications. Keep floating to avoid unexpected restarts.
> 
>   4. DIO GND \(Common In\) must be connected to GND for digital input functionality to work. DIO GND \(Common In\) is tied to GND through a thermal fuse. When connecting the OV80i’s digital I/O lines to a system that is powered from a different power supply, use this pin to tie the grounds together.
> 
> 


## Connecting to the OV80i Software

There’s no need to turn the camera on, when it’s powered it will automatically start. There are two ways to connect to the OV80i software. Once connected, refer to [Software Setup](/v1/docs/software-setup) to activate the product and start creating a recipe.

> **Mac Users**
> 
> If you’re you’re connecting using Google Chrome on a Mac, you may get an error - “This site can’t be reached” \(ERR\_ADDRESS\_UNREACHABLE\). You’ll need to go to **MAC OS System Settings** > **Privacy and Security**. Then scroll to find **Local Network**. Make sure it is enabled for Google Chrome.

### Connecting Directly via Ethernet

  1. Plug into the M12 ethernet port through an ethernet adapter.

  2. Configure your ethernet adapter’s IP address to **10.250.0.10**. In the Subnet Mask field, enter **255.255.255.0**.

> **Tip**
> 
> For help configuring your ethernet adapter’s IP address, refer to the links below:
> 
> [Windows - Change TCP/IP settings \(Microsoft Support\)](https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace)
> 
> [Mac - Change TCP/IP settings \(Apple Support\)](https://support.apple.com/guide/mac-help/change-tcpip-settings-on-mac-mh14129/mac)

  3. Open your browser and enter the IP address **10.250.0.100** to connect to the OV80i software.

> **Note**
> 
> This IP address is configurable and can be automatically assigned via DHCP or changed to suit your networking needs.




### Connecting via an Ethernet Network

To manually assign a static IP address to the OV80i device, follow these instructions:

  1. Connect to the OV80i software using one of the above methods.

  2. In the OV80i software, go to **Settings** > **System**.

  3. Click **Edit** to change the network settings of the OV80i.

  4. Scroll to the bottom of the page and click the **Static IP** option. Enter the appropriate IP address and Subnet Mask. You can also optionally set the Gateway and DNS. If you’re unsure of these settings, check with your network administrator to avoid conflicts with existing devices or other technical difficulties. Once you’ve entered the new network settings, click **Save**.

  5. After changes have been saved, you will see a message prompting you to restart the OV80i to apply the saved changes.

> **Important**
> 
> Take note of the Static IP address you have entered. If you mistyped the IP address information it can be difficult to find the device.

To restart the OV80i device, do one of the following:

     * Go to **System Settings** in the OV80i software, scroll down to **Power** ,**** and click **Reset**.

     * Press the physical **Reset** button on the top of the OV80i camera, near the indicator LEDs.

     * Unplug the camera, wait 5 seconds, then plug it back in.

  6. After the OV80i is restarted, you may use the newly assigned static IP address to access this device from any computer on the same network.




> 💡 **Keep in mind**
> 
> To prevent IP conflicts and ensure smooth connectivity for your camera, it's essential to configure a unique IP address for each device on your network.
> 
> To detect IP conflicts, use an IP scanner tool to identify any devices sharing the same IP address. If conflicts are found, adjust the IP address of one or more devices to ensure uniqueness and eliminate conflicts.

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

  * [ Multiple Views in a Single Recipe ](/docs/multiple-views-one-recipe-1) __



Table of contents

    * Ports 
    * Connecting to the OV80i Software 



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
