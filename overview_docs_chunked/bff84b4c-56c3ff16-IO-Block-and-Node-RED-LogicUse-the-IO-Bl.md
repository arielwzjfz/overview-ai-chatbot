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
chunk_id: bff84b4c
chunk_index: 11
total_chunks: 18
chunk_title: Debug Node
chunk_level: 4
chunk_start_line: 445
chunk_end_line: 507
chunked_at: '2025-07-01T17:23:34.019701'
chunking_method: header_based
---

#### **Debug Node**

Description: The "Debug Node" is an essential tool for displaying messages in the Debug sidebar within the editor. It provides a structured view of the messages it receives, making it easier to explore and analyze them.

Functionality:

  * Displays messages in the Debug sidebar.

  * Provides detailed information about each message, including the time it was received and the source Debug node.

  * Allows users to click on the source node ID to reveal the node within the workspace.

  * Includes a button on the node to enable or disable its output.

  * It can be configured to send all messages to the runtime log.

  * You can send short messages \(32 characters\) to the status text under the Debug node.




Key Features:

  * Structured Message View: The Debug sidebar organizes messages, making it easier to explore and analyze them.

  * Timestamp and Source Information: Each message includes the time it was received and the source Debug node.

  * Node Reveal: Clicking on the source node ID in the Debug sidebar reveals the node within the workspace.

  * Enable/Disable Output: A button on the node allows users to enable or disable its output.

  * Runtime Log: The node can be configured to send all messages to the runtime log for persistent logging.

  * Status Text: The node can send short messages \(32 characters\) to the status text under the Debug node for quick reference.




Usage Recommendations:

  * Disable or remove any Debug nodes that are not being used to reduce clutter and improve performance.

  * Use the Debug node to troubleshoot and analyze message flows during development and testing.




Usage Scenarios:

  * Monitoring and debugging message flows within the editor

  * Analyzing the structure and content of messages received by the node.

  * Quickly identifying and locating source nodes within the workspace for further inspection.

  * Sending important runtime information to the log for persistent monitoring.

  * Displaying short status updates directly under the Debug node for quick reference.



