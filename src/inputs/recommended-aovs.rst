Recommended AOVs
----------------

More information coming soon.

By default, only the Beauty AOV is filtered.
You can configure Altus to filter other AOVs in various ways; see :doc:`/usage/filtering-aovs` for more information.

Beauty
======

Primary input, typically specified with the ``rgb`` series of options.

Position
========

World point position.
Specified using the ``pos`` series of options.

Normals
=======

Forward-facing normals that preserve bump and displacement information.
Specified using the ``nrm`` series of options.

Albedo
======

Unshaded diffuse texture applied with displacement to the geometry, i.e. thge diffuse reflectance of surfaces with the diffuse component.
Altus prefers the pass with the diffuse component only, with no lighting model applied; the goal is have the constant color on a surface.

In V-Ray, this AOV is typically called "diffuse_filter"; Arnold, "diffuse_albedo"; Redshift "diffuse_color"; Mental Ray "diffuse_material".

Specified using the ``alb`` series of options.

Visibility
==========

Grayscale shadows from all present ight sources in a scene.
Alternatively it can be a black and white binary input defining your keylight only.
It is paramount this AOV does not contain color information.
This pass is sometimes referred to as the "shadow pass".

Specified using the ``vis`` series of options.

Caustics
========

Caustics is an optional input.
If you do not have caustucs, the refractions pass may suffice.

Specular
========

Optional input, but highly recommended if your scene has reflections.
Specified using the ``extra`` series of options.

Other AOVs
==========

Other AOVs you'd like to use for consideration of filtering can be specified using the ``extra`` series of options.

.. seealso::

    - :doc:`../3rdparty`
