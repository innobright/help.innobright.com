Using floating licenses on a Client Computer
--------------------------------------------

First, ensure that the RLM license server has been started correctly.  Visit here for more info on setting the ``RLM License Server`` :doc:`/licensing/setting-up-rlmd`.

Connecting to the license server
################################

Workstations must be configured so that it can find the license server and checkout licenses.  You do this by defining an environment variable ``ALTUS_LICENSE``.

Given your setup there are three ways that you can set the enviroment variable.
    1) You can use the license server's ip address for a direct reference
    2) You can use a domain name if your license server has an internal domain name
    3) If you have machines that identify by name you can use machine name.

ALTUS_LICENSE: port@ipaddress or port@domainname or port@machinename

.. Examples:: 
    
    5053@192.168.1.50 or 5053@optimusprime.innobright.com or 5053@optimusprime

.. Note:: 
    If you do not know how to adjust your environment variables please reference this documentation.
    
    WINDOWS: http://www.computerhope.com/issues/ch000549.htm

    LINUX: http://www.cyberciti.biz/faq/set-environment-variable-linux/