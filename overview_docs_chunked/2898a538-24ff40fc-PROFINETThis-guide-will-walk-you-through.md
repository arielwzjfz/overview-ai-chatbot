---
title: PROFINETThis guide will walk you through setting up PROFINET on your OV20i.
  Enabling PROFINET The fi
category: PLC Communication5 Articlesin this category
language: English
url: https://docs.overview.ai/docs/plc-communication-profinet
source_page: https://docs.overview.ai/docs/ethernet
parent_category: PLC Communication5 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:24.226867'
chunk_id: 2898a538
chunk_index: 1
total_chunks: 5
chunk_title: Enabling PROFINET
chunk_level: 2
chunk_start_line: 65
chunk_end_line: 92
chunked_at: '2025-07-01T17:23:34.043028'
chunking_method: header_based
---

## Enabling PROFINET

The first step will be to connect to the OV20i software and navigate to the **Industrial Ethernet** menu on the left-hand side. From this menu, complete the following steps:

  1. Select **PROFINET** protocol to enable communication with your PLC \(top left\).

> **Note**
> 
> The Industrial Ethernet menu allows you to enable PROFINET as a global setting for the OV20i. After PROFINET has been selected, you will still need to enable PLC Triggering and the Inspection Pass/Fail function in the Recipe Editor \(more details below\) for any recipes that will be controlled by your PLC.

  2. Note your OV20i’s network settings in the **Device Information** window. We recommend you set a Static IP for the device. For instructions on that process, see [Connecting via an Ethernet Network](https://docs.overview.ai/docs/electrical-and-communication#connecting-via-an-ethernet-network).

  3. Change the PROFINET Device Name to whatever you would like. Hit save. These should be unique if you have multiple OV20i’s communicating with the same PLC.

  4. Download the GSD file.

  5. To enable PLC Triggering for a given recipe, navigate to the **Recipe Editor** and then to the **Imaging Setup** menu. Under **Trigger Settings** , select **PLC Trigger** to allow the PLC to trigger the camera using the PROFINET output assembly bit.

> **Note**
> 
> Once PLC Trigger has been selected, the camera will no longer be able to trigger manually from the software or provide a live camera view—only the PLC Trigger will capture a new image. For this reason you may find it helpful to keep Manual Trigger enabled while getting the cameras mounted and working on the AI Blocks, and switch over to a PLC Trigger when you are ready to control captures via the PLC.

  6. The Inspection Pass function in the PROFINET input assembly will always be set to 0 for new recipes by default. You can use the[IO Block](/docs/io-and-node-red-logic)to define pass/fail conditions for a recipe, which will set the Inspection Pass bit to equal 1 for passing images and 0 for failing images. You can use the Classification Block Logic node in the IO Block to configure pass/fail conditions without writing any scripts—see Classification Block Logic Setup for details. You can also use the IO Block to send and receive custom data for more complex inspections.



