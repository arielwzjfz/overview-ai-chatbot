---
title: "Electrical and CommunicationPorts Power I/O Connector Pinout and Wiring Note When active, output sinks to GND. Max 100mA. When not active, output is floating. Requires an external power supply. Pull to GND to activate input. Pull to GND to rebo..."
category: "Hardware Setup4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/electrical-and-communication"
source_page: "https://docs.overview.ai/docs/hardware-setup"
parent_category: "Hardware Setup4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:01.824665"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/electrical-and-communication "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/electrical-and-communication "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/electrical-and-communication "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Electrical and Communication

  *  __16 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Electrical and Communication

  *  __Updated on 16 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

## Ports

\#| Port Type| Description  
---|---|---  
1| HDMI| Not used  
2| USB type C| Optionally accessed through ethernet dongle  
3| M12 A-Coded 17 Pin| Power I/O \(see [Power I/O Connector Pinout and Wiring](/v1/docs/electrical-and-communication#power-io-connector-pinout-and-wiring)\)  
4| M12 X-Coded Ethernet| Used for camera programming, network communication, and PLC communication  
5| Micro USB| Used for camera programming  
  
### Power I/O Connector Pinout and Wiring

![Pinout and wiring diagram of the OV20i M12 17-Pin power connector](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/OV20i M12 17-Pin Wiring Diagram.png)

> **Note**
> 
>   1. When active, output sinks to GND. Max 100mA. When not active, output is floating. Requires an external power supply.
> 
>   2. Pull to GND to activate input.
> 
>   3. Pull to GND to reboot the camera. This is not needed for most applications. Keep floating to avoid unexpected restarts.
> 
>   4. DIO GND must be connected to GND for digital input functionality to work. DIO GND is tied to GND through a thermal fuse. When connecting the OV20i’s digital I/O lines to a system that is powered from a different power supply, use this pin to tie the grounds together.
> 
>   5. If there is insufficient power, modify the wiring to ensure that the 24V power supply is connected to both ports, rather than only connecting it to a single terminal. This adjustment is necessary to maintain consistent voltage across all required components.
> 
> 


## Connecting to the OV20i Software

There’s no need to turn the camera on, when it’s powered it will automatically start. There are three ways to connect to the OV20i software. Once connected, refer to [Software Setup](/v1/docs/software-setup) to activate the product and start creating a recipe.

> **Mac Users**
> 
> If you’re you’re connecting using Google Chrome on a Mac, you may get an error - “This site can’t be reached” \(ERR\_ADDRESS\_UNREACHABLE\). You’ll need to go to **MAC OS System Settings** > **Privacy and Security**. Then scroll to find **Local Network**. Make sure it is enabled for Google Chrome.

### Connecting Directly via USB

  1. Remove the rubber side flap on the OV20i to expose the auxiliary connections. Connect a micro USB cable from the camera \(see image\) to the computer you will use to connect to the OV20i.

  2. Open your browser and enter the IP address **192.168.55.1** to connect to the OV20i software.

> **Note**
> 
> This IP address never changes and does not require configuration of your network adapter.




### Connecting Directly via Ethernet

  1. Plug into the M12 ethernet port through an ethernet adapter.

  2. Configure your ethernet adapter’s IP address to **192.168.0.10**. In the Subnet Mask field, enter **255.255.255.0**.

> **Tip**
> 
> For help configuring your ethernet adapter’s IP address, refer to the links below:
> 
> [Windows - Change TCP/IP settings \(Microsoft Support\)](https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace)
> 
> [Mac - Change TCP/IP settings \(Apple Support\)](https://support.apple.com/guide/mac-help/change-tcpip-settings-on-mac-mh14129/mac)

  3. Open your browser and enter the IP address **192.168.0.100** to connect to the OV20i software.

> **Note**
> 
> This IP address is configurable and can be automatically assigned via DHCP or changed to suit your networking needs.




### Connecting via an Ethernet Network

To manually assign a static IP address to the OV20i device, follow these instructions:

  1. Connect to the OV20i software using one of the above methods.

  2. In the OV20i software, go to **Settings** > **System**.

  3. Click **Edit** to change the network settings of the OV20i.

  4. Scroll to the bottom of the page and click the **Static IP** option. Enter the appropriate IP address and Subnet Mask. You can also optionally set the Gateway and DNS. If you’re unsure of these settings, check with your network administrator to avoid conflicts with existing devices or other technical difficulties. Once you’ve entered the new network settings, click **Save**.

  5. After changes have been saved, you will see a message prompting you to restart the OV20i to apply the saved changes.

> **Important**
> 
> Take note of the Static IP address you have entered. If you mistyped the IP address information it can be difficult to find the device.

To restart the OV20i device, do one of the following:

     * Go to **System Settings** in the OV20i software, scroll down to **Power** ,**** and click **Reset**.

     * Press the physical **Reset** button on the top of the OV20i camera, near the indicator LEDs.

     * Unplug the camera, wait 5 seconds, then plug it back in.

  6. After the OV20i is restarted, you may use the newly assigned static IP address to access this device from any computer on the same network.




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

  * [ Using the Classifier ](/docs/creating-a-basic-single-roi-classifier-1) __



Table of contents

    * Ports 
    * Connecting to the OV20i Software 



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
