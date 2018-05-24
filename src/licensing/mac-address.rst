What is a MAC Address
---------------------

Altus Denosier uses RLM (Reprise licensing software) to license our product.  Our licenses are tied to a computer by a unique identifier called the ``MAC address``.  A MAC address (media access control address) of a device is a unique identifier assigned network interfaces/adapters including Ethernet and Wi-Fi.

Node-locked licenses will be tied to a single computer with the MAC address given to Innobright.

Floating licenses will need to be run on a license server computer.  The MAC address given to Innobright must be for this server.

Most computers will have multiple physical addresses (MAC addresses), look for "Ethernet adapter Local Area Connection" or "Ethernet adapter Wireless Network Connection."  Pick the device that matches your usage.  If you generally use a wireless connection then select the WiFi adapter MAC address.  If you use a wired connection then select the Ethernet adapter MAC address.

A MAC address will be in the following form:  00:00:00:00:00:00 or 00-00-00-00-00-00.  An example address could be: c8:1a:14:56:3a:b6


Find MAC address on Windows
###########################

1) Open your Powershell or Command Prompt (CMD).  

2) Type the command ``ipconfig /all``.  This will print a list of all network devices.  

3) Look for entries that contain "Physical Address".  This will be your MAC address.

.. Note::
    
    There are many guides on finding MAC addresses the internet, for more information try this one:  https://www.laptopmag.com/articles/find-mac-address-windows-10


Find MAC address on Mac
#######################

1) Launch a Terminal from your Applications.

2) Type the command ``ifconfig`` into the terminal and press enter.  This will print a list of devices.  

3) Look for an entry that contains ``ether`` which will be the mac address for that device.

.. Note::
    
    There are many guides on finding MAC addresses the internet, for more information try this one:  http://www.iclarified.com/30929/how-to-find-your-mac-address-in-mac-os-x


Find MAC address on Linux
#########################

1) Open a terminal

2) Type the command ``ifconfig -a``.  This will print a list of all devices with a MAC address.  Eth0 is usually the default device.

3) The MAC address should be under the HWaddr entry of each device.

.. Note::
    
    There are many guides on finding MAC addresses the internet, for more information try this one:  http://www.coffer.com/mac_info/locate-unix.html