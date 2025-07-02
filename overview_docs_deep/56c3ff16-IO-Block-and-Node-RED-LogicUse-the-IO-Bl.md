---
title: "IO Block and Node-RED LogicUse the IO Block menu to define Pass/Fail rules for each captured image, and use a built-in Node-RED editor to customize digital IO functions, complex logic, and web-based dashboards and user interfaces. Configuring IO is typically one of the final..."
category: "Software Setup15 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/io-and-node-red-logic"
source_page: "https://docs.overview.ai/docs/software-setup"
parent_category: "Software Setup15 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:16.462351"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/io-and-node-red-logic "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/io-and-node-red-logic "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/io-and-node-red-logic "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



IO Block and Node-RED Logic

  *  __30 Dec 2024



  *  __ Print

  *  __ PDF




 __Contents

# IO Block and Node-RED Logic

  *  __Updated on 30 Dec 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

Use the IO Block menu to define Pass/Fail rules for each captured image, and use a built-in Node-RED editor to customize digital IO functions, complex logic, and web-based dashboards and user interfaces.

Configuring IO is typically one of the final steps in the process of building a Recipe.

## Node-RED

Node-RED is a low-code, browser-based environment for programming event-driven applications. On top of Node-RED, the OV20i contains Overview-specific nodes to make it easy to set up basic inspection logic without coding. These include the OV20i default flow and multiple custom nodes.

> **Note**
> 
> More information about the Node-RED platform can be found on their website - <https://nodered.org/.> To learn and explore the full functionality of Node-RED please refer to [their documentation, specifically the cookbook.](https://nodered.org/docs/)

### Overview-Specific Nodes

We will use a few important purple nodes to get data from the camera. Let’s go through them one by one.

#### **All Block Outputs**

Description: The "All Block Outputs" module is a crucial component within the unified pipeline system. It is responsible for outputting data after each camera capture. It collates and processes all AI block data, ensuring the output is comprehensive and detailed.

Functionality: This module outputs data as a JSON object. The data includes information from various AI processes such as inspection, alignment, classification, and segmentation. Each capture's output is meticulously structured to provide valuable insights into the inspection process.

Data Fields:

  * Inspection Data:

    * Inspection ID: A rolling 16-bit integer that increments for each inspection.

    * Inspection Time: An ISO 8601 formatted timestamp of the capture for each inspection.

    * Image URL: An HTTP URL to the captured image \(jpg\).

  * Alignment Data:

    * Success: Indicates whether the part was successfully aligned.

    * Center Location X: The x-coordinate of the aligned part's center.

    * Center Location Y: The y-coordinate of the aligned part's center.

    * Confidence: The confidence level of the alignment \(0-1\).

    * Matched Angle: The angle matched relative to the template.

  * Classification Data:

    * Predictions:

      * ROI ID: The ID of the predicted Region of Interest \(ROI\).

      * ROI Name: The name of the predicted ROI.

      * Confidence: The confidence level of the predicted class \(0-1\).

      * Predicted Class: The name of the predicted class.

  * Segmentation Data:

    * Confidence Score Threshold: The threshold used to process the segmentation model outputs \(0-1\).

    * Blobs:

      * Center X: The x-coordinate of the blob's center.

      * Center Y: The y-coordinate of the blob's center.

      * Pixel Count: The total pixel count \(area\) of the blob.

      * Major Axis Length: The length in pixels of the major axis.

      * Minor Axis Length: The length in pixels of the minor axis.

      * ROI ID: The ID of the predicted ROI.

      * ROI Name: The name of the predicted ROI.

      * Predicted Class: The name of the predicted class for the blob.

    * Classes:

      * Predicted Class: The class name.

      * Number of Blobs: The number of blobs in the class.

      * Pixel Count: The total pixel count \(area\) of all blobs in the class.




#### **Classification Block Logic**

Description: The "Classification Block Logic" node is designed to set and evaluate rules on classification block outputs. The output of this node is a boolean value \(true/false\), which depends on whether all rules pass or any rule passes.

