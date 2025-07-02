---
title: 'Software Updates Release NotesFor new updates, follow this link: https://updates.overview.ai/
  On thi'
category: Software Setup15 Articlesin this category
language: English
url: https://docs.overview.ai/docs/software-updates-release-notes
source_page: https://docs.overview.ai/docs/software-setup
parent_category: Software Setup15 Articlesin this category
is_individual_article: true
scraped_at: '2025-06-30T17:20:18.521102'
chunk_id: 799f7a3a
chunk_index: 0
total_chunks: 2
chunk_title: Software Updates Release Notes
chunk_level: 1
chunk_start_line: 42
chunk_end_line: 322
chunked_at: '2025-07-01T17:23:34.282967'
chunking_method: header_based
---

# Software Updates Release Notes

  *  __Updated on 07 Feb 2025



  *  __ Print

  * __ PDF




* * *

Article summary

Did you find this summary helpful?  __ __ __ __

Thank you for your feedback\!

For new updates, follow this link: <https://updates.overview.ai/>  
  
On this page you will find all the release notes from Overview’s software updates:

**v2024.18.90 \(Sept 24, 2024\)**

**🆕 View All ROIs** : The View All ROIs page now loads significantly faster than before. By caching ROIs that don’t need to be regenerated, ROIs that have already been generated will be reused and not processed again. The first time the page is opened will take the same time to load as it still needs to generate all the ROIs from scratch, but subsequent loads will be much faster than before.

**🆕 Imaging Setup → Autofocus** : Autofocus is now back in the product and can be used to automatically find the optimal focus for the camera. To use it, place the part under the camera, make sure it is still, and then click the Autofocus button. It may take some time for the camera to autofocus and find the optimal focus setting.

**🆕 NodeRED:** A new “camera\_id” field has been added to the All Block Outputs data. This is the unique serial number ID for the camera, and will always be the same for a given camera. This is useful for multi-camera deployments that need to correlate data between several cameras.

**🆕 NodeRED Recipe Switching:** When recipe switching \(through any mechanism, manual or PLC\), the camera switches to the new recipe’s NodeRED flow much faster than before, leading to a much faster overall recipe switch time. Switching the flow now takes roughly 1 second, which is a 5-10 second improvement compared to before.  
🆕 Navigating between blocks can be done directly in the navigation bar now with a dropdown in the breadcrumb, instead of having to go back to the recipe page.

🆕 Blocks have been renamed to make things more intuitive and understandable for users. Alignment Block -> Template Image and Alignment, ROI Block -> Inspection Setup, Classification/Segmentation Block -> Label and Train.

💄 **PROFINET:** The default cycle time in the PROFINET GSDML file has been increased from 16ms to 128ms. A slower cycle time leads to significantly better stability when operating the camera while connected to a PROFINET PLC. This change only applies for newly installed GSDML files in PLC software. Existing PLC programs can modify the cycle time setting directly in PLC software to achieve better stability.

💄 **PROFINET:** When PROFINET is enabled, there is now better messaging and informational alerts describing the behavior of the camera IP address. Since the PLC manages the cameras IP address when PROFINET is enabled, the on-board IP address configuration page does not have an effect.

💄 **Software Updating:** A link to the latest software download has been added to the Software Update page.

💄 **Software Updating:** The camera will now block software downgrades to older versions of software, as downgrading can easily lock the camera data.

💄 **Exposure:** The maximum exposure has been increased from 500ms to 1 second.

💄 **Segmentation Block:** The ability to draw a straight line / polygon by holding Shift has been restored. The keyboard shortcut for the ‘Move’ tool has been changed to the space bar instead of Shift.

💄 **Serial Number:** The serial number of the camera is now visible on all pages in the top right corner next to the software version.

💄 **ROI Block:** All ROI’s can be locked or unlocked at the same time with a single click by using the bulk locking button at the top of the table.  
💄 For both EthernetIP and PROFINET, the timing of the Inspection Complete bit, the Trigger Ready bit, and the Busy bit have been modified to make the camera behavior clearer and make PLC programming easier during capture and response. This is not a breaking change and should not affect any existing programs. See the new state diagram in the manual for specifics.

