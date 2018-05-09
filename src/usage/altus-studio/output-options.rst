Output Options
==============

Altus will save the denoised result as an EXR image.
Denoised AOVs will be saved as a multi-layer EXR.

.. Warning::

    Altus has problems dealing with data windows that are smaller than display windows. As a workaround, data windows will be ignored on file write.

``--out-path`` or ``-O``
------------------------

the absolute file path that serves as a template for output file paths. '####' and '%4d' in the base name are supported

``--out-dir`` or ``-o``
-----------------------

The path to the directory to which filtered images are written

``--scene-name`` or ``-i``
--------------------------

The name of the scene being processed (default: guessed)


``--preserve-layers`` or ``-p``
-------------------------------

Original layers in a multi-layer OpenEXR image given for "rgb" can be preserved and saved as layers inside the filtered output image by passing ``--preserve-layers`` to Altus.


``--quality``
-------------

Set the quality level of the denoised RGB image.
