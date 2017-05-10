Image formats
-------------

For the best quality possible, Altus operates on `high-dynamic range (HDR) images`__.
The only HDR format currently supported is `OpenEXR`__ format.

__ https://en.wikipedia.org/wiki/High-dynamic-range_imaging
__ http://openexr.com/

OpenEXR images can be 16-bit floating point (half) or 32-bit floating point (float) images.
8-bit integer images are not supported.

Altus does NOT support JPEG, PNG, WebP, etc images.
Altus' denoised output will be severely degraded by using lossy image formats like these as input.

All of Altus' internal processing is done in 32-bit floating point.
If 16-bit floating point images were given, images will be truncated to 16-bit when written out.

Deep EXR images are partially supported.

If there are additional HDR image formats you would like Altus to support, please contact support.
