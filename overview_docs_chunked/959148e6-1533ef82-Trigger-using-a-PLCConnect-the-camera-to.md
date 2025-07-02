---
title: Trigger using a PLCConnect the camera to the PLC of your choice by following
  Ethernet/IP - Establish
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/trigger-using-a-plc
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:06.873200'
chunk_id: 959148e6
chunk_index: 0
total_chunks: 2
chunk_title: Trigger using a PLC
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 193
chunked_at: '2025-07-01T17:23:34.125399'
chunking_method: header_based
---

# Trigger using a PLC

  *  __Updated on 30 Dec 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

  1. Connect the camera to the PLC of your choice by following [Ethernet/IP - Establishing Communication](/docs/plc-communication-ethernetip-connections).




  
Program the logic using a similar example

** _Camera Triggering and Status Monitoring_**

This section explains the process of triggering the camera and monitoring its status using PLC logic. Each signal and its corresponding action are detailed to ensure proper integration and functionality.

  * PB\_TRIGGER

    * Function: Acts as a control signal from the PLC logic to determine when to trigger the camera.

    * Description: This tag is essential for initiating the camera trigger process. When activated, it serves as an input that starts the sequence of events leading to image capture.

  * Trigger\_ONS

    * Function: Provides a one-shot signal to ensure the trigger occurs only during the rising edge.

    * Description: The Trigger\_ONS generates a single pulse when the PB\_TRIGGER signal transitions from low to high. This prevents multiple triggers from occurring due to signal fluctuations or noise.

  * Camera\_1:I.Data\[0\].0

    * Function: Indicates that the camera is ready to be triggered.

    * Description: This bit, coming from the PLC, must be monitored to confirm that the camera is ready to accept a trigger signal. The camera will not respond to trigger signals unless this bit is high.

  * Camera\_1:O.Data\[0\].0

    * Function: Sends the trigger signal to the camera.

    * Description: This output bit from the PLC must be set high to initiate image capture. It must be latched, meaning it remains high until the camera acknowledges receipt of the trigger. The acknowledgment is received via the Camera\_1:I.Data\[0\].1 signal, which then allows the trigger bit to be unlatched.

  * Camera\_1:I.Data\[0\].1

    * Function: Acknowledges the trigger from the camera.

    * Description: Once the camera has received the trigger signal, this bit will turn high. The PLC logic must monitor this bit to unlatch the Camera\_1:O.Data\[0\].0 trigger signal, completing the trigger sequence.

_Result Availability and Status_

  * Camera\_1:I.Data\[2\].1 :

    * Function: Indicates that the result of the image processing is available.

    * Description: This bit turns high when the camera has processed the image and the result is ready to be read.

  * \- Camera\_1:I.Data\[2.2\] :

    * Function: Provides the pass/fail status of the image.

    * \- Description :

      * If this bit is high, it indicates a pass.

      * If this bit is low, it indicates a failure.

_Error Handling_

  * Camera\_1:I.Data\[1\].0 :

    * Function: Indicates an error condition.

  * Description: This bit turns high if there is an error with the camera. The error bit will latch and remain high until the error is cleared. Proper error-handling logic should be implemented in the PLC to reset this bit and handle the error condition accordingly.

Summary of Key Signals:

  * PB\_TRIGGER: Initiates the camera trigger process.

  * Trigger\_ONS: Ensures a single trigger pulse.

  * Camera\_1:I.Data\[0\].0: Camera readiness indicator.

  * Camera\_1:O.Data\[0\].0: Trigger signal, must be latched until acknowledgment.

  * Camera\_1:I.Data\[0\].1: Acknowledgment of trigger from the camera.

  * Camera\_1:I.Data\[2\].1: Indicates result availability.

  * Camera\_1:I.Data\[2\].2: Pass/fail status indicator.

  * Camera\_1:I.Data\[1\].0: Error indicator, latched until cleared.




By following these steps and monitoring the specified signals, the integration of the camera with the PLC logic can be effectively managed, ensuring reliable image capture and processing.

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