🐞 Memory leak issues with repeated recipe switching have been fixed. Previously, repeated recipe switches will eventually exhaust system resources.

💄 The dashboard interface will resize itself and scale down when displayed on small screens, so content will not overflow.

💄 Spanish manual is now available offline onboard the camera.

💄 The navigation menu has been simplified to be without submenus to make things easier to navigate.

💄 Additional checks at boot time for potential issues with the live feed.

💄 The dashboard interface is better scaled for intermediate sized screens, so content won’t overflow.

💄**PLC:** EthIP and PROFINET stability and bit behavior are improved. 1\) The BUSY bit set is to TRUE and TRIGGER\_READY is set to FALSE at the start of training. 2\) EthIP and PROFINET communications restart at the completion of training. 3\) Communication cycle timing is a lot more stable.

💄 **NodeRED:** Persistent context variables that save between restarts is available as an option when saving variables.

💄 **NodeRED:** All Block Outputs support incoming payloads larger than 65KB now, which can happen if there are more than ~100 segmenter blobs.

🐞 **ROI Block:** Bug where ROI’s could have accidentally been ‘sheared’ and transformed into a parallelogram when holding shift is fixed.

🐞 **PROFINET:** Bug introduced in v2024.17.1 where IP addresses configured by the PLC/TIAPortal did not take effect on the camera is fixed.

🐞 **Segmentation Block:** Fixed minor layout issues in the View All ROI’s page for segmentation ROIs.

🐞 Button alignment in the segmenter page is corrected.

🐞 Issue with the camera automatically triggering on recipe switch when in PLC Trigger Mode and using photometric mode is fixed.

🐞 Issue with database connections hitting the limit when using FTP is fixed.

🐞 Issue with the live stream booting to a solid gray stream in rare cases is fixed.

🐞 Fix for cameras hanging after updating from v2024.16.0.

🐞 Fix for occasional software update issues leaving the software unable to start.

🐞 Memory leak issues with repeated recipe switching have been fixed. Previously, repeated recipe switches will eventually exhaust system resources.

🐞 Fix for heat maps in the library for classification captures being misaligned.

🐞 **Storage Watcher:** For old captures, the data in the database is now also correctly deleted in addition the image file itself, in the case when the SD card is full and new captures are made.

**v2024.17.1 \(Jul 6, 2024\)**

**🆕 Lens Distortion Correction Mode:** Enhance the imaging accuracy by correcting for lens distortion during the Imaging Setup process. All lenses have some degree of distortion, and the distortion is more apparent the shorter the focal length of the lens. Correcting for lens distortion can enhance the accuracy of alignment and model prediction, by ensuring parts are dimensionally accurate no matter where in the frame it is. The lens focal length \(6mm, 8mm, 12mm, 16mm, and 25mm\) can be selected under Imaging Setup. The OV20i out of the box ships with a 12mm lens.

💄 **Software Updating:** All software updates starting this version will now be faster than before, and the time it takes will no longer depend on how much data is stored onboard. Previously, the more existing production data, the longer an update will take. All updates should now take roughly 15-20 minutes.

💄 **On-Board Offline Manual:** Downloadable \*\*\*\*files attached in the manual such as CAD drawings and PLC program samples are now downloadable offline without internet. Issue with the manual not loading due to a Document360 formatting change is fixed.

