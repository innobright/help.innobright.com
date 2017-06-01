Variance
========

Altus Denoiser relies on variance to determine which areas of a render contain noise that must be removed.
There are two types of variance Altus uses: *buffer variance* and *sample variance*.

Buffer Variance
---------------

Buffer variance is calculated internally by Altus by analyzing the differences between the two input buffers, b0 and b1.

Sample Variance
---------------

Some renderers can output sample variance, and this can be given to Altus.
If not provided. Altus will construct an estimated sample variance.

For renderers that can output sample variance, you must render it with a 1,1 box filter.
The output cannot be averaged through an external reconstruction filter.

Here is an example of a sample variance output from PBRT renderer.
The render's beauty output (left) and the sample variance of the beauty (right):

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