Functionality: If no rules are set by default, the output will be true if all inspections return the "pass" class. If any class is not "pass," the output will be false. This node allows for customization through rule setting, enabling more specific criteria to be applied to the classification results.

Key Features:

  * Allows setting of specific rules on classification block outputs

  * Boolean output based on rule evaluation \(true/false\)

  * Default behavior ensures output is true if all inspections return "pass" and false if any do not

  * Configurable confidence threshold for more precise rule setting

  * No immediate connections to other components, allowing for flexible future integration




Usage Scenarios:

  * Ensuring consistent quality control by verifying that all inspection outputs meet the defined "pass" criteria

  * Customizable rule settings to adapt to various inspection requirements

  * Providing clear pass/fail output for automated decision-making processes




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




#### **Inspection Pass/Fail**

Description: The "Final Pass/Fail Output Node" is designed to set and store an inspection's final pass/fail state. This node ensures the inspection outcome is clearly defined, communicated, and archived as a boolean value.

Functionality: This node processes the results of an inspection and outputs a boolean value indicating the overall state:

  * True: Indicates that the inspection has passed.

  * False: Indicates that the inspection has failed.




This node outputs the pass/fail state and stores the result for future reference and analysis. This node simplifies the decision-making process in automated inspection systems by providing a clear and recorded pass/fail output. It also ensures that all results are archived for traceability and quality control purposes.

Key Features:

  * Sets and stores the final pass/fail state of an inspection

  * Outputs a boolean value: false for fail and true for pass

  * Ensures clear and unambiguous communication of inspection results

  * Archives inspection results for future reference and analysis

  * Enhances the efficiency of automated quality control processes

  * Integrates seamlessly with other nodes and components in the inspection system




Usage Scenarios:

  * Determining and storing the outcome of quality control inspections in manufacturing

  * Automating decision-making processes based on inspection results

  * Providing a straightforward pass/fail output for integration with downstream systems and processes

  * Ensuring traceability and quality control through archived inspection results




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




#### **Capture Metadata**

Description:The "Metadata Assignment Node" is designed to set the metadata associated with each capture. This metadata can include information such as a serial number, part number, or other relevant details. The assigned metadata will appear in the library alongside the captured data.

Functionality:This node allows for the addition of metadata to each capture. The metadata is structured as an object with string keys and values that can be strings or numbers. This ensures that each capture is accompanied by important contextual information, making it easier to identify and reference in the future.

Key Features:

  * Assign metadata to each capture

  * Metadata can include serial numbers, part numbers, or other relevant information

  * Structured as an object with string keys and string or number values

  * Ensures that captures in the library are accompanied by contextual information

  * Enhances traceability and identification of captured data




Usage Scenarios:

  * Adding serial numbers, part numbers, or other identifiers to captured images

  * Providing additional context and information for captures stored in the library

  * Facilitating easier identification and reference of captures during analysis and review

  * Integrating metadata with other nodes and components in the capture and storage system




#### **Output**

Description: The "Digital Output Node" is designed to control the output pins on the M12 connector of the OV20i. The node turns the pins on or off based on boolean values.

Functionality:

  * True: Turns the pin ON.

  * False: Turns the pin OFF.




Digital Output nodes are straightforward in operation and do not have editable properties, ensuring consistent and reliable performance.

Wiring Diagram:

