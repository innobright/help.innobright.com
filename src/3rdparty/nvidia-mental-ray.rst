NVIDIA Mental Ray and Altus
---------------------------

.. warning::

    This article is mostly out of date, but will be updated soon.

The Innobright team has tested Mental Ray in Maya 2015 for scenes that use the mia_material_x_passes shader or Maya materials.

For a still images render to two separate frames.
For example, b0 passes can be rendered with a start frame and end frame of 1.
b1 passes can be rendered with start frame and end frame of 2.

For animations set one render to have the sample lock on and a second render have sample lock off.

For animations you will need to set one render to have the Sample Lock on and a second render to have Sample Lock off. (Render Settings -> Sample
Options -> Sample Lock)

Pass types are as follows:

* Diffuse Material Color → albedo
* Object Normal → normals
* World Position → world position
* Raw Shadow → visibility

More information coming soon.
