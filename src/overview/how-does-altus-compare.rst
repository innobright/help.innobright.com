.. role:: red

How Does Altus Compare?
-----------------------

Innobright’s Altus is the world’s first multi-platform, Monte Carlo render denoising system. We let you generate fast, noisy renders with smaller samples per pixel (SPP) and filter them to produce high quality images & animation. We give you the quality you want, in a fraction of the time.


.. This will change the background color of a table cell. Used to highlight Altus features.
.. role:: gbg

.. raw:: html

   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
   <script>
     $(document).ready(function() {
       $('.gbg').parent().addClass('gbg-parent');
     });
   </script>
   <style>
      .gbg-parent {background-color:#D5FFCB;}
   </style>


Features
========

+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| **FEATURE**                 |:gbg:`Supported in Altus`| **V-Ray Denosier**             | **Corona Denosier**              | **RMan 22 Denosier**           |
+=============================+=========================+================================+==================================+================================+ 
| Standalone                  |        **Yes**          |              Yes               |             Yes                  |             Yes                |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| GUI Option                  |        **Yes**          |              Yes               |              No                  |             No                 |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| Works with ANY PBR Renderer |        **Yes**          |              No                |              No                  |             No                 |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| HW acceleration             |        **Yes**          |              Yes               |              No                  |             Yes                |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| GPU Support                 |        **Yes**          |              No                |              No                  |             No                 |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| Animation Support           |        **Yes**          |              No                |              No                  |             Yes                |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| Firefly Remover             |        **Yes**          |              No                |              Yes                 |             No                 |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| Filter AOVs along with RGB  |        **Yes**          |              Yes               |              Yes                 |             Yes                |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 
| Fast/Preview Mode           |        **Yes**          |              No                |              No                  |             No                 |
+-----------------------------+-------------------------+--------------------------------+----------------------------------+--------------------------------+ 


Performance 
===========

.. Note::
    These numbers were collected on a single computer with the following specs:

    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+
    | **OS**     | **CPU**                            | **RAM Memory**           | **GPU**                  |  **VRAM**                |
    +============+====================================+==========================+==========================+==========================+
    | Windows    |   Intel Core i7-4770 @3.10GHz      |      12GB                |  NVIDIA GeForce GTX 960  |    4GB                   |
    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+

+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------------+
|                    |                                                                         Elapsed Time (mm:ss)                                                                       |
+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------------+
| **Image Size**     |:gbg:`Altus Preview (GPU)`| :gbg:`Altus Production (GPU)`    |   **V-Ray Denosier**             | **Corona Denosier**              | **RMan 22 Denosier**           |
+====================+==========================+==================================+==================================+==================================+================================+
| 3000x3000          |         00:53            |              05:20               |             4:04                 |            2:49                  |         11:52                  |
+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------------+
| 1920x1080          |         00:11            |              00:59               |             1:26                 |            0:41                  |         02:36                  |
+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------------+
|  960x540           |         00:03            |              00:15               |             0:07                 |            0:16                  |         00:44                  |
+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------------+


Quality vs PBR Denoisers
========================

This section contains comparisons to other denoisers. Each scene was rendered in Renderman, V-Ray, Corona and then denoised using their integrated denoisers.
Then after rendering, all required AOVs were exported and used to denoise the beauty pass with Altus Denoiser.  All denoisers were used with default settings unless otherwise specified.

Renderman
#########
.. figure:: ./images/Altus-Renderman_diff_closeUp.png
   :scale: 150 %
   :align: center

   Left: Altus Denoiser   Right: Renderman Denoiser

.. Note::

   Quality Differences: Renderman tends to leave blotchy shadows in low light situations.  This becomes apparent if exposure is adjusted to clearly see the differences.  The shadows behind the rim, under the tire and inside the handle all appear blotchy.



Corona
######

.. figure:: ./images/Altus-Sponza_diff_corona.png
   :scale: 150 %
   :align: center

   Left: Altus Denoiser   Right: Corona Denoiser

.. Note::

   Quality Differences: Corona left residual noise in shadowed areas.

V-Ray
####

.. figure:: ./images/Altus-Vray_coronell_diff.png
   :scale: 150 %
   :align: center

   Left: Altus Denoiser   Right: V-Ray Denoiser

.. Note::

   Quality Differences: V-Ray denoiser has trouble preserving detail in reflections.  V-Ray image has blurry reflections on the cube and blurry refractions on the sphere.



Quality vs Generic Film Denoisers
=================================

.. Warning::  

    The following results are from two generic image-space denoisers which operate only on the RGB image and cannot include any AOV/feature information.  Often these denoisers are intended to clean up noise from film.  This means that these denoisers will be fast but will produce worse quality outputs.  All such comparisons will be unfair but are included for reference. 

Neat-Image
##########

.. figure:: ./images/Altus-NeatImage_diff.jpg
   :scale: 150 %
   :align: center

   Neat-Image settings used: 100% reduction, 150% noise level

.. Note::

   Quality Differences: NeatImage denoiser was unable to remove the bright noise surrounding the ceiling light, even after using more extreme filter parameters. 

Revision FX DE:Noiser
#####################

.. figure:: ./images/Cornell_Rev_Denoiser.png
   :scale: 150 %
   :align: center

   DE:Noiser settings used:  Variational reduction type, Spatial Threshold 50%, Spatial Radius 3.


.. Note::

   Quality Differences: Revision DE:noiser was unable to smooth out noise over the light without over blurring the rest of the image.


Download links
==============

    .. Note:: 
        
        Zip of all three above mentioned scenes: Austin Martin, Cornell Box, Sponza.  Each output from Altus, V-Ray, Corona and Renderman are included uncompressed and in exr format.
            https://drive.google.com/file/d/0B1qS9hgD_Sn2V0ZHR3V4YmN4MGc/view?usp=sharing  (392M)


Full Performance Table
======================

This section contains performance/timing information that was collected on multiple computers with a range of specs from slow to fast.  Each scene was rendered in Renderman, V-Ray, Corona and then denoised using their integrated denoisers.
Then after rendering, all required AOVs were exported and then used to denoise the beauty pass with Altus Denoiser.


Austin Martin Scene:
####################    

.. Note::

    This scene was rendered at 3000x3000 and then denoised.  This computer can be categorized as slow.  Computer Spec:

    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+
    | **OS**     | **CPU**                            | **RAM Memory**           | **GPU**                  |  **VRAM**                |
    +============+====================================+==========================+==========================+==========================+
    | Windows    |  Intel Core i7-4510U @2.0 - 2.6GHz |      8GB                 |  NVIDIA GeForce GTX 860M |    1GB                   |
    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+

+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------+---------+
|                                                                                            Elapsed Time (h:mm:ss)                                                                           |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+
|      Scene Name          | **Image Size**     |:gbg:`Altus Preview (GPU)`| :gbg:`Altus Production (GPU)`    |Renderman 22 Denoiser   |        V-Ray Denoiser     |       Corona Denoiser    |
+==========================+====================+==========================+==================================+========================+===========================+==========================+
|       Austin Martin      | 3000x3000          |         0:01:15          |            0:06:21               |       0:20:42          |        0:21:45            |       0:13:15            |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+


Cornell Box Scene:
##################

.. Note::

    This scene was rendered at 1920x1080 and then denoised.  This computer can be categorized as fast.  Computer Spec:

    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+
    | **OS**     | **CPU**                            | **RAM Memory**           | **GPU**                  |  **VRAM**                |
    +============+====================================+==========================+==========================+==========================+
    | Windows    |Intel Xeon CPU E5-1650 v3 @ 3.50GHz |      32GB                |NVIDIA GeForce GTX TITAN  |    8GB                   |
    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+

+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------+---------+
|                                                                                            Elapsed Time (h:mm:ss)                                                                           |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+
|      Scene Name          | **Image Size**     |:gbg:`Altus Preview (GPU)`| :gbg:`Altus Production (GPU)`    |Renderman 22 Denoiser   |        V-Ray Denoiser     |       Corona Denoiser    |
+==========================+====================+==========================+==================================+========================+===========================+==========================+
|       Cornell Box        | 1920x1080          |         0:00:08          |            0:00:27               |       0:00:56          |        0:00:42            |       0:00:20            |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+



Sponza Scene:
#############

.. Note::

    This scene was rendered at 950x540 and then denoised.  This computer can be categorized as mid-range.  Computer Spec:

    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+
    | **OS**     | **CPU**                            | **RAM Memory**           | **GPU**                  |  **VRAM**                |
    +============+====================================+==========================+==========================+==========================+
    | Windows    |     Intel Core i5-4460 @3.20GHz    |      12GB                |  NVIDIA GeForce GTX 760  |    2GB                   |
    +------------+------------------------------------+--------------------------+--------------------------+--------------------------+


+--------------------+--------------------------+----------------------------------+----------------------------------+----------------------------------+--------------------------+---------+
|                                                                                            Elapsed Time (h:mm:ss)                                                                           |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+
|      Scene Name          | **Image Size**     |:gbg:`Altus Preview (GPU)`| :gbg:`Altus Production (GPU)`    |Renderman 22 Denoiser   |        V-Ray Denoiser     |       Corona Denoiser    |
+==========================+====================+==========================+==================================+========================+===========================+==========================+
|       Cornell Box        |  950x540           |         0:00:05          |            0:00:18               |       0:02:16          |        0:00:09            |       0:00:16            |
+--------------------------+--------------------+--------------------------+----------------------------------+------------------------+---------------------------+--------------------------+