![image\(53\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(53\).png)

Pin Configuration:

**Pin \#**| **Pigtail**| **Description**  
---|---|---  
10| Violet| Output 1  
11| Gray / Pink| Output 2  
  
Key Features:

  * Controls the output pins on the M12 connector of the OV20i

  * Boolean values determine the state of the pins \(ON/OFF\)

  * No editable properties, ensuring simplicity and reliability




Usage Scenarios:

  * Automating control processes by turning specific output pins on or off.

  * Integrating with other control systems for coordinated operations.

  * Providing a straightforward interface for digital output control on the OV20i




#### **Onboard Status LED**

Description: The "Onboard Status LED Node" is designed to control the onboard status LED located on top of the OV20i. This LED can display various colors, including Yellow, Orange, and Green.

Functionality:

  * True: Turns the LED ON.

  * False: Turns the LED OFF.




This node provides a simple interface for controlling the status LED, making it easy to indicate different statuses or states of the device.

LED Colors:

  * Yellow

  * Orange

  * Green




Key Features:

  * Controls the onboard status LED on the OV20i

  * Boolean values determine the state of the LED \(ON/OFF\)

  * Supports multiple LED colors: Yellow, Orange, and Green

  * Provides visual indication of device status




Usage Scenarios:

  * Indicating the operational status of the OV20i

  * Providing visual feedback for various system states or alerts

  * Enhancing user interface with clear and visible status indicators




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




### **Node-RED Basics**

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




### **Node-RED Dashboard**

Description: The Node-RED Dashboard provides a web-based interface for Node-RED, enabling users to create and display live data visualizations, control interfaces, and dashboards. This functionality is essential for real-time monitoring and interaction with Node-RED flows.

![image\(75\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(75\).png)

Functionality:

  * User Interface Creation:

    * It allows users to design custom dashboards with various UI components, such as charts, gauges, text, sliders, buttons, and more.

    * Components can be arranged and styled to create intuitive and functional interfaces.

  * Real-Time Data Visualization:

    * Displays real-time data from Node-RED flows, providing immediate insights into system performance and metrics.

    * Supports dynamic updates, ensuring that the dashboard reflects the latest data.

  * Control Interfaces:

    * Includes interactive elements like buttons and sliders to control flows and processes directly from the dashboard.

    * Enables users to send commands and adjust settings without needing to access the Node-RED editor.

  * Responsive Design:

    * Dashboards are accessible from any device with a web browser, including desktops, tablets, and smartphones.

    * Ensures that the dashboard layout adjusts appropriately to different screen sizes and orientations.




Key Components:

  * Layout Manager:

    * Provides a drag-and-drop interface for arranging UI components on the dashboard.

    * Allows users to create a structured and organized layout.

  * UI Nodes:

    * Various nodes are available to add functionality to the dashboard, including:

    * ui\_button: Adds buttons for triggering actions.

      *     * ui\_chart: Displays line, bar, and pie charts for visualizing data trends.

      *     * ui\_gauge: Shows gauge meters for monitoring values within a range.

      *     * ui\_text: Displays static or dynamic text values.

      *     * ui\_slider: Allows users to adjust values using a slider control.

      *   * Theme Customization:

    * Users can customize the dashboard's appearance, including colors, fonts, and styles, to match their preferences or corporate branding.




Steps to Create a Dashboard:

  * Add UI Nodes to Flows:

    * You can drag and drop UI nodes from the palette into your flows to define the data and controls you want to include in the dashboard.

  * Configure UI Nodes:

    * Configure the properties of each UI node, such as labels, ranges, and data sources.

  * Arrange Components:

    * Use the layout manager to arrange the UI components on the dashboard, creating a logical and user-friendly layout.

  * Deploy and Access Dashboard:

    * Deploy your flows and access the dashboard by navigating to the appropriate URL \(typically **http://\{hostname\}:1880/api/ui**\).




Usage Scenarios:

  * Control Interfaces:

Provide users with interactive controls to manage and adjust processes, such as turning devices on or off, setting thresholds, or adjusting configurations based on your camera’s output.

  * Data Visualization:

Create visual representations of data trends, helping users to analyze and interpret complex information quickly.

  * User Interaction:

Enable end-users to interact with the Node-RED application without technical knowledge of the underlying flows.




> **Note**
> 
> More in-depth explanations and examples can be found [here](https://www.influxdata.com/blog/node-red-dashboard-tutorial/).

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

###### What's Next

  * [ FTP ](/docs/ftp-server) __



Table of contents

    * Node-RED 



ENTER

ESC

 __

__

Eddy AI, facilitating knowledge discovery through conversational intelligence

Search Limit Exceeded. Please upgrade the plan.

Answer copied\!

__

__ __

No results found

Provide more context or information so that I can better understand and assist you
