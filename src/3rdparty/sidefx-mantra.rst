Denoise SideFX Mantra renders with Altus
----------------------------------------

.. warning::

    This tutorial is for older versions of Altus; configuring Corona and Altus are significantly easier now.



Mantra ROP Create a mantra ROP and set the render engine to Physically Based Rendering.  The default sampling parameters are excellent for use with Altus.  Use the lowest Pixel Samples possible to capture texture and surface details.  For 1920x1080 renders, 5x5 is an excellent compromise between quality and render time for use with Altus. 
 
[img]

Secondary bounces beyond three produce little to no improvement for most scenes.  Secondary volume bounces are quite expensive. 

[img]

Altus requires at minimum an RGB and a position plane.  For optimal noise-reduction, Innobright recommends also providing normal, visibility, and albedo planes.  Additional planes may be provided if needed for additional features not prevalent in the recommended AOV. 
 
[img]

The albedo AOV in Mantra is named “direct_reflectivity” and is of type vector.  The “direct_shadow” AOV of type vector can be used as the visibility plane. 

[img]

Altus requires two renders with different samples seeds. To generate the extra render and minimize user error, make a reference copy of the Mantra ROP 

[img]

Break expressions on Sample Lock and Random Seed and set values to checked and 1 respectively. 
 
[img]