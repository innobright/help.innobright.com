# Known Issues

This document details known issues and problems, and their workarounds, in the latest version of Altus.

These will be fixed in a future release.

 * If filtering a large image on GPU and CUDA fails, consider trying OpenCL on GPU.
 * OpenCL and CUDA-related errors can be obtuse. If you encounter one you don't understand, contact support@innobright.com and we'll help.
 * Bugs exist with images where the OpenEXR data window is not the same as the display window.
 * OpenEXR images with data windows smaller than the display window are not preserved on file write. We expand the data window to match the display window. This does not effect filtering speed or file size.
 * Normalized extra AOVs have both CLI and configuration file options, but these have no effect and those AOVs will be ignored.
 * If Altus 1.8 encounters a licensing error while filtering, it will insert a watermark instead of quitting, regardless of `--force-continue`. This behavior is consistent with previous versions of Altus but may not be desired. Please make sure network connectivity to your licensing server is stable.
 * Before Altus 1.8, running Altus with `--version` would print license status. In 1.8, this is broken, but will be fixed in a future release. The only way to determine license status is by running Altus on images.
 * Altus for macOS requires macOS 10.11 (El Capitan) or later; in the future the minimum requirement will be macOS 10.9 (Mavericks).
