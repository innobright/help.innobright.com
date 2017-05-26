Output Options
-----------------

Altus will save the denoised result as an exr image.  Denoised AOVs will be saved as a multi-layer exr.  Altus has various options/flags which 

.. Warning::
    
    Altus has problems dealing with data windows that are smaller than display windows. As a workaround, data windows will be ignored on file write.

``--out-path`` or ``-O``
----------------------------
the absolute file path that serves as a template for output file paths. '####' and '%4d' in the base name are supported

``--out-dir`` or ``-o``
-----------------------------

The path to the directory to which filtered images are written
   
``--scene-name`` or ``-i``
-----------------------------

The name of the scene being processed (default: guessed)


``--preserve=layers`` or ``-p``
-----------------------------

Original layers in a multi-layer OpenEXR image given for "rgb" input AOV can be preserved and saved as layers inside the filtered output image by passing `--preserve=layers` to Altus.


``--quality``
-----------------------------
This flag will set the output denoised quality level.


``--filter-aov``
-----------------------------
This flag will denoised and output all given AOVs including named input AOVs (nrm, vis, alb, etc), extra AOVs and additional AOVs.