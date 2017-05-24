Denoising AOVs
--------------

By default Altus will take all input AOVs and use their contributions to denoise the single rgb image (beauty AOV).  Altus also supports denoising multiple AOVs simultantiously.

``--filter-aov``
------------------------

This option will enable denoising AOVs in addition to the rgb image (beauty AOV). The options for this flag are: {prefiltered, preview, production}

Each option corresponds to a denoise quality level where 'prefiltered' is the fastest, 'preview' is a mix between speed and quality, and 'production' is the highest quality.  Note:  These quality levels are independent of the '--quality' flag 
used for rgb image (beauty AOV) denoising.  This makes it possible to denoise the rgb image at the highest quality and denoise other AOVs at lower quality levels.

Once --filter-aov is specified Altus will denoise and save all input AOVs as a multi-layer exr.  Denoised AOVs will include all named AOVs (such as nrm, vis, alb, etc.) as well as extra and additional AOVs. 

``--additional``
------------------------

This flag was added in Altus 1.8.3 to specify AOVs which require denoising but will not contribute to denoise quality.  To denoise and save additional AOVs '--filter-aov' must be specified.
