---
title: Sending Messages to Microsoft Teams with Node-REDThis guide walks you through
  how to send inspection
category: NODE-RED4 Articlesin this category
language: English
url: https://docs.overview.ai/docs/sending-messages-to-microsoft-teams-with-node-red
source_page: https://docs.overview.ai/docs/node-red
parent_category: NODE-RED4 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:21:31.163749'
chunk_id: c7e3d0ab
chunk_index: 7
total_chunks: 14
chunk_title: 2\\. Function Node
chunk_level: 3
chunk_start_line: 113
chunk_end_line: 146
chunked_at: '2025-07-01T17:23:34.202479'
chunking_method: header_based
---

### 2\. Function Node

Use this function to format the message.
    
    
    msg.headers = {
        "Content-Type": "application/json"
    };
    
    msg.payload = {
        text: "You got a new message from your OV20i"
    };
    
    return msg;
    
    

You can also use msg.payload.image\_url if the image is coming dynamically from the inspection data, that way you can click on the link and open the image in a new window.
    
    
    let imageUrl = msg.payload.image_url;
    
    msg.headers = {
        "Content-Type": "application/json"
    };
    
    msg.payload = {
        text: `Inspection Image(${imageUrl})`
    };
    
    return msg;
    
