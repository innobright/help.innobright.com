How to use the Altus license I just bought
------------------------------------------

When purchasing a license you will need the MAC (media access control) address of your license server (floating licenses) or computer (node-locked licenses). We need this information before we can issue you a license.  You should reference the MAC address that is being used by the local computer or by the license server.  For information on finding the MAC Address visit: https://kb.netgear.com/1005/How-to-find-a-MAC-address

Node-Locked License
###################

If you purchased a node locked license: this license is locked to the machine you purchased it for. You can run unlimited instances of Altus Denoiser on that machine making it great for multi-GPU.

Node locked licenses can be installed in two ways.  The recommended way is with Enviroment Variables as it will work with Standalone and integrated/plugins.  If you only use Altus' standalone products (Altus-CLD and Altus-Studio) then the 2nd method will be faster.  


1) Enviroment Variables
=======================

Visit your OS page for more information on setting up your ``ALTUS_LICENSE`` enviroment variable to install the node-locked license.

Setting up :doc:`/licensing/node-locked-licenses-windows` for Windows.

Setting up :doc:`/licensing/node-locked-licenses-mac` for Mac.

Setting up :doc:`/licensing/node-locked-licenses-linux` for Linux.


2) Standalone Products
======================

Node-locked licenses for standalone products can be installed by placing the node-locked license in the working directory of the Altus executables.  On most setups that will be the same directory as Altus executable.  By default, on Windows it's C:/Program Files/Altus Denoiser/bin/


Floating License
################

If you purchased a floating license: this license is locked to the server that serves the license. This can be the same machine or a networked machine. This license is limited to the count that was purchased but is much more flexible than the node locked license and allows you run share licenses across computers on the same network.

There are two steps to install a floating license:

.. Note::
	The license server cannot be run in a VM.

1) License Server
=================

In order to use a floating license you must first setup an RLM License server to keep track and serve license requests to networked computers.  The license server can either be installed on the same computer running Altus, or a computer on the same network.

For information on setting up the license server visit: :doc:`/licensing/setting-up-rlmd`.

For information on using an existing RLM license server visit: :doc:`/licensing/existing-rlmd`.

For information on using RLM's web interface visit: :doc:`/licensing/rlm-web-interface`.


2) Client Computer
==================

The client computer is the machine that will run Altus Denoiser.  It connects to the license server to request a license.  Altus denoiser will look for an ``ALTUS_LICENSE`` enviroment variable that points to the port and ip address of the computer running as the license server.

Visit our OS page for more information on setting up your enviroment variable:

Setting up ``Enviroment Variable`` in Windows :doc:`/licensing/floating-licenses-windows`.

Setting up ``Enviroment Variable`` in Mac :doc:`/licensing/floating-licenses-mac`.

Setting up ``Enviroment Variable`` in Linux :doc:`/licensing/floating-licenses-linux`.
