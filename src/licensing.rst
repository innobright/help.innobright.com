Licensing
---------

.. toctree::
    :maxdepth: 2

    licensing/how-to-use-license
    licensing/setting-up-rlmd
    licensing/existing-rlmd
    licensing/rlm-web-interface
    licensing/evaluation
    licensing/virtual-machines
    licensing/node-locked-licenses
    licensing/troubleshooting

You can `buy a license for Altus from our Website`__. Without a license, Altus will insert a watermark into any filtered image.

__ https://www.innobright.com/product/altus-purchase-options/

We are using `Reprise License Manager (RLM)`__ for licensing, and support floating licenses only.

__ http://www.reprisesoftware.com/products/software-license-management.php

Floating licenses require you setup a license server on your property, locked to a MAC address. To setup a licensing server, follow the instructions for `downloading & installing RLM from our Website`__. When you use the installer on Windows, the RLM licensing package is an option in the installer.

__ https://support.innobright.com/kb/faq.php?id=6

After setting up the RLM license server, remember to set the `ALTUS_LICENSE` path to point to the license server. Note that the format is `port@hostname`; the port comes first, then an '@' character, then the hostname.
