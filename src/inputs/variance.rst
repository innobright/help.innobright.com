Variance
---------------

Altus relies on variance to determine which areas of the render haven't converged and still contain noisy samples.  There are two types of variance Altus utilizes:  *sample variance* and *buffer variance*.  

**Buffer Variance**

Currently buffer variance can only be calculated from inside Altus by analyzing the differences between the two buffers, b0 and b1.  

**Sample Variance**

Sample variance can be outputed from the renderer and given to Altus.  By default Altus does an internal variance estimate to get the sample variance.  When using our variance estimation you can output images with any reconstruction filter that you would like to use.

If you can produce a sample variance directly from the renderer you will need to render with a 1,1 box filter as the output cannot be corrupted by an external reconstruction filter and needs to be the exact information that the renderer outputs as raw pixel information.

Sample variance can be specified using the --rgb-var --pos-var --extra-var flags

.. Note::

    Versions of Altus 1.5 and earlier have different CLI flags.  Here's an example usage:

    altus.exe -i ./out -o ./outdir -b rgb_b0.exr -b rgb_b1.exr -b rgb_var.exr


Here is an example of a sample variance output from PBRT renderer.  The render's beauty output (left) and the sample variance of the beauty (right):

.. image:: ./input/sample_variance.png
   :scale: 60 %
   :align: center
