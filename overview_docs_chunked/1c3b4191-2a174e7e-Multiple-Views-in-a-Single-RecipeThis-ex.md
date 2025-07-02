---
title: Multiple Views in a Single RecipeThis example shows you how to set up a single
  recipe that can inspe
category: Walkthroughs10 Articlesin this category
language: English
url: https://docs.overview.ai/docs/multiple-views-one-recipe-1
source_page: https://docs.overview.ai/docs/clone-walkthroughs
parent_category: Walkthroughs10 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:56.066147'
chunk_id: 1c3b4191
chunk_index: 2
total_chunks: 5
chunk_title: Configure Node-RED Logic
chunk_level: 2
chunk_start_line: 142
chunk_end_line: 181
chunked_at: '2025-07-01T17:23:34.286170'
chunking_method: header_based
---

## Configure Node-RED Logic

  1. Navigate to the **IO Block** \(**Configure IO** from the Recipe Editor\) and select **Advanced Settings** to open your Node-RED flow. Create a source to tell the OV80i which side is currently being inspected. This can be robot position data, information from the PLC, or anything else you want to use. In the example below, we will simulate this using two **Inject nodes** , one that sends the string "A" and one that sends the string "B".

  2. Since the side data coming in might be momentary, but we want to check to see which side is active, we will store the state data using a **Flow variable** , which will persist until the next side information is received. Hook your data source up to a function block containing the following code:  

         
         flow.set('side',msg.payload);
         return msg;

  
![image\(86\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(86\).png)

  3. You can test to see if your side data is being properly stored by opening up the **context** data sidebar, sending a message, and then hitting **refresh** on the **Flow variable pane**. The flow data pane will only update when manually refreshed using the small **refresh** button.  
  
![image\(87\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(87\).png)  
  


  4. Once the side data is properly stored in the **Flow variable** , add a **switch node** connected to **All Block Outputs**. This will be the block that routes the message with the inspection data according to which side is active in the **Flow variable**. Configure it to look at the **Flow variable** and route the message to port 1 if A is active and 2 if B is active.  
  
![image\(88\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(88\).png)

> **Note**
> 
> For more complex recipes, repeat this process for as many different views as you want to inspect.

  5. Connect each output port of the **switch** to a **Classification Block Logic block** , and configure each one according to the rules you want to inspect for that side. The **switch node** will only route a message to one of the nodes at a time. The image below shows the configuration for the B-side port of the switch. Notice it doesn't reference any of the A ROIs, so the logic will ignore that side's results when the inspection is routed through this node.  
  
![image\(89\)](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(89\).png)  
  


  6. Finally, hook the **logic blocks** up to the **Inspection Pass/Fail block**. This allows the results to show up on the HMI, as well as be passed to any attached PLC or other flow component.  




