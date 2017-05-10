How to use the Altus license I just bought
------------------------------------------

After purchasing a license you should receive an email within one business day asking for the MAC address of your license server. We need this information before we can issue you a license.

For all licenses the MAC address that is being used by the system either local or a license server is the one that you should be referencing when you reply to the initial licensing email.

If you purchased a node locked license: this license is locked to the machine you purchased it for. You can run unlimited instances on that machine.

If you purchased a floating license: this license is locked to the server that serves the license. This can be your home machine or a networked machine. This license is limited to the count that was purchased but is much more flexible than the node locked license.

Attached to this article there are the license servers for floating licenses, please download the appropriate license server for your needs.

The license server cannot be run in a VM.

README contents:

In this archive you will find your license file and the floating license server. If you are running your license separate from your workstation that will be operating the Altus you will need to point the server using the system environment variable:

Given your setup there are three ways that you can setup the rlm service.
You can use an ip address for a direct reference
You can use a domain name if you license server has an internal domain name
If you have machines that identify by name you can use machine name.

altus_LICENSE: port@ipaddress or port@domainname or port@machinename

examples: 5053@192.168.1.50 or 5053@optimusprime.innobright.com or 5053@optimusprime

If you do not know how to adjust your environment variables please reference this documentation.

WINDOWS: http://www.computerhope.com/issues/ch000549.htm
LINUX: http://www.cyberciti.biz/faq/set-environment-variable-linux/

The license server runs on port 5053.

This port can be changed in the license, the top line will say:

HOST localhost macid 5053
If you are running the license server on your local machine the windows installer will have set the environment variable at installation to 5053@127.0.0.1 which will point to your local domain when the server is running.

The license file can be stored anywhere, but the best place is to store it in the same directory as the license server.

If you have everything stored in the same place and you have removed the contents of the contained archive you can operate the license server by double clicking the rlm.exe executable. This will start the licnese server and pick up any contained licenses in its directory.

running rlm -h from the command line will provide a help.

-nows turns off the webservice that allows you to check your licenses on port 5054
-ws allows you to specify a different port for the web server
-c allows you to specify a location for the license file
-dlog specify an alternate path for the debug log


