---
title: "Node-RED IntroductionThis document provides an introduction to Node-RED as implemented in the OV20i camera system, explaining key concepts and features that help you create powerful inspection workflows. What is Node-RED? Node-RED is a flow-based programming tool ..."
category: "OVERVIEW SOFTWARE4 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/node-red-introduction"
source_page: "https://docs.overview.ai/docs/overview-software"
parent_category: "OVERVIEW SOFTWARE4 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:21:21.925899"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/node-red-introduction "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/node-red-introduction "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/node-red-introduction "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Node-RED Introduction

  *  __13 May 2025



  *  __ Print

  *  __ PDF




 __Contents

# Node-RED Introduction

  *  __Updated on 13 May 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

This document provides an introduction to Node-RED as implemented in the OV20i camera system, explaining key concepts and features that help you create powerful inspection workflows.

* * *

## What is Node-RED?

Node-RED is a flow-based programming tool that provides a browser-based editor for visually connecting hardware devices, APIs, and online services. Originally developed by IBM, it has become an open-source project that offers a low-code approach to automation and data processing.

The OV20i camera leverages Node-RED as its automation platform, allowing you to create sophisticated inspection workflows with minimal coding knowledge. Through a simple drag-and-drop interface, you can quickly develop complex logic that would otherwise require extensive programming expertise.

## Key Concepts in Node-RED

#### Flows

Flows are the visual representations of your automated processes. Each flow consists of nodes connected by wires that represent how data moves through the system. The OV20i camera uses flows to process inspection results and communicate with external systems.

#### Nodes

Nodes are the building blocks of your flows, each representing a specific function or capability:

  * Input nodes - Receive data \(e.g., camera triggers, HTTP requests\)
  * Processing nodes - Transform or analyze data \(e.g., classification logic\)
  * Output nodes - Send data to external systems or trigger actions \(e.g., PLC communication\)



#### Messages

Nodes communicate by passing messages to each other. In the OV20i system, these messages often contain:

  * Inspection results
  * Metadata about inspected objects
  * Commands for external systems
  * Trigger signals



## Essential Node-RED Features

#### Context Storage

Node-RED provides a method for storing information that can be shared between different nodes without relying on messages that pass through a flow.

The 'scope' of a particular context value determines who can access it:

Scope Type| Visibility| Use Case  
---|---|---  
Node Context| Only visible to the node that set the value| Storing node-specific temporary state information  
Flow Context| Visible to all nodes on the same flow \(tab\)| Sharing data between nodes within the same flow  
Global Context| Visible to all nodes across all flows| Application-wide state or configuration  
  
**Benefits of Context Storage**

  * Data Persistence - Store data between message flows
  * Scope Flexibility - Different levels of data sharing
  * State Management - Maintain application state across nodes



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28202%29.png)

#### Deploy Button

The Deploy button in Node-RED allows you to apply and push configurations to the runtime environment.

  * Full Deploy - Updates all nodes and flows
  * Modified Nodes - Updates only the nodes that have been changed
  * Modified Flows - Updates only the flows containing modified nodes



![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28203%29.png)

#### Importing and Exporting

Node-RED allows you to export and import flow configurations as JSON files, enabling:

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28205%29.png)

  * Backup of your camera configurations
  * Sharing flows between team members
  * Moving configurations between different cameras



**Export Process**

  1. Open the camera's Node-RED Editor
  2. Select the flows you want to export
  3. Click the menu button and select "Export"  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28206%29.png)
  4. Choose the JSON format  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28207%29.png)



**Import Process**

  1. Open the camera's Node-RED Editor
  2. Click the menu button and select "Import"  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28209%29.png)
  3. Paste the JSON data or upload the JSON file
  4. Click "Import" to integrate the configuration
  5. Deploy to apply the new flows  
![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28210%29.png)



#### Debug

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28212%29.png)

**1\. Purpose and Functionality**  
The Debug node displays messages in the Node-RED editor's Debug sidebar, facilitating development and troubleshooting of inspection flows.

**2\. Key Features**

  * Structured message view in the Debug sidebar
  * Detailed information about message timing and source
  * Ability to locate source nodes in the workspace
  * Toggle capability for enabling/disabling debug output



#### Dashboard Capabilities

The Node-RED Dashboard provides a web-based interface for monitoring and controlling your camera system through a customizable UI.

![image.png](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image%28204%29.png)

**Key Components**

  * Layout Manager - Organize UI components
  * UI Nodes - Add specific interface elements
  * Theme Customization - Personalize appearance



**Common UI Elements**

  * Buttons - Trigger actions like recipe changes
  * Charts - Visualize inspection metrics over time
  * Gauges - Monitor values within a range
  * Text displays - Show current camera status
  * Sliders - Adjust parameters in real-time



**Steps to Create a Dashboard**

  1. Add UI Nodes to Flows  
Drag and drop UI nodes from the palette into your flows to define the data and controls you want to include in the dashboard
  2. Configure UI Nodes  
Configure the properties of each UI node, such as labels, ranges, and data sources
  3. Arrange Components  
Use the layout manager to arrange the UI components on the dashboard, creating a logical and user-friendly layout
  4. Deploy and Access Dashboard  
Deploy your flows and access the dashboard by navigating to the appropriate URL \(typically **\[http://\{hostname\}/ui\]**\)



## Working with Node-RED in the OV20i

#### Accessing the Editor

The Node-RED editor in your OV20i camera can be accessed through the UI in:

#### Default Flow

The OV20i comes with a pre-configured default flow that handles basic inspection operations. This serves as a starting point for your custom configurations and demonstrates best practices for camera integration.

#### OV20i Custom Nodes

The camera extends Node-RED with specialized nodes designed for vision applications:

  * Classification Logic - Process classification results
  * PLC Format - Format data for industrial controllers
  * Final Pass/Fail - Determine inspection outcomes



#### Integration Capabilities

The Node-RED environment in the OV20i supports integration with various industrial systems:

  * PLCs via Ethernet/IP, Profinet, or Modbus
  * MQTT for IoT applications
  * HTTP/REST for web services
  * Database systems for data logging
  * HMI interfaces for operator control



#### Best Practices

**Flow Organization**

  * Keep flows organized by function
  * Use comments to document complex logic
  * Name nodes clearly to indicate their purpose
  * Use subflows for repeated patterns



#### Performance Considerations

  * Minimize the number of debug nodes in production
  * Consider the impact of high-frequency triggers
  * Use context variables efficiently
  * Test thoroughly before deployment



#### Backup Strategy

  * Regularly export and save your flows
  * Document your configuration changes
  * Consider version control for team environments
  * Test restored flows before production use



**Information**

More information about the Node-RED platform can be found on their website - <https://nodered.org/>

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

  * [ Mouting Distance and Lens Selection ](/docs/lens-selection) __



Table of contents

    * What is Node-RED? 
    * Key Concepts in Node-RED 
    * Essential Node-RED Features 
    * Working with Node-RED in the OV20i 



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
