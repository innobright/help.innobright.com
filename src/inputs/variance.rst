Variance
========

Altus relies on variance to determine which areas of the render haven't converged and still contain noisy samples.  There are two types of variance Altus uses:  *sample variance* and *buffer variance*.

Buffer Variance
---------------

Buffer variance is calculated internally by Altus by analyzing the differences between the two buffers, b0 and b1.

Sample Variance
---------------

Some renderers can output sample variance, and this can be given to Altus.
If not provided. Altus will construct an estimated sample variance.

If you can produce a sample variance directly from the renderer you will need to render with a 1,1 box filter as the output cannot be averaged through an external reconstruction filter. It must be the exact information that the renderer outputs.

Here is an example of a sample variance output from PBRT renderer.  The render's beauty output (left) and the sample variance of the beauty (right):

.. image:: ./input/sample_variance.png
   :scale: 60 %
   :align: center

Sample variance can be specified using flags in CLI::

    --rgb-variance=<path to exr image>
    --pos-variance=<path to exr image>
    --nrm-variance=<path to exr image>
    --cau-variance=<path to exr image>
    --vis-variance=<path to exr image>
    --extra-variance=<path to exr image>
    --additional-var=<path to exr image>


Sample variance can be specified using a config file::

    rgb-variance=<path to exr image>
    pos-variance=<path to exr image>
    nrm-variance=<path to exr image>
    cau-variance=<path to exr image>
    vis-variance=<path to exr image>
    extra-variance=<path to exr image>
    additional-variance=<path to exr image>
