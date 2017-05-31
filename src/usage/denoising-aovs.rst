Denoising AOVs
==============

By default Altus will take every input AOV and use their contributions to denoise the single RGB image (i.e. beauty render).
Altus can also denoise AOVs along with the RGB image.

This guide will explain the various denoise options and provide examples.

``--filter-aov``
----------------

This option will enable denoising AOVs along with the rgb image (beauty render). The options for this flag are: {prefiltered, preview, production}

Each option corresponds to a denoise quality level where 'prefiltered' is the fastest, 'preview' is a mix between speed and quality, and 'production' is the highest quality.  Note:  These quality levels are independent of the ``--quality`` flag
used for RGB image (beauty render) denoising.  This makes it possible to denoise the RGB image at the highest quality and denoise other AOVs at lower quality levels.

Once ``--filter-aov`` is specified Altus will denoise and save *all* input AOVs as part of the multi-layer exr output.  Denoised AOVs will include all named AOVs (such as nrm, vis, alb, etc.) as well as extra and additional AOVs.

Saving denoised AOVs to non-multilayer EXRs is not supported.

``--additional``
----------------

Specify AOVs which require denoising but will not contribute to the denoise quality of any image.

Specifing additional AOVs will let you denoise those AOVs without incurring the runtime cost of using those AOVs to filter RGB.

.. Note::
    To denoise and save additional AOVs '--filter-aov' must be specified.  Otherwise additional AOVs will be bypassed by Altus.



Example Usage
-------------

In the example config below we are providing Altus with two AOVs (position and reflection) that will be utilized when denoising.  We also give an additional AOV (shadow) that will not be used when denoising but will be available for denoising if you decide to denoise AOVs.

Here is an example config file when using two buffers::

    rgb-0=C:\path\to\file\beauty_b0.exr
    rgb-1=C:\path\to\file\beauty_b1.exr
    pos-0=C:\path\to\file\position_b0.exr
    pos-1=C:\path\to\file\position_b1.exr
    extra-0=C:\path\to\file\reflection_b0.exr
    extra-1=C:\path\to\file\reflection_b1.exr
    additional-0=C:\path\to\file\shadow_b0.exr
    additional-1=C:\path\to\file\shadow_b1.exr

If we don't specify the ``--filter-aov`` flag then the output file will contain only the rgb (beauty render) output and none of the AOVs will be denoised.

If we specify ``--filter-aov`` then the output exr image will contain the denoised rgba and the denoised AOVs (position, reflection, shadow) as layers.
