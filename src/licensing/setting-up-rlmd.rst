Setting up a new RLM licensing server
-------------------------------------

Installing the RLM licensing server
###################################

Download the license server bundle for `Windows`__, or `Linux`__. Extract the files from the zip and move them to a folder on your license server machine. The location of the folder is not important.

__ http://shop.innobright.com/wp-content/uploads/2018/03/RLM-12.1-Windows-Licensing-Package.zip
 
__ http://shop.innobright.com/wp-content/uploads/2018/03/RLM-12.1-Linux-Licensing-Package.zip


Add your Altus license file
###########################

Place the Altus Denoiser license file in same folder that contains the RLM license server files (This is the folder that contains the rlm executable).

Starting the RLM license server
###############################

The license server can be run from the command-line, or can be set up to run as a windows service so that it automatically starts when you boot your server. Running from the command-line is convenient for testing, but we recommend running the RLM server as a service once it's been confirmed to be working.


Using the license server
########################

Workstations must be configured so that it can find the license server and checkout licenses.  You do this by defining an environment variable ALTUS_LICENSE. 

Given your setup there are three ways that you can set the enviroment variable.
	1) You can use an ip address for a direct reference
	2) You can use a domain name if your license server has an internal domain name
	3) If you have machines that identify by name you can use machine name.

ALTUS_LICENSE: port@ipaddress or port@domainname or port@machinename

.. Examples:: 
	
	5053@192.168.1.50 or 5053@optimusprime.innobright.com or 5053@optimusprime

.. Note:: 
	If you do not know how to adjust your environment variables please reference this documentation.
	
	WINDOWS: http://www.computerhope.com/issues/ch000549.htm

	LINUX: http://www.cyberciti.biz/faq/set-environment-variable-linux/
