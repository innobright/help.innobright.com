Known Issues
============

This document details known issues and problems, and their workarounds, in the latest version of Altus.

These are typically not fixed because we have incomplete information on how to resolve them.
However, the plan is to fix them in a future release.

Core
----

* If filtering a large image on GPU and CUDA fails or produces a black image, consider trying OpenCL on GPU. The OpenCL version of Altus is more resistant to failures. Innobright plans to discontinue general availability of the CUDA version of Altus in the future.
* Bugs exist with images where the OpenEXR data window is not the same as the display window.
* OpenEXR images with data windows smaller than the display window are not preserved on file write. We expand the data window to match the display window. This does not effect filtering speed or file size.

GUI
---

* Manually editing file paths in the GUI to use format specifiers will cause Altus to be unable to revert to the original paths when switching animation on/off. It's recommended to let Altus autoconvert the format specifier in paths. If you find an issue in this workflow contact support@innobright.com to let us know!
* GUI does not support '#' symbols in the file path. Please use "%01d" type specifier when working on animation sequences.
* The GUI will not display accurate license status until Altus is run on an image.

UX
---

* If filtering a large image that does not fit into memory, you can use the :option:`--tile` option to denoise an image in smaller chunks. Tiling is slower, however. This recommendation should be printed when Altus fails because it has run out of memory.
* OpenCL and CUDA-related errors can be obtuse. These errors are what 3rd party OpenCL and CUDA implementations to return to us, so it's not always possible for us to provide a better error message. If you encounter one you don't understand, contact support@innobright.com and we'll help.

Licensing
---------

* If Altus 1.8 encounters a licensing error while filtering, it will insert a watermark instead of quitting, regardless of :option:`--force-continue`. This behavior is consistent with previous versions of Altus but may not be desired. Please make sure network connectivity to your licensing server is stable.
* Before Altus 1.8, running Altus with :option:`--version` would print license status. In 1.8, this is broken, but will be fixed in a future release. The only way to determine license status is by running Altus on images.
