Advanced usage
==============

``--radius`` or ``-r``
----------------------

Specifies the dimension of the filtering window.
The default of 10 means that the origin pixel, plus 10 pixels up, down, left, and right will be considered.
That is, the filtering window will be a 21x21 box.

Decreasing the radius will result in faster denoising, but may leave more noise behind.

Increasing the radius will result in significantly slower denoising, possibly removing more noise at the risk of "over-smoothing" an image.

Generally, reducing the radius will be more noticeable visually than increasing it.

``--renderer`` or ``-R``
------------------------

Sets various optimized options and does additional processing based on which renderer from which AOVs were generated.

The processing as of 1.8 is as follows:

* ``vray``: Set optimized kc_1, kc_2, and kf.

This option is not required, but highly recommended.
Valid options are:

* ``generic``
* ``pbrt``
* ``cycles``
* ``arnold``
* ``vray``
* ``maxwell``
* ``redshift``
* ``prorender``
* ``mantra``
* ``octane``
* ``mentalray``
* ``modo``
* ``iray``

The default is ``generic``, which as of 1.8 is the same as ``pbrt``.

``--frame-radius`` or ``-f``
----------------------------

When Altus is in animation mode, this controls how many neighboring frames will be considered when doing temporal filtering.
It is a radius, so the default value of 1 means 3 images will be considered: the current frame, the frame before, and the frame after.

If you are getting ghosting because of intense motion, consider setting this to 0.

Setting this parameter greater than 1 can help reduce flickering, but exponentially increases denoising time.

``--quiet`` and ``--verbose``
-----------------------------

By default, Altus is always in verbose mode.
Status and information messages will be printed in this mode.
The ``--verbose`` flag is present for legacy compatibility, but otherwise does nothing.

If you would only like to see warnings and errors, you can make Altus much more quiet by passing the ``--quiet`` option.

``--query-devices``, ``--platform-id``, and ``--device-id``
-----------------------------------------------------------

Some systems may have multiple OpenCL ICDs and devices.
For example, systems with multiple GPUs.

``--query-devices`` will let you see Altus' view of the devices that are available.

Given the information provided by ``--query-devices``, you can pass the information to ``--platform-id`` and ``--device-id`` to manually select which OpenCL ICD and device you would like Altus to use.

``--force-continue``
--------------------

Normally, if Altus encounters any error, it will quit (with caveats; see :doc:`/known-issues`).

With this option, Altus will attempt to recover.
This is useful several situations.
For example:

* if an animation frame is missing on disk, instead of quitting Altus will output a black frame and do it's best to continue on with the remaining frames of the animation
* if a licensing error occurs, insert the watermark instead of quitting.

This flag is intended for debugging purposes only and should not be used in production.


``--kc_1``
----------

This value scales how much color (beauty) will influence the small (detail) kernel blur.

``--kc_2``
----------

This value scales how much color (beauty) will influence the large (edge) kernel blur.

``--kc_3``
----------

This value is not used; it is present for legacy compatibility.

``--kc_4``
----------

Controls removal of residual noise.

``--kf``
--------

Controls the influence of feature AOVs (e.g. position, normals, etc) for all kernel sizes.
Generally controls the trade-off between preserving edges and fine detail.


``--tile``
----------

Altus can internally divide, denoise, and combine tiles in order to denoise large images that wouldn't otherwise fit in memory.
Generally this feature is more useful when using GPU's to denoise since GPU's typically have a small amount of VRAM.  This causes large images to be impossible to denoise on GPU unless using tiling.

``--tile-size``
---------------

Controls the max size of the internal tile.  The tile-size given is an upper bound, the actual tile size will always be less than the tile-size in each axis.  If the tile-size is larger than the full image then it is clamped to the size of the image.

``--firefly``
-------------

Enables the firefly suppressor.  This will detect and reduce the spread of high energy pixels.  By default it's turned off.  Minor performance hit to enable.
