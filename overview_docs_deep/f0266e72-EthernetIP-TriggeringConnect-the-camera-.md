---
title: "Ethernet/IP - TriggeringConnect the camera to the PLC of your choice by following this article. Camera Trigger Settings Make sure to set the PLC Trigger as a trigger on the camera side ( Imaging Setup > Photometric Control ). Timing Diagram The tim..."
category: "PLC Communication2 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/trigger-using-a-plc-ethernet-1"
source_page: "https://docs.overview.ai/docs/clone-plc-communication"
parent_category: "PLC Communication2 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:18.399297"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/trigger-using-a-plc-ethernet-1 "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/trigger-usando-plc "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/trigger-using-a-plc-ethernet-1 "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Ethernet/IP - Triggering

  *  __10 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Ethernet/IP - Triggering

  *  __Updated on 10 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

[](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Trigger_Camera_Routine_RLL.L5X)Trigger\_Camera\_Routine\_RLL

5.39 KB

Connect the camera to the PLC of your choice by following this article.

## Camera Trigger Settings

Make sure to set the **PLC Trigger** as a trigger on the camera side \(**Imaging Setup** > **Photometric Control**\).

  
![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(168\).png)

## Timing Diagram

The timing diagram visualizes the sequence of operations within the camera system. It shows the relationship between different signals—how one signal triggers another and how the process progresses through various stages, such as triggering, exposure, inspection, and completion. The transitions between high and low states on these signals represent the state changes in the camera's operation and help understand the timing and dependencies between each part of the process.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/250510_EtherNetIPTriggering_TimingDiagram\(8\).png)

### **Breakdown of the Timing Diagram**

  * **Busy** :  
The "Busy" signal indicates whether the system or camera is actively engaged in a process. The signal starts low \(inactive\), goes high \(active\) as the process begins, and stays high throughout the operation. Once all tasks are completed, the signal goes low again, indicating that the system is no longer busy and is ready for the next operation.

  * **Trigger** :

The "Trigger" signal is an input to the camera that initiates an image capture or inspection process. The signal goes high to activate the trigger and stays high for a short duration before going low again. This pulse indicates that a trigger command has been sent to the camera.

  * **TriggerReady \(Trigger Ready\)** :

This signal shows when the system is prepared to accept a trigger command. It starts high, indicating readiness, and then goes low once the trigger is issued. After the system processes the trigger and completes the necessary actions, the signal goes high again, indicating that the system is ready for the next trigger.

  * **TriggerAck \(Trigger Acknowledge\)** :

After the camera receives the trigger command, it sends a "Trigger Acknowledge" signal back to the PLC. This signal goes high to indicate that the trigger was successfully received and processed. It remains high for the duration of the processing and then returns low.

  * **ExposureComplete** :

This signal indicates that the camera has completed its exposure process. It follows the TriggerAck signal, going high after the acknowledgement and remaining high until the exposure is fully complete. At this point, it returns low.

  * **InspectionComplete** :

After the exposure process, the camera performs image processing or inspection. Once this inspection process is finished, the "Inspection Complete" signal goes high. This signal typically follows the ExposureComplete signal and stays high until the inspection is confirmed to be complete; at this point, it goes low.

  * **InspectionPass:**

This signal indicates whether the inspection was successful. It goes high once the inspection is complete and has passed all checks. If the inspection does not pass, this signal would remain low.




Program the logic using a similar example, PFA the logic attached

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(119\).png)

## Camera Triggering and Status Monitoring

This section explains how to trigger the camera and monitor its status using PLC logic. Each signal and its corresponding action are detailed to ensure proper integration and functionality.

  * **PB\_TRIGGER/OV\_Debug\[0\]**

    * **Function** : Acts as a control signal from the PLC logic to determine when to trigger the camera.

    * **Description** : This tag is essential for initiating the camera trigger process. It serves as an input that, when activated, starts the sequence of events leading to image capture.

  * **Trigger\_ONS**

    * **Function** : Provides a one-shot signal to ensure the trigger occurs only during the rising edge.

    * **Description** : The Trigger\_ONS generates a single pulse when the PB\_TRIGGER signal transitions from low to high. This prevents multiple triggers from occurring due to signal fluctuations or noise.

  * **Camer\_1:I.Data\[0\].0**

    * **Function** : Indicates that the camera is ready to be triggered.

    * **Description** : This bit, coming from the PLC, must be monitored to confirm that the camera is in a state ready to accept a trigger signal. The camera will not respond to trigger signals unless this bit is high.

  * **Camer\_1:O.Data\[0\].0**

    * **Function** : Sends the trigger signal to the camera.

    * **Description** : This output bit from the PLC must be set high to initiate image capture. It needs to be latched, meaning it remains high until the camera acknowledges receipt of the trigger. The acknowledgement is received via the Camer\_1:I.Data\[0\].1 signal, which then allows the trigger bit to be unlatched.

  * **Camer\_1:I.Data\[0\].1**

    * **Function** : Acknowledges the trigger from the camera.

    * **Description** : Once the camera has received the trigger signal, this bit will turn high. The PLC logic must monitor this bit to unlatch the Camer\_1:O.Data\[0\].0 trigger signal, completing the trigger sequence.

  * **Camer\_1:I.Data\[2\].1 :**

    * **Function** : Indicates that the result of the image processing is available.

    * **Description** : This bit turns high when the camera has processed the image and the result is ready to be read.

  * **Camer\_1:I.Data\[2.2\] :**

    * **Function** : Provides the pass/fail status of the image.

    * **Description** :

      * If this bit is high, it indicates a pass.

      * If this bit is low, it indicates a failure.

  * **Camer\_1:I.Data\[1\].0 :**

    * **Function** : Indicates an error condition.

    * **Description** : This bit turns high if there is an error with the camera. The error bit will latch and remain high until the error is cleared. Proper error-handling logic should be implemented in the PLC to reset this bit and handle the error condition accordingly.




### **Summary of Key Signals** :

  * **PB\_TRIGGER:** Initiates the camera trigger process.

  * **Trigger\_ONS** : Ensures a single trigger pulse.

  * **Camer\_1:I.Data\[0\].0** : Camera readiness indicator. \(trigger ready\)

  * **Camer\_1:O.Data\[0\].0** : Trigger signal must be latched until acknowledgement. \(Trigger\)

  * **Camer\_1:I.Data\[0\].1** : Acknowledgment of trigger from the camera. \(trigger Ack\)

  * **Camer\_1:I.Data\[2\].1** : Indicates result availability. \(Inspection Complete/Results Available\)

  * **Camer\_1:I.Data\[2\].2** : Pass/fail status indicator. \(Inspection Pass\)

  * **Camer\_1:I.Data\[1\].0** : Error indicator, latched until cleared. \(Acquisition/Trigger Error\)




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

###### What's Next

  * [ FAQ\! ](/docs/faq) __



Table of contents

    * Camera Trigger Settings 
    * Timing Diagram 
    * Camera Triggering and Status Monitoring 



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
