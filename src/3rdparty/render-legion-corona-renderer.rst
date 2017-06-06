Denoise Render Legion Corona Render renders with Altus
======================================================

.. warning::

    This article is under construction and will be updated.


Overview
--------

Altus Denoiser uses information between two rendered images to generate a high quality denoised image. This guide will explain how to setup and render the inputs to Altus. There are two concepts that Altus uses to generate denoised outputs:

AOVs (Arbitrary Output Variables) provide a way to render any arbitrary shaded component into different images. Typically renderers will only produce a final color for each pixel of the image, but you can break out renders into their component parts such as indirect lighting, diffuse color, reflections, shadows, mattes, etc. and save them as AOVs individually. The denoiser quality will improve with more AOVs given as inputs to Altus.

Two images (called buffers) must be generated for each image. It's important that each buffer is rendered with a different sample seed so that they will have unique noise patterns. The variance between the two buffers is what Altus uses to remove noise. Without variance, there is not enough information to remove noise.

For information on how to run Altus once the correct inputs have been created see :doc:`/usage`.


Exporting AOVs
-----------------

Recommended List of AOVs to use with Altus:

+----------------+-----------------------+-----------------------------------------+
| **AOV type**   | **Altus Input Name:** | **Corona AOV Name**                     |
+================+=======================+=========================================+
| World Position | pos                   | CGeometry_WorldPosition                 |
+----------------+-----------------------+-----------------------------------------+
| Bump Normals   | nrm                   | CGeometry_NormalsShading                |
+----------------+-----------------------+-----------------------------------------+
| Visiblity      | vis                   | CShading_Shadows                        |
+----------------+-----------------------+-----------------------------------------+
| Albedo         | alb                   | CShading_SourceColor or CSading_Albedo  |
+----------------+-----------------------+-----------------------------------------+
| Reflection     | extra                 | CESSENTIAL_Reflect                      |
+----------------+-----------------------+-----------------------------------------+
| Caustics       | cau (Optional)        | <Unknown>                               |
+----------------+-----------------------+-----------------------------------------+


How to Output AOVs that are compatible with Altus from 3ds Max
##############################################################

Add AOVs to save from Corona (3ds Max) by opening the Render Settings Window:

.. image:: ./3dsmax/RenderSettingsCropped.png
   :scale: 60 %
   :align: center

Then switch to the Render Elements tab. This is where all the available Render Elements will be listed.  Clicking "Add" will open a selection window with available elements. You can select multiple elements by holding down ctrl while clicking. Select all the necessary elements:

.. image:: ./corona/Corona_Render_Elements_Tab.png
   :scale: 100 %
   :align: center

Once all Render Elements have been added, they will appear in the Render Elements tab.  Now you need to specify where to save each AOV by selecting each pass and in the Selected Element Parameters panel: ensure the 'Enable' check box is checked to render the pass.  Click on the '...' browse button to set the location on disk to save that pass and to set the output image extension to 'EXR'.  Repeat this process for all the selected passes:

.. image:: ./corona/Corona_Added_Render_Element.png
   :scale: 80 %
   :align: center

Exporting Two Buffers
----------------------

Altus requires two renders (called buffers) of the same scene to denoise properly.

Render Twice
############

Corona can generate the two buffers by rendering twice and changing the seed between renders.

Under the "Scene" tab, set the "Pass limit" to half of the requested number of passes before filtering.

.. image:: ./corona/Corona_Scene_tab.png
   :scale: 80 %
   :align: center


Under the "Performance" tab, in "Performance settings" ensure that the option “Lock the sampling pattern” is disabled ­ this way every time you hit the Render button the rendered image will be different ­ this is crucial for the denoising.

.. image:: ./corona/Corona_Performance_Tab.png
   :scale: 80 %
   :align: center

Now you are ready to render twice to get two renders with a different seed which Altus can denoise.


Render Once with Stereo
#######################

.. warning::

    This is not creating stereoscopic imagery; it is a mechanism to create the two buffers Altus needs without having to render twice.

You can render once using a stereo camera rig and Altus will divide the image into two buffers. The camera's (eye) separation should be set to 0.0 so the left and right camera's have the same location and their renders will be identical except for the noise pattern.

.. Note::
    This section is under construction and will be updated.
