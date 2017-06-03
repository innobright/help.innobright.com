Image formats
-------------

For the best quality possible, Altus Denoiser operates on `high-dynamic range (HDR) images`__.
The only HDR format currently supported is `OpenEXR`__ format.

__ https://en.wikipedia.org/wiki/High-dynamic-range_imaging
__ http://openexr.com/

Altus does NOT support JPEG, PNG, WebP, etc images.
Altus needs as much information as possible from a renderer to create the best quality output, and using lossy image formats will create suboptimal outputs that we don't stand by.

OpenEXR images can be 16-bit floating point (half) or 32-bit floating point (float) images.
8-bit integer images are not supported.

All of Altus' internal processing is done in 32-bit floating point.
If 16-bit floating point images are given, images will be truncated to 16-bit when written out.

Deep EXR images are partially supported, if they have been saved "flat" with averaged samples.
Most renderers output this by default.

Multi-part EXR images (e.g. using deep samples from deep EXRs, or stereoscopic images) are not supported.

Multilayer EXR images are supported; see :doc:`/inputs/multichannel-exrs`.

If there are additional HDR image formats you would like Altus to support, please contact support.
