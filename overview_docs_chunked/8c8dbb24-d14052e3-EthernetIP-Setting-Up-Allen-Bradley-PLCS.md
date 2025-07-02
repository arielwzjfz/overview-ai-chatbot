---
title: Ethernet/IP - Setting Up Allen Bradley PLCSetting up OV20i in Rockwell Studio
  5000 Connections Aft
category: PLC Communication5 Articlesin this category
language: English
url: https://docs.overview.ai/docs/ethernetip-setting-up-rockwell-software
source_page: https://docs.overview.ai/docs/ethernet
parent_category: PLC Communication5 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:23.515675'
chunk_id: 8c8dbb24
chunk_index: 1
total_chunks: 3
chunk_title: Setting up OV20i in Rockwell Studio 5000 \\Connections\\
chunk_level: 2
chunk_start_line: 63
chunk_end_line: 192
chunked_at: '2025-07-01T17:23:34.279963'
chunking_method: header_based
---

## Setting up OV20i in Rockwell Studio 5000 \(Connections\)

After enabling Ethernet/IP functions within the OV20i software, you're prepared to incorporate module\(s\) for the OV20i into your PLC project and verify communication.

  1. Launch Studio 5000 and initiate the creation of a **New Project**.



  2. Select the controller model that matches your PLC, assign a name to your new project, and proceed by clicking **Next**.



  3. Studio 5000 will present software revision and security options, typically requiring no alterations for most users. When satisfied with the settings, click **Finish** to confirm and open your project.



  4. Go online with the PLC. If you are already online with the PLC, jump to Step 5.  


> **Warning**
> 
> Before downloading, make sure it is okay to do a download on the PLC as it will remove all the old existing programs from the PLC.

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/plc-communication-ethernetip-connections-image-5iby9jaf.png)



  5. A blank project window will appear. From the taskbar, navigate to **Tools** > **EDS Hardware Installation Tool** to register the previously downloaded EDS file.



  6. Select **Register a device description file\(s\)** and continue by clicking **Next**.



  7. Choose **Register a single device description file** , then locate the downloaded EDS file by browsing to its saved location. Select the OV20i.eds file and proceed by clicking **Next** to initiate installation.   


> **Note**
> 
> You can download the EDS File from the camera or from the file attached below. After downloading, extract the file.




[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/OV20i_EDS \(3\).zip)OV20i\_EDS \(3\)

28.06 KB

  6. The installation process will verify the file's validity, and the result will be displayed below. Click **Next** to proceed.



  7. The EDS file download includes an identifying icon, which will be integrated into your Studio 5000 project. Proceed by clicking **Next**.



  8. The device wizard will display the device to be added. Click **Next** , followed by **Finish** to conclude the EDS registration.



  9. With the EDS file registered, proceed to add an OV20i device module to your project. In the Controller Organizer window, located on the left-hand side, identify the Ethernet port corresponding to your PLC. Right-click on the port, then select **New Module…**.



  10. A prompt will appear, guiding you to select a module type. Filter the list by searching for "ov20i" in the search bar, locate the OV20i module type derived from the EDS file, and then ensure the **Close on Create** checkbox is selected before clicking **Create**.



  11. Another window will appear, requiring you to input essential details to define the module being added. Name the module and input the IP address of the camera \(the provided IP address serves as an example—ensure you input the appropriate IP address corresponding to your camera\). Once changes are made, click **OK**. \(Make sure they match the IP from the camera and that ethernet IP is set to active\).   
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/plc-communication-ethernetip-connections-image-grapnjq9.png)  
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/plc-communication-ethernetip-connections-image-ql26szx7.png)  


  12. Subsequently, you should see a new OV20i module in the Controller Organizer under the selected ethernet port.



  13. This module's addition generates PLC tags corresponding to various OV20i functions. Access the Controller Tags at the top of the Controller Organizer, and double-click to view and edit these tags.



  14. These controller tags facilitate information exchange between the PLC and the OV20i through Ethernet/IP communication. They are organized into arrays outlined in the Industrial Ethernet Menu on the OV20i. Input Assembly tags signify inputs the PLC receives from the OV20i, conveying hardware states, inspection results, and customized data \(e.g., individual ROI results, confidence levels, etc.\). Conversely, Output Assembly tags represent outputs sent from the PLC to the OV20i, such as trigger signals, recipe selection commands, and customized information \(e.g., job numbers, process states, etc.\).




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
