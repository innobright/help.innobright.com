What is Altus?
-------------

Innobright’s Altus is the world’s first multi-platform, Monte Carlo render denoising system. We let you generate fast, noisy renders with smaller samples per pixel (SPP) and filter them to produce high quality images & animation. We give you the quality you want, in a fraction of the time.

Altus is a post-processing filter to remove noise from renders created with physically-based Monte Carlo rendering methods.
Most photorealistic renderers use this method of path generation;
see :doc:`/3rdparty` for more information.

It operates in image space with no direct knowledge of scene geometry required.
It does, however require :doc:`two sets of images </inputs/buffers>` and :doc:`feature information in the form of AOVs output from the renderer </inputs/recommended-aovs>`.

.. seealso::

    - :doc:`/inputs/buffers`
    - :doc:`/inputs/recommended-aovs`
