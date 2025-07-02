---
title: Send custom data from PLC to cameraCreate and Configure the Custom Data Tag
  Start by creating two ta
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/send-customdata-from-plc-to-camera
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:12.261962'
chunk_id: 58ec6d67
chunk_index: 0
total_chunks: 2
chunk_title: Send custom data from PLC to camera
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 168
chunked_at: '2025-07-01T17:23:34.054132'
chunking_method: header_based
---

# Send custom data from PLC to camera

  *  __Updated on 29 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

  1. **Create and Configure the Custom Data Tag**  
  
Start by creating two tags, one to copy data from the custom data tag and the other to move it on to the camera output tag. Both have to be a STRING data type.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(117\).png)

  2. **Define the Byte Order for Node-RED**  


You can choose any byte order from the output assembly assigned for Node-RED. The byte order refers to how the data is formatted and transmitted.   
  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/send-vin-from-plc-to-camera-image-hm2vdqk4.png)

  3. **Develop Trigger Logic**

  
After creating the custom data tag, use the trigger logic detailed in [Ethernet/IP - Triggering](/docs/trigger-using-a-plc-ethernet) to create a new set of logical instructions. The trigger logic should handle the camera's activation, ensuring that it captures an image whenever specific conditions are met.  


Download the .L5X file below:  


[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Send_Numeric_Data_Routine_RLL.L5X)Send\_Numeric\_Data\_Routine\_RLL

3.84 KB

  
![image\(116\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(116\).png)  


> **Note**
> 
> If you trigger the same VIN twice the data won’t be stored on the second image. Try to clear the data before sending the new one in.

  4. **Create a Flow in Node-RED**

  
Access the Node-RED flow and create a new flow that mirrors the required functionality.  
  
You can use the JSON file provided below to import and set up the logic within Node-RED, ensuring that the flow is configured according to the overall system requirements.  
  
![image\(127\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(127\).png)  


[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/PLC to Node Red Custom data.json)PLC to Node Red Custom data

5.30 KB

  


  5. **Capture the Image and Associate Metadata**

  
After triggering the camera, verify that the image capture process is working as expected.

  
Ensure that each image the camera takes has metadata, including the custom data.  


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/send-vin-from-plc-to-camera-image-ph141wpm.png)




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
