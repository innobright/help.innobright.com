Denoising AOVs
==============

By default Altus will take every input AOV and use their contributions to denoise the single RGB image (i.e. beauty render).
Altus can also denoise AOVs along with the RGB image.

This guide will explain the various denoise options and provide examples.

``filter-aov``
----------------

This option will enable denoising AOVs along with the rgb image (beauty render). When enabled in Altus Studio, you can then set the quality level of AOVs between the following: {prefiltered, preview, production}

Each option corresponds to a denoise quality level where 'prefiltered' is the fastest, 'preview' is a mix between speed and quality, and 'production' is the highest quality.  Note:  These quality levels are independent of the ``quality`` setting used for RGB image (beauty render) denoising.  This makes it possible to denoise the RGB image at the highest quality and denoise other AOVs at lower quality levels.

Once ``filter-aov`` is enabled, then Altus will denoise and save *all* input AOVs as part of the multi-layer exr output.  Denoised AOVs will include all named AOVs (such as nrm, vis, alb, etc.) as well as extra and additional AOVs.

Saving denoised AOVs to non-multilayer EXRs is not supported.

``additional``
----------------

Specify AOVs which require denoising but will not contribute to the denoise quality of any image.

Specifing additional AOVs will let you denoise those AOVs without incurring the runtime cost of using those AOVs to filter RGB.

.. Note::
    To denoise and save additional AOVs '--filter-aov' must be specified.  Otherwise additional AOVs will be bypassed by Altus.
