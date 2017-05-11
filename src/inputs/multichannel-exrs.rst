Multichannel and Multilayer EXRs
--------------------------------

Altus supports OpenEXR's mechanism for multilayer (also known as multichannel) images.

When specifying an AOV, simply specify the filename containing the layer, followed by ``::``, and then the layer name.

For example::

    pos-0=image.b0.exr::P
    pos-1=image.b1.exr::P

By default, Altus will *not* output layers. Please see :doc:`/usage/preserving-layers`.

Altus pre-v1.5 has no support for multichannel or multilayer images.
