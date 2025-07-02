---
title: Template Image and AlignmentUse the Template Image and Alignment page to capture
  a Template Image as
category: Software Setup15 Articlesin this category
language: English
url: https://docs.overview.ai/docs/alignment-block
source_page: https://docs.overview.ai/docs/software-setup
parent_category: Software Setup15 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:14.333995'
chunk_id: cd80b5da
chunk_index: 7
total_chunks: 9
chunk_title: Alignment Best Practices
chunk_level: 2
chunk_start_line: 107
chunk_end_line: 184
chunked_at: '2025-07-01T17:23:34.385898'
chunking_method: header_based
---

## Alignment Best Practices

> **Alignment Best Practices**
> 
>   1. When placing Template Regions, focus on edges that are simple, unique, and consistently visible across all parts. Try to avoid edges that may be obscured by defects, or edge patterns that vary from part to part.
> 
>   2. Edges found inside a Template Region are highlighted green. Red highlights indicate that there are not enough edges found for valid alignment. You can increase sensitivity or add more Template Regions to increase the edge count \(below\).
> 
>   3. Use the Ignore Template Region tool to filter out edge noise from the Alignment. “Edge noise” includes any highlighted edges that do not represent a simple, unique, and consistently visible pattern. For example, a Template Region might inappropriately highlight textured surfaces, reflections, debris, or other features as edges in your Template Image.
> 
> 


![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(9\).png)

In this example, we are attempting to align to some of the white outlines printed on the circuit board, because they should be visible even if other components are broken or missing. In this case, the 1st Template Region does not have enough edges.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(11\).png)

Adding more Template Regions increases the number of edges for Alignment. In this case, a 2nd Template Region has been added over the circular feature in the lower left corner, but the highlights remain red because not enough edges are found.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(12\).png)

Increasing the sensitivity finds more edges in the existing Template Regions. It’s recommended to use the lowest Sensitivity setting that still finds adequate edges to avoid unwanted noise in the pattern.

![](https://cdn.document360.io/863daf20-40fe-49e9-9c91-e3c6cfba55d1/Images/Documentation/image\(13\).png)

**Left:** Before using the Ignore Template Regions tool, the edge finder highlights some shiny areas and resistor edges that are not _simple, unique, and consistently visible._**Right** : After applying the Ignore Template Regions tool, the unwanted noise is masked by the red regions so the aligner will only pay attention to the white printed line patterns.

> **Tips**
> 
>   1. If Alignment is inconsistent or fails when testing on different parts, your Template Regions may be set up on a pattern that is not simple enough, or not consistently visible across all parts. Try reducing the amount of edges, or choosing a different pattern to focus on for Alignment.
> 
>   2. If Alignment has frequent “false positives” where it matches to something other than the part you want to find, you may have chosen a pattern that is not unique enough. Try increasing the Confidence Threshold to screen out the false positives, or add Template Regions and/or Sensitivity to make your Alignment pattern more specific.
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
