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
chunk_id: 24957c37
chunk_index: 14
total_chunks: 18
chunk_title: Deploy Button
chunk_level: 4
chunk_start_line: 571
chunk_end_line: 625
chunked_at: '2025-07-01T17:23:34.019813'
chunking_method: header_based
---

#### **Deploy Button**

Description: The "Deploy Button" in Node-RED is a critical editor component, allowing users to manage, apply, and push configurations to their Node-RED instances. A running configuration consists of several Flow objects, each corresponding to a node in the editor. Additionally, a global Flow object manages global configuration nodes and subflow definitions.

Functionality:

  * Flow Object: Defined in red/runtime/nodes/flows/Flow.js, the Flow object is responsible for creating, starting, and stopping all the nodes it contains. When a Flow object is created, it receives its own configuration and a reference to the global Flow object, allowing access to global configurations and sub-flows.

  * Node Object: The basic Node object, defined in red/runtime/nodes/Node.js, is instantiated by the Flow object. For subflow instances, local instances of each node within the subflow are created.

  * Full Deploy: During a full deployment, the Flow object instantiates all the Node objects it owns. Conversely, all nodes are stopped and cleaned up when a flow is stopped.

Modified-Nodes/Flows Deploy: When deploying only modified nodes or flows, the start/stop functions utilize a different object to identify changes and update only the necessary components.




Flow Object Management:

  * The creation and management of Flow objects are handled by the runtime in red/runtime/nodes/flows/index.js.

  * The runtime processes the flow configuration provided via the admin API, converting the flat array of node objects into a structured format.

  * This structured object is then split and passed to individual Flow objects.

  * In the case of modified nodes/flows deployments, the runtime generates the diff between configurations to determine necessary updates.




Key Features:

  * Flow Management: Handles the creation, starting, and stopping of nodes within each Flow object.

  * Global Access: Each Flow object has access to global configurations and subflows through a reference to the global Flow object.

  * Efficient Deployment: Supports full and modified nodes/flows deployments, ensuring efficient updates and minimal disruption.

  * Runtime Integration: Managed by the runtime, providing seamless integration with the Node-RED admin API and configuration processes.




Usage Scenarios:

  * Flow Creation: Automatically handles the instantiation of nodes and subflow instances when a new flow is created.

  * Flow Updates: Efficiently updates only modified nodes or flows during deployment, reducing downtime and improving performance.

  * Global Configuration: Ensures that all flows have access to global configurations and subflows, promoting consistency and reuse.



