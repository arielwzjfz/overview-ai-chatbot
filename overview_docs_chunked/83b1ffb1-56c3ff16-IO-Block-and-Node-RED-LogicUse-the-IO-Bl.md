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
chunk_id: 83b1ffb1
chunk_index: 13
total_chunks: 18
chunk_title: Context Tab
chunk_level: 4
chunk_start_line: 509
chunk_end_line: 571
chunked_at: '2025-07-01T17:23:34.019775'
chunking_method: header_based
---

#### **Context Tab**

Description: Node-RED provides a method for storing information that can be shared between different nodes without relying on messages that pass through a flow.

Functionality: Context storage allows for the preservation and sharing of data across various nodes and flows within a Node-RED environment. This can be useful for maintaining state, sharing configuration data, or caching information.

Context Scopes: The 'scope' of a particular context value determines who can access it. There are three context scope levels:

  * Node Context:

    * Scope: Only visible to the node that set the value.

    * Use Case: This type of storage is ideal for storing data specific to a single node, such as temporary state information or local settings.

  * Flow Context:

    * Scope: Visible to all nodes on the same flow \(or tab in the editor\).

    * Use Case: This is useful for sharing data between nodes within the same flow, such as shared configuration data or intermediate results.

  * Global Context:

    * Scope: Visible to all nodes across all flows.

    * Use Case: Suitable for data that needs to be accessed by any node within the Node-RED instance, such as global configuration settings or application-wide state.




Key Features:

  * Node Context: Limited to the node that sets the value, ensuring encapsulated data handling.

  * Flow Context: Accessible by all nodes within the same flow, facilitating shared data usage.

  * Global Context: Available to all nodes, sharing data globally across the Node-RED instance.




Usage Scenarios:

  * Node Context: Storing temporary state information or local settings only relevant to a single node.

  * Flow Context: Sharing intermediate results or configuration data between nodes within the same flow.

  * Global Context: Maintaining global configuration settings or application-wide state information that needs to be accessible by any node.




Benefits:

  * Data Persistence: Allows data to be stored and accessed without passing through message flows.

  * Scope Flexibility: Provides different levels of data sharing, from node-specific to global access.

  * State Management: Facilitates the management of state and configuration data across nodes and flows.



