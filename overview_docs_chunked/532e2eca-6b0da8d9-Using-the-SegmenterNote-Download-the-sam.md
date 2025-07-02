---
title: Using the SegmenterNote Download the sample recipe here . From the All Recipes
  page, click + New Rec
category: Walkthroughs14 Articlesin this category
language: English
url: https://docs.overview.ai/docs/creating-a-segmenter
source_page: https://docs.overview.ai/docs/how-to-guides
parent_category: Walkthroughs14 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:04.710671'
chunk_id: 532e2eca
chunk_index: 0
total_chunks: 7
chunk_title: Using the Segmenter
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 154
chunked_at: '2025-07-01T17:23:34.075348'
chunking_method: header_based
---

# Using the Segmenter

  *  __Updated on 25 Nov 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

> **Note**
> 
> Download the sample recipe [here](https://drive.google.com/file/d/1gAqRFkDqkqVeuod_ksO8RooMuCPf1izP/view?usp=sharing).

  1. From the **All Recipes** page, click **\+ New Recipe** in the top-right corner.

![New Recipe button](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/New%20Recipe%20button.png)

  2. The **Add A New Recipe** modal will appear. Enter a **Name** for the Recipe \(required\) that reflects the specific application you are working on and select **Segmentation** from the **Recipe Type** down-down menu. Click **OK** to create the new Recipe.

![Add A New Recipe modal](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Add%20A%20New%20Recipe%20modal.png)

  3. The new Recipe will be listed on the **All Recipes** page \(Inactive\). Select **Actions > Activate** to the right-hand side of the Recipe. Then click **Activate** to confirm.

![All Recipes - Actions Activate](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/All%20Recipes%20-%20Actions%20Activate.png)

  4. Click **Edit** to initiate the process of creating your first Segmenter model. Then click **Open Editor** to confirm.

![Edit button](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Edit%20button.png)

  5. Click **Configure Imaging** at the lower left-hand side of the page to begin setting up your OV20i camera for this application.

![creating-a-segmenter-image-e3i245a3](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-e3i245a3.png)

  6. When setting up the camera, it's essential to take the time to configure all of the camera settings correctly. This includes focusing the camera on the region of interest, which is the specific area of the image that contains the object or feature you want to analyze. You can adjust the **Focus** using the slider or enter the value manually.

Another critical camera setting to get right is the **Exposure** , which controls how much light enters the camera. You can adjust the **Exposure** using the slider or enter the value manually.

Optimizing lighting conditions is also crucial for obtaining accurate and reliable results. You need to make sure that the lighting conditions are appropriate for the type of analysis you want to perform. For example, if you're analyzing a reflective surface, you may need to use the lighting to avoid glare or reflections. This can be selected under the **LED Light Pattern**. In addition to these camera settings, you can configure in-house designed lights for the camera and obtain various patterns to identify defects that may be visible under different reflective conditions.

Getting the **Gamma** just right is also important. **Gamma** is a measure of the contrast between the light and dark areas of an image. Adjusting the **Gamma** correctly can help you see more detail in the image and make it easier to identify defects or features of interest.

Once all of these settings are configured, simply hit **Save Imaging Settings** to apply them and start using the camera for your analysis.

![creating-a-segmenter-image-7xfwmdny](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-7xfwmdny.png)

  7. Next, navigate to **Template Image and Alignment**.

> **Navigation Tip**
> 
> Click on the Recipe Name in the breadcrumb menu to return to the Recipe Editor or use the drop-down menu to select **Template Image and Alignment**.
> 
> ![Segmeneter Recipe Editor Breadcrumb Menu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/Segmeneter%20Recipe%20Editor%20Breadcrumb%20Menu.png)

  8. Once you are on the **Template Image and Alignment** page, you can capture a template image and align the page to your desired condition. However, since you don't require this step for your current task, select **Skip Aligner**. Once you have made any necessary adjustments, simply click **Save** to apply the changes and move on to the next step.

![creating-a-segmenter-image-vurg9pet](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-vurg9pet.png)

  9. Next, navigate to **Inspection Setup**.

  10. For this particular case, the inspection will be focused on the sheet. However, you can select a different inspection type for your specific use case and adjust the inspection region accordingly.

Once you have selected the appropriate inspection type, you can adjust the Region of Interest \(ROI\) to ensure that the camera is focused on the correct area. This can be done by dragging the corners of the ROI box to adjust its size and position. It's crucial to ensure that the ROI is correctly aligned with the object you want to analyze to obtain the most accurate results.

Once you have adjusted the ROI, simply hit **Save** to apply the changes and continue with the inspection process.

![creating-a-segmenter-image-369jbtyk](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-369jbtyk.png)

  11. Next, navigate to **Label And Train**.

  12. Under**Inspection Types** , click**Edit** to rename the class as “Pencil Mark”. You can also change the color associated with the class.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(122\).png)

  13. Take a minimum of 10 images of the sheet with different pencil markings on it. Use the **Brush** tool to trace over the pencil marks in each image. Make sure to paint only the pencil marks and nothing else. Click **Save Annotations** and repeat.

![creating-a-segmenter-image-9t58musu](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-9t58musu.png)

  14. Once you have labeled at least 10 images, it's essential to double-check them to ensure that everything is correctly labeled. Once you've verified everything, click **Return to Live** and then **Train Segmentation Model**. Enter the **Number of Iterations** you want to be shown to the model. Keep in mind that the more **Iterations** you choose to show the model, the better the model's accuracy will be. However, more **Iterations** will take longer to train the model.

It's important to balance the need for accuracy with the amount of time you have available for training the model. Once you've selected the appropriate settings, hit the **Start Training** button to begin the training process. The system will start training the model, and you can monitor its progress and make any necessary adjustments as needed.

![creating-a-segmenter-image-d3t5mlho](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-d3t5mlho.png)

  15. After clicking on the **Start Training** button, a model training progress modal will be displayed. Here, you can see the current Iteration number and the accuracy value. If you need to stop the training for any reason, click the **Abort Training** button. If the training accuracy is already sufficient, you can finish the training early by clicking on the **Finish Training Early** button.

> **Note**
> 
> The training will finish automatically if the training accuracy is met.

Once the training is complete, you can check the training accuracy and evaluate the model's performance on the validation data. If you're satisfied with the results, you can save the model and use it for your analysis. If not, you can go back and adjust the settings as needed and retrain the model until you're satisfied with the performance.

![creating-a-segmenter-training](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-training.png)

  16. Once the training is completed, click **Live Preview** to view the live preview of the trained model highlighting the pencil marks. Congratulations\! You have trained your first segmentation model.

![creating-a-segmenter-image-q86qlteg](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/creating-a-segmenter-image-q86qlteg.png)



