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
chunk_id: 9eb038ea
chunk_index: 4
total_chunks: 18
chunk_title: Classification Block Logic
chunk_level: 4
chunk_start_line: 152
chunk_end_line: 184
chunked_at: '2025-07-01T17:23:34.019435'
chunking_method: header_based
---

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



