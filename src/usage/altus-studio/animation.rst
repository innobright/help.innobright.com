Animation
=========

Altus can be put into animation mode by specifying the :option:`--start-frame` and :option:`--end-frame` options.

In animation mode, Altus will preserve motion blur, at the expense of increased filter run time and memory usage.
It will also reduce/remediate flicker.

When specifying AOVs, replace in the filename where the frame number would be with either:

 * C-style integer specification, e.g. %04d
 * Hash symbols indicating the padding

For example, if your animation frames were named::

    car.b0.001.exr
    car.b1.001.exr
    car.b0.002.exr
    car.b1.002.exr

You can specify to Altus::

    car.b0.###.exr

or::

    car.b0.%03d.exr

And Altus will be able to find the images on disk.
