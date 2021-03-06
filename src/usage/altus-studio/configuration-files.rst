Configuration Files
===================

Altus Studio can import configuration files, or config file for short.  Altus supports config files that define a the input images, filter settings and output options.


Specify Input Images
--------------------

Config files have a syntax that allow you to specify the path to an AOV:

The following are valid AOV inputs::

    rgb - (beauty)
    pos - (position)
    vis - (visibility/shadow)
    alb - (albedo)
    cau - (caustics)
    extra - (any)
    additional - (any)


Both buffers must be passed when specifing images ::

    rgb-0=image.b0.exr
    rgb-1=image.b1.exr

You only need to pass one when using side-by-side images, make sure to append '-stereo' to the AOV input name ::

    rgb-stereo=image.exr


When using layers, simply specify the filename containing the layer, followed by ``::``, and then the layer name.

For example::

    pos-0=image.b0.exr::P
    pos-1=image.b1.exr::P

Will tell Altus to use the ``P`` layer from images :file:`image.b0.exr` and :file:`image.b1.exr`.


Filter Settings
---------------

Filter settings can also be defined in a config file:

For example::

    rgb-0=image.b0.exr
    rgb-1=image.b1.exr
    pos-0=image.b0.exr::P
    pos-1=image.b1.exr::P
    kc_1 = 0.5
    kf = 0.5
    radius = 15

Denoising Animation
-------------------

Denoising animations can be setup with config files:

For example::

    rgb-0=image.b0.####.exr
    rgb-1=image.b1.####.exr
    pos-0=image.b0.####.exr::P
    pos-1=image.b1.####.exr::P
    start-frame = 0001
    end-frame = 0125
    frame-radius=1

