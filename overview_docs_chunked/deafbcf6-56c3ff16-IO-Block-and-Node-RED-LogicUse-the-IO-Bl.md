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
chunk_id: deafbcf6
chunk_index: 16
total_chunks: 18
chunk_title: Node-RED Dashboard
chunk_level: 3
chunk_start_line: 710
chunk_end_line: 855
chunked_at: '2025-07-01T17:23:34.019895'
chunking_method: header_based
---

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
