Denoising AOVs
--------------

By default Altus will take every input AOV and use their contributions to denoise the single rgb image (beauty render).  Altus also supports denoising AOVs along with the rgb image.  This guide will explain the various denoise options and provide an example usage.

``--filter-aov``
------------------------

This option will enable denoising AOVs along with the rgb image (beauty render). The options for this flag are: {prefiltered, preview, production}

Each option corresponds to a denoise quality level where 'prefiltered' is the fastest, 'preview' is a mix between speed and quality, and 'production' is the highest quality.  Note:  These quality levels are independent of the '--quality' flag 
used for rgb image (beauty render) denoising.  This makes it possible to denoise the rgb image at the highest quality and denoise other AOVs at lower quality levels.

Once --filter-aov is specified Altus will denoise and save *all* input AOVs as part of the multi-layer exr output.  Denoised AOVs will include all named AOVs (such as nrm, vis, alb, etc.) as well as extra and additional AOVs.

``--additional``
------------------------

This flag was added in Altus 1.8.3 to specify AOVs which require denoising but will not contribute to denoise quality.  

.. Note::
    To denoise and save additional AOVs '--filter-aov' must be specified.  Otherwise additional AOVs will be bypassed by Altus.


**Example Usage**

In the example config below we are providing Altus with two AOVs (position and reflection) that will be utilized when denoising.  We also give an additional aov (shadow) that will not be utilized when denoising but will be availble for denoising if you decide to denoise AOVs.

Here is an example config file when using two buffers::

    rgb-0=C:\path\to\file\beauty_b0.exr
    rgb-1=C:\path\to\file\beauty_b1.exr
    pos-0=C:\path\to\file\position_b0.exr
    pos-1=C:\path\to\file\position_b1.exr
    extra-0=C:\path\to\file\reflection_b0.exr
    extra-1=C:\path\to\file\reflection_b1.exr
    additional-0=C:\path\to\file\shadow_b0.exr
    additional-1=C:\path\to\file\shadow_b1.exr

If we dont specify the ``--filter-aov`` flag then the output file will contain only the rgb (beauty render) output and none of the AOVs will be denoised.  

If we specify ``--filter-aov`` then the output exr image will contain the denoised rgba and the denoised AOVs (position, reflection, shadow) as layers.
