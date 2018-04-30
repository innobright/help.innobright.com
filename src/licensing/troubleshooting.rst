Troubleshooting
===============

.. warning::

    This article is mostly out of date, but will be updated soon.

Altus is not recognizing it's license file
------------------------------------------

If you cannot get the Altus to recognize the license file keep in mind these things.

If you have node locked license:

1. Are you trying to access the altus from a non local drive. Is your home directory served through LDAP or Active Directory? If so a floating license is probably right for you.
2. A node locked license operating through a home directory served by ldap or active directory will not source correctly as there will be conflicting mac address assignments.

If you have a floating license:

1. Do you have the environment variables set correctly? There is one variables that need to be set: ALTUS_LICENSE should point to the port and hostname/IP address of your RLM server.

If you are using a plugin/integrated version of Altus:

1. Ensure that you bought/recieved the correct product license.  For example, Altus-Studio licenses will not activate the Altus-Redshift integrated plugin.


I bought a license, but Altus is still running in evaluation mode?
------------------------------------------------------------------

This problem can manifest itself in more than one way and depends on floating/node-locked licenses:

If you have floating license:

1. You have not set the ALTUS_LICENSE env variable.
This needs to be set to port#@ipaddress or port#@webaddress or port#@machinename of you license server. If you are using the same machine that you will be running the altus on as your license server this needs to be set to port#@127.0.0.1

The port can be changed in the license file by changing the number on the line with the mac address. The default is 5053

2. You have a firewall blocking incoming/outgoing connections.
To fix this you can either whitelist the programs that need to use the ports, or you can open the ports used by the altus and the license server binary.

3. You have anti virus software enabled.
Given the way that our software uses your hardware by accessing the GPU and or CPU and that the main launching application is a command wrapper to choose either the gui or the correct executable at run time if command line arguments are present you will need to whitelist the executable pieces of altus to work properly.

The only known case of this problem:
Avast

If you have Node-Locked license:

1.  You placed the node-locked file in the wrong directory.  It must be placed in the working directory of the denoiser.  For standalone products (Altus Studio, Altus-CLD) this is the same directory as the executable.  For plugins/integrations it depends on the usage and developers of the program.

2.  If you use ALTUS_LICENSE to point to the license file, make sure it's path is correct.

