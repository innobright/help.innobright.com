Common errors
=============

.. warning::

    This article is mostly out of date, but will be updated soon.

Zero CL buffer error
--------------------

This error is only passed by the OpenCL version.

The Zero CL Buffer error is passed when the device that is being used to filter has run out of accessible memory. This Error will most likely happen on a graphics card that is being used for display and other loads.

Currently we select the largest card in the system to process images and if that card is the one that is being used for graphics display and other functions then the end result can potentially be a race for resources. If you get this error please check the memory consumption of your graphics devices in a tool like msi afterburner to make sure that it is not being over susbscribed.
