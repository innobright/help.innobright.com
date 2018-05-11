Animation
=========

Altus Studio can be put into animation mode during import using the Project Wizzard, or by specifing a config file with animation enabled, or by enabling "animation" from Altus Studio after importing.

In animation mode, Altus uses temporal filtering to preserve motion blur, at the expense of increased filter run time and memory usage.
It will also reduce/remediate flicker.

To ensure your animation was properly imported check the start-frame and end-frame settings in the animation bar located on the bottom of the screen.  Altus will display a caution indicator on passes where it couldn't find the image on disk.  The common cause of this error is an incorrect start-frame, which makes Altus unable to find the sequence's frames.


Import Animation from Config file
---------------------------------

Altus Studio can load config files that specify animation settings.  The following are examples of animation settings in a config file:

When specifying AOVs you must also let Altus know what section of the filename is the frame number.  To indicate this, replace the section of the filename where the frame number would be with either:

 * C-style integer specification, e.g. %04d
 * Hash symbols indicating the padding

For example, if your animation frames were named::

    car.b0.001.exr
    car.b1.001.exr
    car.b0.002.exr
    car.b1.002.exr

You can specify to Altus::

    car.b0.###.exr

or::

    car.b0.%03d.exr

Then Altus will be able to find the images on disk.

The start-frame and end-frame can also be specified in the config file along with frame-radius, which is the number of neighboring frames on each side that Altus will use to denoise.  A frame-radius of 2 will make Altus import 2 previous frames, and 2 next frames, along with the current frame.

The following are examples of all animation related settings::

    start-frame=100
    end-frame=201
    frame-radius=2

