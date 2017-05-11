Render Legion Corona Render and Altus
-------------------------------------

.. warning::

    This tutorial is for older versions of Altus; configuring Corona and Altus are significantly easier now.

First, create a directory where the renderings should be saved.
In this guide we will name it AltusWithCorona and the path to it will be C:/AltusWithCorona.
To be able to use Altus you need to render your scene with Corona two times with several modifications of your render settings. So in 3ds Max, under the "Rendering" tab hit "Render setup" and make sure Corona is selected as active Renderer. Now you need to do the following changes:

* Under the "Scene" tab, set the "Pass limit" to half of the requested number of passes before filtering.
* Under the "System" tab uncheck "Render stamp" generation, so it won’t appear on saved renders.
* Under the "Performance" tab, in "Performance settings" uncheck the option "Lock the sampling pattern" ­ this way severy time you hit the Render button the rendered image will be different ­ this is crucial for the denoising.
* Add the following render elements under the "Render elements" tab using "Add" button:

  * CShading_SourceColor ­ make sure that in "Source (Raw) Color" dialog the "Diffuse" is checked, and save it to a file named "albedo_b0.exr" to the AltusWithCorona directory,
  * CGeometry_WorldPosition, and save it to "position_b0.exr" also to the AltusToCorona directory,
  * CShading_Shadows, save it to "shadows_b0.exr" also to the AltusToCorona directory,
  * CGeometry_NormalsShading, save it to "normals_b0.exr" also to the AltusToCorona directory,

* Save the Beauty pass to an EXR file: Under the "Common" tab, in "Render output" settings, check "Save file" and save it to "beauty_b0.exr" also to the AltusToCorona directory.

Render the scene with these settings once.

After that rename all the output images so they end with _b1.exr instead of _b0.exr. This way it won’t rewrite the rendered
images and we will have all the passes twice with different noise patterns.
