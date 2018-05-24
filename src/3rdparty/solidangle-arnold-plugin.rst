Denoise SolidAngle Arnold renders with Altus
============================================

.. warning::

    This article is under construction and will be updated.  If you find any issues with the documentation please contact us at support@innobright.com


Overview
--------

Altus-Arnold plugin integrates the denoiser directly into the Arnold renderer as an output driver.  This allows you to automatically denoise after rendering once, all without saving intermediate images.  The plugin uses sample information from the renderer to generate a high quality denoised image.  The driver can also export the required images to denoise at a later time with our Standalone products (Altus-Studio and Altus-CLD). This guide will explain how to setup and use the Altus-Arnold plugin.

Generally, Altus uses AOVs to enhance denoise quality and retain extra details.  AOVs provide a way to render any arbitrary shaded component into different images. Typically renderers will only produce a final color for each pixel of the image, but you can break out renders into their component parts such as indirect lighting, diffuse color, reflections, shadows, mattes, etc. and save them as AOVs individually. The denoiser quality will improve with more AOVs given as inputs to Altus.


Install the Plugin 
------------------

.. Warning::

	Contact us at support@innobright.com for the packaged Altus-Arnold BETA plugin.

Altus-Arnold plugin comes in a packaged zip with two libraries.  These libraries must be placed in a directory that is searched by the renderer or a content creator like Maya.  

Currently we recommend copying the libraries to the bin and shader folders.  By default, on Windows (2017) that is ``C:/solidangle/mtoadeploy/2017/bin`` and ``C:/solidangle/mtoadeploy/2017/shader``.  This will cover most options, the renderer searches /bin/ and content creators like Maya/C4d/etc will load from /shaders/.


InputAOVs
---------

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

Now that the plugin can be found and loaded, lets add it to a project.  The Altus-Arnold plugin works as an output driver that will denoise and save the images.  Arnold lets you select an output driver for each AOV.  We recommend changing the output driver of the beauty (or RGBA) AOV to use Altus-Arnold driver.  However, you can add additional AOVs to denoise and save by changing the "FilterAOVs" setting (more info below).

Most Arnold plugins like MtoA, or C4DtoA will expose the AOV's drivers in their UI panels for easy access.  This makes it simple to add Altus-Arnold denoiser as a driver.  However, you can also edit the .ass file to manually add Anrold-Altus driver to the AOV.

Below is a snippet of an .ass file exported from MtoA, this snippet shows the various AOV outputs of the scene including RGBA, Normals, Position, Albedo, etc.

.. code-block:: html

	outputs 6 1 STRING
	 "RGBA RGBA defaultArnoldFilter@gaussian_filter aiAOVDriver2@altus_arnold_driver.RGBA"
	 "N VECTOR aiAOVFilter3@closest_filter defaultArnoldDriver@driver_exr.N"
	 "P VECTOR aiAOVFilter2@closest_filter defaultArnoldDriver@driver_exr.P"
	 "albedo RGB defaultArnoldFilter@gaussian_filter defaultArnoldDriver@driver_exr.albedo"
	 "diffuse RGB defaultArnoldFilter@gaussian_filter defaultArnoldDriver@driver_exr.diffuse"
	 "diffuse_indirect RGB defaultArnoldFilter@gaussian_filter defaultArnoldDriver@driver_exr.diffuse_indirect"


Each output entry has the following format:

.. code-block:: html
	
	AOV_Name, AOV_Type, pixel_filter_name, output_driver_name

Notice the output driver of the RGBA (beauty) AOV points to ``aiAOVDriver2@altus_arnold_driver.RGBA``.  This is the name MtoA has given to Altus-Arnold driver.


Plugin Settings
---------------

Below is an example usage of Altus-Arnold plugin taken from the same .ass file exported with MtoA above.

.. code-block:: html
 
	altus_arnold_driver
	{
	 name aiAOVDriver2@altus_arnold_driver.RGBA
	 FilterWindow 10
	 FilterAOVs "RGBA,P,N"
	 InputAOVs "N,P,diffuse_albedo"
	 denoiseBuckets on
	 preview off
	 gpu on
	 useSinglePass off
	 verbose on
	 outputBuffers on
	 maxTileSize 0
	 autoTileMemory 0
	 kc1 0.45
	 kc2 0.45
	 kc3 0.75
	 kf 0.6
	 filename "[...]/images/beauty/test_filter.exr"
	}


Altus Denoiser settings:
 * FilterWindow:  The overall constraint to the filter.  Larger numbers will increase quality at a cost of speed.  The default of 10 is a good balance. 
 * kc1,kc2,kc3: 	Color sensitivity at various frequences. (kc1 = high freq details, kc2 = mid details, kc3 = large details)  Low numbers give more detail, higher numbers will aggressively denoise.
 * FilterAOVs:	AOVs to filter.  Altus will denoise and output these AOVs.
 * InputAOVs: 	Input AOVs that Altus uses for denoise quality.  We recommend six AOVs from Arnold, visit for more info: https://help.innobright.com/3rdparty/solidangle-arnold/
 * Preview:  	Toggles preview/production quality.  Preview is great for iterative workflows, production gives the best results.

Altus Memory settings:
 * maxTileSize:  	Altus will internally split the image into tiles to denoise with less memory.  This sets the max tile size in pixels. 0 will disable internally tiling.
 * autoTileMemory:  Altus can select the best tile size.  This option sets the max memory usage in megabytes (MB) and Altus will configure itself to run below the limit.  0 will disable tiling.

Altus Plugin settings:
 * denoiseBuckets:  Toggles between denoising the entire image at once (buffer mode), or denoise each bucket as it finishes rendering (bucket mode).
 * gpu:  		 	Use GPU (GPUs with large VRAM are highly recommended until internal tiling is implemented in this plugin)
 * verbose: 	 	Print to console
 * outputBuffers:  	This will output the intermediate buffers which can be denoised at a later time by standalone Altus products such as Altus Studio.

