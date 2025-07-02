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
chunk_id: 26f36e2c
chunk_index: 15
total_chunks: 18
chunk_title: Importing and Exporting Node-RED
chunk_level: 4
chunk_start_line: 625
chunk_end_line: 710
chunked_at: '2025-07-01T17:23:34.019852'
chunking_method: header_based
---

#### Importing and Exporting Node-RED

Description: The Node-RED page allows users to export and import JSON flow configurations. This functionality enables the sharing, backup, and transferring of Node-RED projects across different environments or instances.

Functionality:

  * Exporting JSON:

    * Users can export their current flow configurations as a JSON file.

    * The exported JSON includes all nodes, configurations, and connections within the selected flows.

    * This JSON file can be saved locally or shared with others for collaboration or backup purposes.

  * Importing JSON:

    * Users can import JSON files containing flow configurations into their Node-RED instance.

    * The imported JSON is parsed and integrated into the existing Node-RED environment.

    * This allows for quick setup of predefined flows or restoration of previously saved configurations.




Steps for Exporting JSON:

  1. Open the camera’s Node-RED Editor.

  2. Select Flows: Choose the flows you want to export. This can be done by selecting specific nodes or entire tabs.

  3. Export Option: Click the menu button \(three horizontal lines\) in the top-right corner of the editor and select "Export".

     1.   4. Choose Format: In the export dialog, choose the JSON format and select whether to export the selected nodes or the entire flow.

  5. Copy/Download JSON: Copy the generated JSON to your clipboard or download it as a file.

![image\(62\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(62\).png)




Steps for Importing JSON:

  1. Open the camera’s Node-RED Editor.

  2. Import Option: Click the menu button \(three horizontal lines\) in the top-right corner of the editor and select "Import".

     1.   3. Paste JSON: Paste the JSON data into the import dialog or upload the JSON file.

![image\(64\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(64\).png)

  4. Import Flows: Click "Import" to integrate the JSON data into your Node-RED instance.

  5. Deploy: Click the "Deploy" button to apply the new flows once imported.




Key Features:

  * Data Portability: Easily transfer flow configurations between different Node-RED instances.

  * Collaboration: Share flow setups with team members or the wider community.

  * Backup: Create backups of your Node-RED configurations for safekeeping.

  * Quick Setup: Rapidly set up new environments using predefined JSON configurations.




Usage Scenarios:

  * Collaborative Development: Sharing flow configurations with colleagues for collaborative development and troubleshooting.

  * Migration: Moving Node-RED setups from one server or environment to another.

  * Backup and Restore: Creating backups of flow configurations to prevent data loss and enable easy restoration.

  * Template Sharing: Distributing common flow templates or best practices within the Node-RED community.



