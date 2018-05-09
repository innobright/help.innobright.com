Basic usage
============


Overview
########
.. include:: ../3rdparty/renderer-overview.rst


This guide will explain how to denoise a given scene and adjust some filter settings.  Start by downloading the demo scene we will be using:  <link>


Demo Contents
-------------

The demo scene zip contains two folders of images: b0 and b1.  Each folder was rendered with a different seed to ensure that b0, b1 have different noise patterns.  Each folder contains all the render passes (AOVs) recommended by Innobright: :doc:`/inputs/recommended-aovs`.  We will be using these contents to denoise the beauty images.  

One of the beauty render (b0):

.. image:: ./basic-usage/b2.png
   :scale: 100 %
   :align: center



Denoise the Demo Scene:
##########################

To start lets denoise the demo scene using default Altus settings.  First check that Altus has been setup properly, see: :doc:`/usage/setup`.

Import images into Altus
########################


Using the Import Wizard
=======================

This is the easiest way to import into Altus.  Here you’ll select either “Import Folder” or “Import Images”. From there select the desired files you want to import for denoising. Once the files are selected hit “Open” and the files that were selected will be shown with their AOV’s.  Organize the AOV’s so they match up correctly (this is indicated with a green check-mark over each pass).  Once everything has the green check-mark you can then hit “Finished”.

Setting up the Config File
==========================

Another way to import images into Altus is by using a config file.  Config files (.cfg) allow us to define the image paths along with any filter settings.  In this guide we will be using a config file.  For more info see :doc:`/inputs/config-files`.


First to define in a config file are the paths to the b0, b1 renders.  Lets start with the beauty:

For example::

    rgb-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior####.exr
    rgb-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior####.exr

Now we can add the position pass and normals::

    pos-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior####.exr
    pos-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior####.exr

    nrm-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    nrm-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr

Finally, we rendered out an AOV for reflections.  Lets add that as an extra AOV to Altus::

    extra-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    extra-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr

Now that we defined all the input images, we should specify where the output will be saved.  There are a couple options for that, we will append ''--out-dir'' to the config file::

    out-dir=C:\tmp\output


All together the final config file should look like::

    rgb-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior####.exr
    rgb-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior####.exr
    pos-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior####.exr
    pos-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior####.exr
    nrm-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    nrm-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    extra-0=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 1\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    extra-1=M:\Client_Files\Dante McCoy - animation\animation altus\Pass 2\Ipswich Cycle Park_11_Club house interior_Geometric normals####.exr
    out-dir=C:\tmp\output


Running Altus 
--------------

Now that we have a config file, we can use it to run Altus.  To upload a config file, select the file drop down, select “Load” (Config file) and locate the desired config file you are wanting to import.

To run Altus; first open a CMD/shell window and start Altus by typing the command in this form: <path/to/Altus.exe> --config=<path/to/config.cfg>

Denoise with Altus
##################

To begin::
You have successfully uploaded your files and placed the AOV’s so they all have a green check-mark. The next step is to begin the process of denoising and this is achieved by locating the “Start Denoiser” button on the bottom right corner, click the button and Altus should begin to filter.  Once it has completed the output image will be saved in the directory we specified with out-dir.

My denoised result:

.. image:: ./basic-usage/b2altus.png
   :scale: 100 %
   :align: center


Basic Filter Settings:
######################

Once you are comfortable running Altus, you can experiment with the filter settings.  See also :doc:`/usage/advanced-usage` for more options.  The essential basic settings are as follows:


Window Radius
-------------

Specifies the dimension of the filtering window.
The default of 10 means that the origin pixel, plus 10 pixels up, down, left, and right will be considered.
That is, the filtering window will be a 21x21 box.

Decreasing the radius will result in faster denoising, but may leave more noise behind.

Increasing the radius will result in significantly slower denoising, possibly removing more noise at the risk of "over-smoothing" an image.

Generally, reducing the radius will be more noticeable visually than increasing it.


``--kc_1``
----------

This value scales how much color (beauty) will influence the small (detail) kernel blur.  Low values will expose more detail at the risk of leaving noise behind.

``--kc_2``
----------

This value scales how much color (beauty) will influence the large (edge) kernel blur.  Low values will expose more detail at the risk of leaving noise behind.

``--kc_3``
----------

This value is not used; it is present for legacy compatibility.

``--kc_4``
----------

Controls removal of residual noise.

``--kf``
--------

Controls the influence of feature AOVs (e.g. position, normals, etc) for all kernel sizes.
Generally controls the trade-off between preserving edges and fine detail.  Low values will expose more detail at the risk of leaving noise behind.



Denoise Again With Adjusted Filter Settings
###########################################

Now that we understand the settings, lets try to change the settings on the image we denoised above.  Still within the main interface, lets change the kc values and window radius on the input panel:

    kc_1 = 0.25
    kc_2 = 0.25
    kf = 0.3
    radius = 6

And the denoised output:

.. image:: ./basic-usage/b2altus.png
   :scale: 100 %
   :align: center


Final Notes
###########

Congratulations on completing the basic usage tutorial for Altus Denoiser!  If want to tweak Altus to perfection, see: :doc:`/usage/advanced-usage`.

.. Note:: 

    Explore our help site for more information on Altus and using Altus with third party software.  Here are some places to get started:

    For information on :doc:`/usage/denoising-aovs`.

    For information on :doc:`/usage/animation`.

    For information on :doc:`/usage/output-options`.

    To use Altus with other software see: :doc:`/3rdparty`.