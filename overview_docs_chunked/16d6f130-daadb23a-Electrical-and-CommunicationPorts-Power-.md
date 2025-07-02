---
title: Electrical and CommunicationPorts Power I/O Connector Pinout and Wiring Note
  When active, output sin
category: Hardware Setup4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/electrical-and-communication
source_page: https://docs.overview.ai/docs/hardware-setup
parent_category: Hardware Setup4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:01.824665'
chunk_id: 16d6f130
chunk_index: 2
total_chunks: 8
chunk_title: Power I/O Connector Pinout and Wiring
chunk_level: 3
chunk_start_line: 73
chunk_end_line: 92
chunked_at: '2025-07-01T17:23:34.096940'
chunking_method: header_based
---

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

