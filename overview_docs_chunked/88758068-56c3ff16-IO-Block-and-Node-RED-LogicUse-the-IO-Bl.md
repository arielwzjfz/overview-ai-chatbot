---
title: IO Block and Node-RED LogicUse the IO Block menu to define Pass/Fail rules
  for each captured image,
category: Software Setup15 Articlesin this category
language: English
url: https://docs.overview.ai/docs/io-and-node-red-logic
source_page: https://docs.overview.ai/docs/software-setup
parent_category: Software Setup15 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:16.462351'
chunk_id: '88758068'
chunk_index: 5
total_chunks: 18
chunk_title: Format Data for PLC
chunk_level: 4
chunk_start_line: 184
chunk_end_line: 225
chunked_at: '2025-07-01T17:23:34.019473'
chunking_method: header_based
---

#### **Format Data for PLC**

Description: The "PLC Format Node" is designed to format block outputs to the default PLC format. This ensures compatibility with various PLC \(Programmable Logic Controller\) systems by adhering to their specific byte order requirements.

Functionality: This node formats data outputs from blocks, converting them into the appropriate byte order based on the target PLC system. The two main types of byte orders used are:

  * Little-endian: Typically used by Allen-Bradley PLCs

  * Big-endian: Typically used by Siemens PLCs




By properly formatting the data, the node ensures seamless integration and communication with the respective PLC systems, facilitating accurate and reliable data processing.

Key Features:

  * Formats block outputs to the default PLC format

  * Supports little-endian byte order for Allen-Bradley PLCs

  * Supports big-endian byte order for Siemens PLCs

  * Ensures compatibility and reliable data exchange with various PLC systems

  * Enhances the efficiency and accuracy of automated control processes.




Usage Scenarios:

  * Integrating data outputs from AI and automation systems with Allen-Bradley and Siemens PLCs

  * Ensuring proper byte order conversion for accurate data interpretation by PLCs

  * Streamlining communication between block outputs and PLCs in industrial automation setups



