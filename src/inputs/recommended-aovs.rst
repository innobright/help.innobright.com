Recommended AOVs
----------------

Physically-based rendering works by measuring various aspects about how light interacts with objects in a scene.
Renderers calculate all these measurements internally to create samples, and allow you to export information about these measurements as something called arbitrary output variables (AOVs).

Altus' quality is superior to generic denoisers because we work with AOVs, using the knowledge contained within them to do things like preserve texture detail and edges.

We recommend **seven** AOVs, though some are optional. Almost all physically-based Monte Carlo renderers can output these AOVs, though they may not be named quite the same, or semantically be what we need. If you're wondering which AOVs your renderer generates that correspond to the ones below, please check :ref:`renderers-toc`.

If you can't get these seven, you can still get reasonable quality by providing beauty, position, and normals.
If your scene does not have certain elements such as caustics or specular, you can omit them.
While you can provide all the AOVs your renderer can output, this will make Altus consume more time and memory, and usually for diminishing gains.
Innobright's research has found the seven discussed below maximize the trade-off between quality and speed across a wide range of images.

By default, only the Beauty AOV is filtered.
You can configure Altus to filter other AOVs in various ways; see :doc:`/usage/denoising-aovs` for more information.



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

Unshaded diffuse texture applied with displacement to the geometry, i.e. the diffuse reflectance of surfaces with the diffuse component.
Altus prefers the pass with the diffuse component only, with no lighting model applied; the goal is have the constant color on a surface.

In V-Ray, this AOV is typically called "diffuse_filter"; Arnold, "diffuse_albedo"; Redshift "diffuse_color"; Mental Ray "diffuse_material".

Specified using the ``alb`` series of options.

Visibility
==========

Grayscale shadows from all present light sources in a scene.
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
