Sample variance
---------------

.. warning::

    This article is mostly out of date, but will be updated soon.

The altus does an internal variance estimate between the two buffers to get an estimated sample variance. When using our variance calculation you can output images with any reconstruction filter that you would like to use.

CAVEAT:
If you can produce a variance directly from the renderer you will need to render with a 1,1 box filter as the output cannot be corrupted by an external reconstruction filter and needs to be the exact information that the renderer outputs as raw pixel information.

(Pre 1.5)

A command line passing variance images would look something like this.

altus -i out -o outdir -b rgb_b0.exr -b rgb_b1.exr -b rgb_var.exr


(Post 1.5)

Variance can be specified using the --rgb-var --pos-var --extra-var flags
