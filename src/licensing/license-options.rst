License Options
---------------

1) Floating licenses
####################

A floating license allows users to checkout licenses from any machine that can access the license server.  Each instance of Altus will use one license while it's running and then return the license once it's finished.  

.. Note::

    To use floating licenses you must run an RLM server on the same computer running Altus or on another computer elsewhere on your network. Altus will communicate with the license server to checkout/release licenses.


2) Node-locked licenses
#######################

A node-locked license key is locked to a specific computer. You do not need to run a license server if you are using a node-locked license.  A single license for a computer will activate all instances of Altus run on that computer.

.. Note::

    An RLM license server is NOT needed for node-locked licenses.



Integrated Altus Denoiser Licenses
----------------------------------

Altus licenses are separated into two categories: ``Standalone`` and ``Integrated``.  Each category comes in node-locked and floating varieties.

Standalone Denoiser
###################

Altus-Studio (``altus-studio``) and Altus-ServerPro (``altus-pro``) licenses activate our standalone products.


Integrated Denoiser
###################

If you use Altus Denoiser integrated into Redshift, or our plugins for Arnold (BETA), Nuke (BETA) then you will need to purchase their license type ie ``altus-redshift`` licenses.  These licenses will only activate the integrated/plugin version of Altus.