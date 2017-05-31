Multichannel and Multilayer EXRs
--------------------------------

Altus supports OpenEXR's mechanism for multichannel (also known as multilayer) images.

When specifying an AOV, simply specify the filename containing the layer, followed by ``::``, and then the layer name.

For example::

    pos-0=image.b0.exr::P
    pos-1=image.b1.exr::P

Will tell Altus to use the ``P`` layer from images :file:`image.b0.exr` and :file:`image.b1.exr`.

By default, Altus will *not* output layers. Please see :doc:`/usage/output-options`.

Before 1.5, Altus has no support for multilayer/multichannel images.
