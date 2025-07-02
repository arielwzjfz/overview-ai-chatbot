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
chunk_id: 26160ca5
chunk_index: 5
total_chunks: 7
chunk_title: 'Summary of Key Signals :'
chunk_level: 3
chunk_start_line: 177
chunk_end_line: 239
chunked_at: '2025-07-01T17:23:34.260606'
chunking_method: header_based
---

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
