Node-locked licenses on Linux
=============================

Node-locked licenses lock your usage of Altus to a computer with a specific MAC address.
If the MAC address changes, you will no longer be able to use your license.

Node-locked licenses, unlike floating licenses, let you run as many copies of Altus as you'd like on that computer, only limited by the computing resources you have available (e.g. node-locked licenses are useful if you have multiple GPUs in a single computer).
You do not need to run the RLM Licensing Server if you have a node-locked license.

To use your node-locked license, you can do one of two things: place the license in the working directory (usually the same folder as Altus' executables), or set an environment variable pointing to the license.

Place license into same folder as Altus' executables
----------------------------------------------------

.. Note::

    This will only work for STANDALONE products of Altus Denoiser (Altus-Studio and Altus-ServerPro).  If you bought an integrated version of Altus (Redshift,Arnold,Nuke) then skip to the enviroment variable section below.

Place your license file in the same folder as the other Altus executables.

Altus will automatically find your node-locked license.


Set the ALTUS_LICENSE environment variable
------------------------------------------

If you wish to store your licenses in a separate directory from Altus, you can use the :envvar:`ALTUS_LICENSE` environment variable to point to fully-qualified path to the license file so Altus can find it.

For example, if you place your licenses into :file:`C:\\Licenses`, and your license is called :file:`altus.lic`, then the contents of your environment variable must be ``C:\Licenses\altus.lic``.

Some programs may require a restart to reread the enviroment variables.
