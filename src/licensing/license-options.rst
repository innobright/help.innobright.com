License Options
---------------

Floating licenses
####################

A floating license allows users to checkout licenses from any machine that can access the license server.

To use floating licenses you must run an RLM server on the same computer running Altus or on another computer elsewhere on your network. Altus will communicate with the license server to checkout/release licenses.


Node-locked licenses
####################

A node-locked license key is locked to a specific computer. You do not need to run a license server if you are using a node-locked license.

To use node-locked licenses with Altus, you must place the license file in the same folder as altus-cli.exe, altus-opencl.exe, etc.  Altus will automatically detect the license file.  