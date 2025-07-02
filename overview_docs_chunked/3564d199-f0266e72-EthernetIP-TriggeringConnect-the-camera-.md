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
chunk_id: 3564d199
chunk_index: 4
total_chunks: 7
chunk_title: Camera Triggering and Status Monitoring
chunk_level: 2
chunk_start_line: 118
chunk_end_line: 177
chunked_at: '2025-07-01T17:23:34.260590'
chunking_method: header_based
---

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



