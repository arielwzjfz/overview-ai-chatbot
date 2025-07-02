---
title: Ethernet/IP - TriggeringConnect the camera to the PLC of your choice by following
  this article. Came
category: PLC Communication2 Articlesin this category
language: English
url: https://docs.overview.ai/docs/trigger-using-a-plc-ethernet-1
source_page: https://docs.overview.ai/docs/clone-plc-communication
parent_category: PLC Communication2 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:18.399297'
chunk_id: a6f020c3
chunk_index: 3
total_chunks: 7
chunk_title: Breakdown of the Timing Diagram
chunk_level: 3
chunk_start_line: 82
chunk_end_line: 118
chunked_at: '2025-07-01T17:23:34.260574'
chunking_method: header_based
---

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
