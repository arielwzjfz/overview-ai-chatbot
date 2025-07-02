---
title: Ethernet/IP - Switching RecipesThis section outlines the process for changing
  the recipe in the came
category: PLC Communication5 Articlesin this category
language: English
url: https://docs.overview.ai/docs/plc-communication-ethernetip-recipe-switch
source_page: https://docs.overview.ai/docs/ethernet
parent_category: PLC Communication5 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:22.116905'
chunk_id: 601f3157
chunk_index: 9
total_chunks: 11
chunk_title: Recipe Switching and Error Handling
chunk_level: 2
chunk_start_line: 149
chunk_end_line: 264
chunked_at: '2025-07-01T17:23:34.312202'
chunking_method: header_based
---

## Recipe Switching and Error Handling

This section outlines the process of switching recipes in the camera system and monitoring the status to ensure successful integration with the PLC logic. Each signal and its corresponding action are explained to maintain proper functionality and error management.

  * #### RECIPE\_SWITCH \(BOOL\)

    * **Function** : Initiates the recipe switch process.

    * **Description** : This tag acts as a control signal from the PLC to start the recipe change sequence. When activated, it triggers the sequence that selects and applies a new recipe on the camera.

  * #### Recipe\_ONS

    * **Function** : Provides a one-shot signal to ensure the recipe switch request is processed only once.

    * **Description** : The Recipe\_ONS generates a single pulse when the RECIPE\_SWITCH signal transitions from low to high. This prevents multiple requests from being sent due to signal fluctuations or noise, ensuring that the recipe switch is processed correctly.

  * #### Camera\_1:I.Data\[1\].6 \(Busy\)

    * **Function** : Indicates that the camera is busy processing the recipe switch request.

    * **Description** : This bit is set high when the camera is actively processing the recipe switch. It ensures that no other operations are initiated until the recipe switch is complete. The system must wait for this bit to go low before starting any new process.

  * #### Camera\_1:O.Data\[0\].1 \(Recipe Switch Request\)

    * **Function** : Sends the recipe switch request to the camera.

    * **Description** : This output bit from the PLC initiates the recipe change on the camera. It must be set high to start the process and remain high until the camera acknowledges the switch request.

  * #### Camera\_1:I.Data\[0\].2 \(Recipe Switch Ack\)

    * **Function** : Acknowledges the recipe switch request from the camera.

    * **Description** : This bit turns high once the camera has received and is processing the recipe switch request. The PLC logic monitors this bit to confirm that the request has been accepted, after which the Recipe Switch Request bit can be unlatched.

  * #### Camera\_1:I.Data\[8\] & Camera\_1:O.Data\[4\] \(Current Recipe ID and Selected Recipe ID\)

    * **Function** : Compares the current recipe ID with the selected recipe ID.

    * **Description** : The system compares these two data points to ensure that the correct recipe is being applied. If the IDs match, the recipe change is confirmed as successful.

  * #### CONFIRM\_RECIPES\_MATCH \(BOOL\)

    * **Function** : Confirms that the current and selected recipes match.

    * **Description** : This tag is set when the comparison between the current and selected recipe IDs shows a match. It confirms that the camera is operating with the correct recipe, allowing the process to continue smoothly.

  * #### Camera\_1:I.Data\[1\].1 \(Recipe Switch Error\)

    * **Function** : Indicates an error condition during the recipe switch process.

    * **Description** : This bit turns high if an error occurs while switching recipes. It will remain latched until the error is addressed and cleared. Proper error-handling logic should be in place to manage this condition, including resetting the error bit and taking corrective actions.




This setup ensures that recipe switching in the camera system is performed accurately, with the PLC logic handling confirmations and errors to maintain smooth operations.

> **Summary of Key Signals**
> 
>   * **RECIPE\_SWITCH** : Initiates the recipe switch process.
> 
>   * **Camera\_1:I.Data\[1\].6** : Indicates that the camera is busy processing the recipe switch request. \(Busy\)
> 
>   * **Camera\_1:I.Data\[0\].2** : Acknowledgment of the recipe switch from the camera. \(Recipe Switch Ack\)
> 
>   * **Camera\_1:O.Data\[0\].1** : Sends the recipe switch request to the camera. \(Recipe Switch Request\)
> 
>   * **Camera\_1:O.Data\[1\].1** : Indicates an error during the recipe switch process, which remains latched until the error is cleared. \(Recipe Switch Error\)
> 
>   * **Camera\_1:I.Data\[8\]** & **Camera\_1:O.Data\[4\]** : Used to compare the current recipe ID with the selected recipe ID to confirm that the recipes match. \(Current Recipe ID and Selected Recipe ID\)
> 
>   * **CONFIRM\_RECIPES\_MATCH** : This tag is set when the current and selected recipes match, confirming the correct recipe is in use.
> 
> 


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
