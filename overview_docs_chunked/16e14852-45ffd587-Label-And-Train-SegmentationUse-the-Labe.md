---
title: Label And Train SegmentationUse the Label and Train page to train a deep-learning
  model to take an
category: Software Setup15 Articlesin this category
language: English
url: https://docs.overview.ai/docs/segmentation-block
source_page: https://docs.overview.ai/docs/software-setup
parent_category: Software Setup15 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:15.712136'
chunk_id: 16e14852
chunk_index: 7
total_chunks: 9
chunk_title: Annotation Tools
chunk_level: 2
chunk_start_line: 111
chunk_end_line: 186
chunked_at: '2025-07-01T17:23:34.174112'
chunking_method: header_based
---

## Annotation Tools

**Pan:** This lets you pan/move the image around.

**Brush** :**** This lets you draw on the image. You can use this to highlight the areas of the image that you want the model to learn to detect.

  * Use the **Brush Class** dropdown to select the class of the area you are going to be highlighting.

  * Pick a **Brush Size** that lets you precisely cover the part of the image that you want the model to learn to detect.




**Eraser:** The eraser lets you erase the annotations that have been drawn.

**AI:** Use AI to help annotate segmentation data much faster and intelligently. The AI annotation tool acts like a "magic wand", and will automatically annotate additional areas of the image that are visually similar to the selected patch. The tool can be used to both smartly label and unlabel areas of the image. By using this tool, annotating segmentation data is not only much faster to do but also more consistent and accurate. For more complex defects, it is useful as a first-pass to bulk annotate relevant areas before fine-grained annotation by hand.

**Show Annotations:** Toggling this off lets you see the image without the user drawings overlayed on them and toggling this on lets you see the image with the user drawings overlayed on them.

> **Important**
> 
> Drawing on the image is not sufficient to add the ROI to the training dataset. You have to explicitly check the checkbox present at the top left of the ROI to add it to your training dataset.

> **Segmentation Labelling Best Practices**
> 
>   * The segmenter model will roughly mirror the precision of how well you paint/label the training images. So, try to be as precise as possible when labelling them.
> 
>   * In your efforts to draw precisely, if you have to decide between slightly overdrawing and fully covering the defect or slightly underdrawing and leaving out a part of the defect, _choose to overdraw and fully cover the defect._
> 
>   * When annotating a segmenter training image, you are showing the model what to detect by drawing on it, but you are also showing the model what to ignore through all the parts of the image where you have not drawn. So, make sure to draw on all instances of the defects you are trying to detect in the image.
> 
>   * Adjust your imaging setup to make sure that each instance of the defects that you are trying to detect are at least 6 pixels in radius \(you can use the brush sizes for reference\) to give you the best odds at training a successful model. _You can get a production grade model even on defects that are less than 6 pixels in radius. This is just a good setup to aim for._
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
