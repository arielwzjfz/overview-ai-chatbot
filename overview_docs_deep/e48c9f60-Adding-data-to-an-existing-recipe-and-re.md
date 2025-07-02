---
title: "Adding data to an existing recipe and retrainingIf images that are not supposed to fail are failing, follow the steps below to add the images to the model and retrain. Connect to the camera (see Connecting to OV20i Software for help). Ensure the Recipe you want to retrain is Active . ..."
category: "Walkthroughs14 Articlesin this category"
language: "English"
url: "https://docs.overview.ai/docs/adding-data-to-an-existing-recipe-and-retraining"
source_page: "https://docs.overview.ai/docs/how-to-guides"
parent_category: "Walkthroughs14 Articlesin this category"
is_individual_article: True
scraped_at: "2025-06-30T17:20:06.172536"
---

[ ![OV20i](https://cdn.document360.io/logo/863daf20-40fe-49e9-9c91-e3c6cfba55d1/2e22ebf07a24460d8065cff0cb46d3d4-OverviewLogo.png) ](https://www.overview.ai)

  * [Knowledge Base Home](https://docs.overview.ai)
  * [User Manual](https://docs.overview.ai/docs)



  * [ __](/v1/en)
  * English

    * [ English ](/docs/en/adding-data-to-an-existing-recipe-and-retraining "en")
    * [ Spanish \(Mexico\) ](/docs/es-mx/adding-data-to-an-existing-recipe-and-retraining "es-mx")
    * [ Chinese \(Simplified, People's Republic of China\) ](/docs/zh-cn/adding-data-to-an-existing-recipe-and-retraining "zh-cn")




__Ask Eddy AI

Contents x

  * [ OV20i  ](start-here)
  * [ OV80i  ](start-here-1)
  * [ OV20i \(2.0\)  ](faq)



Adding data to an existing recipe and retraining

  *  __21 Oct 2024



  *  __ Print

  *  __ PDF




 __Contents

# Adding data to an existing recipe and retraining

  *  __Updated on 21 Oct 2024



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

If images that are not supposed to fail are failing, follow the steps below to add the images to the model and retrain.

  1. Connect to the camera \(see [Connecting to OV20i Software](https://overview.ai/docs/electrical-and-communication#connecting-to-the-ov20i-software) for help\).

  2. Ensure the Recipe you want to retrain is **Active**.

  3. Navigate to the **Library**. Use the filters and click **Search** find the images you want to use to retrain the model.

> **Tip**
> 
> Use the **Filter by Recipe** field to select the **Recipe** the images were captured with and **Filter by Pass / Fail** field to select **FAIL** to only view the failed images. You can further organize the images by using the **Sort By** option. Click **Search** to view the results.

![converting-fail-to-pass-image-cabfshy7](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/converting-fail-to-pass-image-cabfshy7.png)

  4. Select each image you want to use to retrain the model. Then click **Add to the active recipe’s trainset** at the bottom of the screen. This will add the selected images to the active recipe's trainset, which will help improve the accuracy of your model. Once you have added the selected images to the trainset, you can continue to train your model and test it on new data to see if the accuracy has improved.

> **Warning**
> 
> It's important to only add images that are not supposed to fail to your trainset, as adding failed images can negatively impact the performance of your model.

![converting-fail-to-pass-image-579xrtu0](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/converting-fail-to-pass-image-579xrtu0.png)

  5. A success message in the top-right corner will confirm the selected images have been added to the trainset. Click **Go to recipe editor** to make any adjustments and train the model.

![converting-fail-to-pass-image-p2f0tzeh](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/converting-fail-to-pass-image-p2f0tzeh.png)

  6. From the **Recipe Editor** page, go to **Classification Block** / **Label And Train** \(depending on whether this is a Classification or Segmentation Recipe\) then click **View All ROIs**.

  7. Use the **Filter By Class** filter and select **Unlabeled** to filter the images. This will display all the images in the recipe that have not been labeled yet. Once you have the list of unlabeled images, select all the images that you added to the trainset in the earlier step. Once selected, click **Label Selected ROIs** in the bottom-left corner.

> **Warning**
> 
> Take care when using the bulk labeling tool to avoid accidentally mislabeling data. Click **Clear Selection** at the bottom of the page every time you re-label. If you fail to do so, the images might move over but remain selected, which can lead to incorrect re-labeling.

![converting-fail-to-pass-image-uu48b1e4](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/converting-fail-to-pass-image-uu48b1e4.png)

  8. A modal will appear where you can label the selected ROIs \(Regions of Interest\) in the images. Select the appropriate label for the selected ROIs from the drop-down menu and click **OK** to apply the label to all the selected ROIs in all the selected images. This will help you organize your data and train your model more effectively.

![converting-fail-to-pass-image-0lzknc13](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/converting-fail-to-pass-image-0lzknc13.png)

  9. Close the View All ROIs modal to return to the **Classification Block** / **Label And Train** page.

  10. Click **Train Classification Model** / **Train Segmentation Model** and retain the model. The model will learn from the labeled data and adjust its algorithms to improve the accuracy of its predictions. Once the training process is complete, you can test the accuracy of the model by feeding it new data and observing its predictions using the **Live Preview Mode** or **HMI** page. If the accuracy is not satisfactory, you can repeat the training process with additional data or adjust the model parameters to improve its performance.




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

  * [ Trigger using a PLC ](/docs/trigger-using-a-plc) __



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
