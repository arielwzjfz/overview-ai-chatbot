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
chunk_id: f5574cb0
chunk_index: 3
total_chunks: 18
chunk_title: All Block Outputs
chunk_level: 4
chunk_start_line: 79
chunk_end_line: 152
chunked_at: '2025-07-01T17:23:34.019395'
chunking_method: header_based
---

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



