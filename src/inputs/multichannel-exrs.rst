Multichannel and Multilayer EXRs
--------------------------------

Altus supports OpenEXR's mechanism for multilayer (also known as multichannel) images.

When specifying an AOV, simply specify the filename again, followed by ``::``, and then the layer name.

For example::

    pos-0=image.b0.exr::P
    pos-1=image.b0.exr::P

Altus pre-v1.5 has no support for multichannel or multilayer images.
