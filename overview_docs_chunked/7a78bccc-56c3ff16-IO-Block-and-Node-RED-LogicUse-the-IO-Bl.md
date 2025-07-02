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
chunk_id: 7a78bccc
chunk_index: 7
total_chunks: 18
chunk_title: Save to Library
chunk_level: 4
chunk_start_line: 270
chunk_end_line: 313
chunked_at: '2025-07-01T17:23:34.019551'
chunking_method: header_based
---

#### **Save to Library**

Description: The "Capture Save Decision Node" determines whether a captured image should be saved to the library. This node outputs a boolean value to indicate the same decision.

Functionality: This node processes the capture data and outputs a boolean value indicating whether the capture should be saved:

  * True: Indicates that the capture should be saved to the library.

  * False: Indicates that the capture should not be saved.




By providing a clear save/no-save decision, this node helps manage storage resources efficiently and ensures that only relevant captures are archived for future use.

Key Features:

  * Determines whether a capture is saved to the library

  * Outputs a boolean value: false for do not save and true for save

  * Ensures efficient management of storage resources

  * Helps in archiving relevant captures for future reference and analysis

  * Integrates seamlessly with other nodes and components in the capture and storage system




Usage Scenarios:

  * Deciding whether to save captured images during automated inspections

  * Managing storage resources by only saving relevant captures

  * Providing a straightforward save/no-save output for integration with downstream systems and processes

  * Ensuring important captures are archived for traceability and quality control



