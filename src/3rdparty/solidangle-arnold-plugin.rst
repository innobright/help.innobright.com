Denoise SolidAngle Arnold renders with Altus
============================================

.. warning::

    This article is under construction and will be updated.  If you find any issues with the documentation please contact us at support@innobright.com


Overview
--------

Altus-Arnold plugin integrates the denoiser directly into the Arnold renderer as an output driver.  Allowing you to automatically denoise after rendering.  The plugin uses sample information from the renderer to generate a high quality denoised image. This guide will explain how to setup and use the Altus-Arnold plugin.

Generally, Altus uses AOVs to enhance denoise quality and retain extra details.  AOVs provide a way to render any arbitrary shaded component into different images. Typically renderers will only produce a final color for each pixel of the image, but you can break out renders into their component parts such as indirect lighting, diffuse color, reflections, shadows, mattes, etc. and save them as AOVs individually. The denoiser quality will improve with more AOVs given as inputs to Altus.


Install the Plugin 
------------------
Altus-Arnold plugin comes in a packaged zip with two libraries.  These libraries must be placed in a directory that is searched by the renderer or a content creator like Maya.  

Currently we recommend coping the libraries to "C:\solidangle\mtoadeploy\2017\bin" and "C:\solidangle\mtoadeploy\2017\shader".  This will cover most options, the renderer searches /bin/ and content creators like Maya/C4d/etc will load from /shaders/.


InputAOVs
--------------

Recommended List of AOVs to use with Altus:

+----------------+-----------------------+-------------------------------+
| **AOV type**   | **Altus Input Name**  | **Arnold AOV Name**           |
+================+=======================+===============================+
| World Position | pos                   | P                             |
+----------------+-----------------------+-------------------------------+
| Bump Normals   | nrm                   | N                             |
+----------------+-----------------------+-------------------------------+
| Visiblity      | vis                   | Shadows                       |
+----------------+-----------------------+-------------------------------+
| Albedo         | alb                   | Diffuse                       |
+----------------+-----------------------+-------------------------------+
| Reflection     | extra                 | Reflection                    |
+----------------+-----------------------+-------------------------------+
| Caustics       | cau (Optional)        | Caustics                      |
+----------------+-----------------------+-------------------------------+

.. note::

    These AOVs can be produced with Arnold 4.2.16 and later; earlier versions did not support these AOVs by default, or had bugs during AOV generation.

Using the Plugin
----------------

Now that the plugin can be found and loaded, lets add it to a project.  The Altus-Arnold plugin works as an output driver.  Arnold lets you select and output driver for each AOV.  We recommend changing the output driver of the beauty (or RGBA) AOV to use Altus-Arnold driver.  This way the beauty will be the focus of the denoiser.  However, you can additional outputs from the denoiser by changing the "FilterAOVs" setting (more info below).

We've uploaded a video demonstraighting adding and using the driver in Maya and rendering using Render.exe from Maya:  https://shared.innobright.com/s/xOagmhrjb4OfZS3


Plugin Settings
---------------

Below is an example usage of Altus-Arnold plugin taken from .ass file exported with mtoa.

.. code-block:: html
 
	altus_arnold_driver
	{
	 name aiAOVDriver2@altus_arnold_driver.RGBA
	 FilterWindow 10
	 FilterAOVs "RGBA,P,N"
	 InputAOVs "N,P,diffuse_albedo"
	 useTiles on
	 asyncTiles on
	 preview on
	 gpu on
	 useHybrid off
	 verbose on
	 outputBuffers on
	 kc1 0.449999988
	 kc2 0.449999988
	 kc3 0.75
	 filename "[...]/images/beauty/test_filter.exr"
	}


Altus Denoiser settings:
 * FilterWindow:  The overall constraint to the filter.  Larger numbers will increase quality at a cost of speed.  The default of 10 is a good balance. 
 * kc1,kc2,kc3: 	Color sensitivity at various frequences. (kc1 = high freq details, kc2 = mid details, kc3 = large details)  Low numbers give more detail, higher numbers will aggressively denoise.
 * FilterAOVs:	AOVs to filter.  Altus will output these denoised AOVs.
 * InputAOVs: 	AOVs that Altus uses for quality.  We recommend six AOVs from Arnold, visit for more info: https://help.innobright.com/3rdparty/solidangle-arnold/
 * Preview:  	Toggles preview/production quality.  Preview is great for iterative workflows, production gives the best results.

Altus Plugin settings:
 * useTiles:  	 Toggles between denoising the entire image at once (buffer mode), or denoise each bucket as it finishes rendering (tile mode).
 * asyncTiles:     Async Tiles will wait to denoise a tile/bucket until all neighboring buckets have finished rendering.
 * gpu:  		 Use GPU (GPUs with large VRAM are highly recommended until internal tiling is implemented in this plugin)
 * verbose: 	 Print to console
 * outputBuffers:  This will output the intermediate buffers which can be denoised at a later time by standalone Altus products such as Altus Studio.