💄 **NodeRED Dashboard** : A shortcut page at [_http://CAMERA\_IP/ui_](http://CAMERA_IP/ui) is now available and always links to the NodeRED dashboard originally at _http://CAMERA\_IP:1880/api/ui_.

💄 **Import and Export** : Import errors are now a lot more informative and will display the reason behind a recipe import failure. A common reason for import failure is trying to import a recipe exported from a newer version of the software into a camera running an older version.

💄 **NodeRED** : When connected the camera over the Micro-USB port, the _image\_url_ field now correctly returns a valid IP address: if both the Micro-USB and M12 Ethernet port are connected, it will use the Ethernet port address, and if only the Micro-USB port is connected, then it will use the micro-USB address of 192.168.55.1.

💄 **System Settings** : The camera IP address settings will now always reflect the settings for the M12 Ethernet port, no matter how the camera is connected \(micro-USB or Ethernet\). Only the Ethernet port settings are user-configurable, as the Micro-USB port has a fixed IP address.

🐞 Long running bug but rare bug with NodeRED port conflicts causing service startup issues is fixed.

🐞 Bug with the HMI table not showing all ROIs in a given Inspection Type is fixed.

**v2024.16.2 \(Jun 19, 2024\)**

**🆕 Segmentation Block:** A new AI annotation tool is available to help annotate segmentation data much faster and intelligently. The AI annotation tool acts like a "magic wand", and will automatically annotate additional areas of the image that are visually similar to the selected patch. The tool can be used to both smartly label and unlabel areas of the image. By using this tool, annotating segmentation data is not only much faster to do but also more consistent and accurate. For more complex defects, it is useful as a first-pass to bulk annotate relevant areas before fine-grained annotation by hand. This AI tool is executing entirely in the frontend and requires moderate system resources to run.

**🆕 Telemetry:** Telemetry data is now being collected starting in this version. This data is helpful to track camera usage, track what customers spend time doing on the dashboard, see how recipes are set up, and to help identify potential issues before customers need to reach out. It is very useful to have this information while supporting customers remotely. This is only collected when the dashboard is open and the computer using the dashboard has an internet connection. This is an opt-out feature and can be disabled in the Settings page.

**🆕** **HMI:** The HMI has been updated to include an option to only show the most recent failed capture. In this mode, instead of showing all captures and their results, it will only show the most recent failed capture. This is useful for customers who are running a high volume of captures and only want to see the most recent failed capture.

**🆕 Software Updating:** An option is now available to automatically start the software update process after the .ovupdate file has been uploaded. Instead of a two-step process where the user uploads the .ovupdate file, waits for it to upload, and then has to manually trigger the update, the user can now upload the .ovupdate file and the update process will automatically start.

💄 **Segmentation Block:** Keyboard shortcuts can now be used to toggle between the various drawing modes, such as between the eraser brush and the paint brush, and between the pan tool.

💄 **Photometric Mode:** The photometric algorithm has been improved and now runs entirely in CUDA instead of ONNX, which makes it faster and provides a better merged image.

🐞 **Segmentation Block Training:** Bug with the training process diverging and hanging on complex datasets has been fixed. There is a very high chance that models trained with this fix would perform significantly better. So it is advised that all active projects using segmentation models to update and retrain. Just make sure to back up the old recipes in case of unexpected degradation.

🐞 **Library:** Bug with the capture metadata filters being gray and disabled has been fixed.

**v2024.15.0 \(Jun 8, 2024\)**

🆕 **Library:** Alignment results are now shown in the library for each capture. This includes confidence, matched rotation angle found, and the center x/y location of the part, which can be useful for debugging and understanding the alignment process.

🆕 **ROI Block:** Masking portions of the ROI is now supported with the ROI masking tool. This operates with a brush and eraser, and can be used to mask and exclude sections of an ROI that are not relevant for the model to learn. For example, for a circular washer, the center hole can be masked out with the brush, so the model will focus solely on the washer material itself instead of the center hole. Another example is printed silkscreen on a PCB component - if the text is not relevant to the inspection, that area can be masked out so the model isn't trying to learn text. Internally, the masked portions of the ROI are converted to a neutral grey. You will see the mask applied to the ROI when inside the "View All ROIs" modal.

🆕 **Segmentation Block:** Augmentations are now supported in the segmenter block. This includes flipping, rotation, and scaling. This can be used to increase the diversity of the training set and improve the model's ability to generalize

💄 **Segmentation Block:** While annotating, if a brush is drawn over an ROI, the ROI will automatically be checked and therefore be included as part of the training set.

💄 After training is triggered, all ROIs will be locked to avoid accidental modification.

💄 The minimum required samples needed for the classification block and for the segmentation block has been reduced to 1. A warning will show if there are fewer samples than recommended, but it will not prevent a model from being trained.

💄 **Classification Block:** After capturing, if an ROI is partially or entirely out of the frame due to a rotated alignment result, that ROI will not automatically be labelled when clicking on the class button.

💄 **NodeRED:** The timeout for waiting for a pass/fail result from NodeRED is increased from 0.2 seconds to 2 seconds. Depending on the complexity of the logic that determines pass/fail, this can help prevent false negatives due to slow computation or waiting for external data. This is an upper limit, so if the result is ready before 2 seconds, it will still be processed immediately.

💄 The default rotation augmentation of +/- 5 degrees is removed from the classification block and the segmentation block. This is because it may unintentionally rotate the defect out of the frame, which will pollute the training set. If rotation augmentation is desired, it can be added manually configured.

**v2024.14.1 \(May 23, 2024\)**

🆕 **NodeRED:** There are new fields available in the ‘ _All Block Outputs_ ’ payload for global x/y positioning of segmentation blobs and classification ROI results. These values \(`center_x_global`, `center_y_global`\) are absolute positions of the blob and ROI relative to the full capture frame-of-reference, which can be useful for measurement or guidance applications that need absolute positioning. These new fields are in addition to the existing blob x/y locations that are relative to the ROI frame-of-reference. Additionally there is a new top-level `roi` object for ROI IDs, ROI names, ROI angles, and ROI positions that is useful for more complex flows that use further processing.

🆕 **Library:** Custom User Metadata can now be filtered and searched for in the library. You can search for all captures that have a given key - for example, captures that have a ‘Barcode’ key, without specifying a specific barcode number. You can also search for captures that have a given key-value pair - for example, captures that have a ‘Barcode’ key and a value of 12345. User Metadata supports boolean and string types, and both can be searched for.

🆕 **NodeRED:** New Ignition nodes be used to interface with Ignition MES systems by Inductive Automation. It allows for the reading, writing, and browsing tags configured in Ignition. This is a community-supported node and can only be used to talk to Ignition 8.1.25+ or later.

💄 **Import/Export:** The recipe name is now part of the filename of the exported zip.

💄 **View All ROIs:** In the segmentation View All ROIs interface, the top bar to control opacity and filters will stay fixed at the top as you scroll down.

💄 **Aligner Block:** Aligner search areas are constrained to the full frame and will bounce back if dragged out of bounds.

🐞 **Import From Library:** Issue with using the shift key to select multiple captures at once is fixed in the Import From Library menu.

**v2024.13.0 \(May 16, 2024\)**

🆕 **Segmentation and Classification Block:** The _Optimizing Model_ step during training now runs much faster than before. Depending on how many classes are used in training, this step previously took 5-15 minutes and should now take no longer than a minute or so for the vast majority of scenarios. This is especially apparent for first-time model trainings, where the internal TensorRT timing cache has not been generated yet. With this update, the timing cache is pre-generated and included as part of the software.

🆕 **Alignment Block:** A template image can now be imported from the library, instead of only being able to capture one in real time. This is useful for scenarios where you want to try another template image or revert back to a previous one.

🆕 **Alignment Block:** Search areas can be specified to restrict areas where the aligner can find an alignment, instead of looking for it anywhere in the frame. This is beneficial for certain applications such as ones using aligner trigger mode, where restricting the area can lead to a more accurate and reliable aligner. The aligner will also run faster than before, depending on the size of the search area. New recipes now have a default search area that encompasses most of the full frame and can be adjusted as needed. Old recipes are not affected and default to searching the full frame, which is the same behavior as before. The search area is indicated in all live preview modes.

🆕 The on-board embedded manual has been updated to use our new manual \(available online at [docs.overview.ai](http://docs.overview.ai)\). The on-board manual is accessible offline with the same content as the online version.

💄 **NodeRED:** The RS485 serial port on the 17-pin connector is now accessible through NodeRED at `/dev/ttyTHS1`.

💄 **Alignment Block:** The center location of the found alignment \(center\_x, center\_y\) is now shown on the live preview as a red dot, to better visualize and use that information.

💄 **View All ROIs:** Bulk labeling and unlabeling will clear all selected ROIs.

💄 ROI label names in the dashboard will always be visible now no matter where the ROI is placed. Previously an ROI placed at the top of the frame cuts off the ROI name label.

🐞 **HMI:** Issue with exiting out of full screen mode with the escape key hiding the menu sidebar is fixed.

🐞 Users and Permissions: Issue with permissions reverting back to “Anybody” if the dashboard is loaded before the camera is fully online is fixed.

**v2024.12.0 \(May 7, 2024\)**

💄 **Library:** Traversing quickly through pages of the library is significantly more performant now especially on slower network connections to the camera. When switching pages, all outstanding image load requests are cancelled so the next page takes priority. Previously, skipping quickly between pages will queue up image loads, so the next page will wait until all previous pages finish loading.

💄 **Segmenter Block:** final training accuracy scores are now more reflective of actual accuracy and track closer to training accuracy. The discrepancy is due to a combination of augmentations being added to training images but not final accuracy test images, and images being in different batches during training.

💄 General stability and robustness improvements in segmenter model training.

🐞 Fix issue with “Go To Source Image” not working from “View All ROIs” for segmenter block.

🐞 Adjust and fix the alignment of the checkbox for each ROI in the segmenter block.

**v2024.11.0 \(April 30, 2024\)**

🆕 **NodeRED:** New serial port node can be used to connect to external systems over the OV20i’s serial ports. There is a RS485 serial port on the 17-pin connector. To communicate with RS232-based systems, an external conversion adapter can be used. Baud rates, parity, and other serial port configurations can be set within the node.

🐞 Fix issue with captures from a segmentation block being misaligned in the library.

🐞 Fix issue with some recipe zips not importing correctly.

**v2024.10.0 \(April 22, 2024\)**

💄 The healthcheck timeout per-request is upped from 5s to 30s only when training is in progress, which should lead to better perceived stability especially during segmentation training. This is to get around the system locking up all network sockets during heavy training load, when a request that normally takes 100ms can take more than 10s to reply, therefore showing the "camera services" error, even though training is still progressing normally.

💄 For a dropdown selection with more than 3 selections, it will collapse the menu, so when there are a lot of selections made in a dropdown, it won't take a ton of space \(especially for View All ROIs\)

💄 Support source\_recipe\_id backfill for the updated library for upgrading from pre-segmenter versions older than v2024.2.1 \(the first segmenter release\)

🐞 Fix issue with ROI cloning button not working for segmenter mode

🐞 For recipe exports with a lot of ROIs per capture \(i.e. a recipe with >10 ROIs defined in the ROI Block\), exports will now properly include all ROIs

**v2024.9.0 \(April 11, 2024\)**

🆕 **ROI Block** : There is now a "Lock" function for each ROI region that can be used to avoid accidental modification and also to more easily manipulate overlapping ROIs. By locking a ROI, it cannot be dragged or clicked on in the canvas, and acts 'invisible' so ROIs underneath can be clicked on.

🆕 **Library** : Captures can now be searched by the PLC Trigger ID, which is the rolling 16-bit ID that is sent to NodeRED and over PLC communications. This is used to more easily correlate images between the library and a PLC system tracking triggers by the Trigger ID. Note that there can be multiple captures with the same PLC Trigger ID, because it is a rolling 16-bit number \(max of 65536\). This ID is also shown under the capture information section.

🆕 **Library:** The Trigger Mode \(PLC trigger, HW trigger, interval trigger, etc\) that was used to capture a given image is now shown in each captures information section.

💄 **Imaging Settings** : Max exposure time is now up to 500ms, from 150ms previously.

💄 Error and warning messages have been revised to be a lot more informative all around, including the one for camera reachability, mqtt connections, aligner failures when importing from the library, and segmentation block annotation warnings.

🐞 **Library** : The "capture is used for training" indicator is now correct and indicates whether an image is used in a training set of any recipe. If it is removed from a training set, it will also correctly unmark it as "for training". This is also now indicated in the thumbnails, so you can quickly see which images are used for training without having to click into each one.

🐞 **Library** : Filtering by a specific recipe now correctly shows all captures ever made under that recipe. Previously, some images that were captured during recipe training did not show when filtered by that recipe.

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
