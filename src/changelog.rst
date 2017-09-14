Change Log
==========

This document details changes to Altus.

Altus v1.9.0
------------

Unreleased.

* New flags for passing your renderer's specular pass: :option:`--spc-0`, :option:`--spc-1`, and :option:`--spc-stereo`. Before 1.9, you can pass the specular AOV by the "extra" series of options. Beginning with 1.9, we prefer you use these named options instead. Configurations earlier than 1.9 will work with 1.9, but configurations with 1.9 and later will not work earlier versions of Altus.
* Multiple output images: Altus will be able to denoise and save AOVs as indivudual files in addition to a multilayer image.
* Altus will now run in GPU mode by default.  We are replacing --gpu with --cpu.  All functionality will be the same but the defaults are switched.
* Ignore Alpha:  When filtering images its sometimes prefered to ignore the alpha channel.
* The CUDA compete model of Altus is no longer publically distributed. OpenCL is faster and more reliable. If you need the CUDA version of Altus for some reason (e.g. if you're using an old NVIDIA GPU that does not support OpenCL), please contact support.
* The different executables for altus (:command:`altus-cli`, :command:`altus-cpp`, :command:`altus-opencl`, and :command:`altus-cuda`) have been merged into one: :command:`altus-cli`. The one binary will internally select the best version of Altus that can run.
* Device selection has been completely reworked, and you will need to adjust the platform id and device id you are using, as what worked before Altus 1.9 will not work with Altus 1.9 or later. Platform 0, device 0 is reserved for the fallback version of Altus, so what was platform 0 before is now platform 1. GPUs as reported by :option:`--query-devices` will be listed by how much memory they have, in descending order.
* The fallback version of Altus, implemented in C++-only and previously available as :command:`altus-cpp`, is now integrated into Altus and no longer distributed separately. It will run when Altus cannot run on a faster device. To manually run the fallback, you can pass a platform and device index of 0.
* Intel GPU support is enabled for all platforms (previously only available for macOS, or custom builds from Innobright). Altus will only pick an Intel GPU if there are no other GPUs on the system. A side effect of this, the Intel GPU will report having "0 GiB" memory. You can manually select your Intel GPU by finding out its platform and device indices using the :option:`--query-devices` option, and then passing it to :option:`--platform-id` and :option:`--device-id` respectively.

Altus v1.8.5
------------

Released on 13th July.

* Improved support for negative and irregular data windows.  Data windows that differ across b0 and b1 are supported now, although not recommended.
* Faster previews for animations.  Disabled temporal filtering when denoising animations in preview mode.
* Update the layer selection menu in the GUI.
* Bug fix in the CLI where arguments passed were incorrectly parsed.

Altus v1.8.4
------------

Released on 30 May 2017.

* New :option:`--tile` flag enabling tiling. Altus now supports internally spliting the image into smaller pieces that will be processed individually, and remerged together at the end. This is done independently of either the renderer's or OpenEXR's notion of tiling. This is useful if the image is too big to fit into the memory of your device (e.g. GPU). While it will take longer to denoise, you will be able to use the fastest hardware you have and process larger images.
* New :option:`--tile-size` flag lets you set the maximum tile size.
* New :option:`--firefly` flag will enable the firefly suppressor.
* Fix GUI bug where selecting images will convert the format specifier of all other images filenames, sometimes converting an already converted filename.
* GUI paths will now show the "real" path when editing the textfield. The textfield will be converted upon edit finish. This way there is no uncertainty on what the path is to the image you orignally selected.
* GUI settings menu has been updated to reflect the new features: firefly suppressor and tiling.
* Fixed linking issue on macOS: zlib was dynamically being linked when it should have been linked statically. On some systems, the dynamically-linked executable may not have ran; the statically-linked executable should run anywhere.

Altus v1.8.3
------------

Released on 10 May 2017.

* Fix bug introduced in 1.8.2 with animation format specifiers in filenames. Parsing input filenames in animations will now work as before in 1.8.1. Output filenames will now replace "#" and "%04d" format specifiers for animation.
* Altus for Linux is now built with GCC 7.1.
* Altus for macOS now runs on macOS 10.9 (Mavericks) and later. Previous versions of Altus required 10.11 (El Capitan) or later.
* Upgraded RLM to RLM 12.2.

Altus v1.8.2
------------

* New :option:`--additional-0`, :option:`--additional-0`, and :option:`--additional-s` flags let you specify an AOV that will be denoised, but not used in consideration of filtering RGB. Note: as of 1.8.2, additional AOVs will not be saved unless :option:`--filter-aov` is specified.
* Black AOV inputs are bypassed to save time.
* The denoised position output, before 1.8.2, was normalized to [0,1], as this was needed internally. It is now restored to its original range.
* Minor GUI updates to support new features.
* Issues with single channel images and layers have been resolved. Please contact us if you still have issues.
* Altus for Linux is now built with GCC 6.3.

Altus v1.8.1
------------

* Fix crash w/ watermark insertion when running in evaluation mode
* Fix GUI issue where it was possible to click on the option menu even if it was hidden.
* Increase performance of preview quality by avoiding some extra calculations.
* Display a warning if no variance is detected between buffers: i.e. if you pass the same image to buffer 0 and buffer 1, you'll get a warning.
* Altus will now attempt to auto-detect single-channel images & layers. Previously, users had to name the channel.
* Filtering did not occur properly when in :option:`--quiet` mode: fixed.

Altus v1.8.0
------------

* Altus 1.8 now supports filtering at different quality levels: "preview" and "production".
* New ``--quality={preview, production}`` flag:  filter parameter to select if the filter should run in full quality (production) or a faster quality (preview)
* New ``--filter-aov={prefiltered, preview, production}`` flag:  Altus 1.8 now supports filtering AOVs at various quality levels.  The first mode 'prefiltered' allows Altus to save "prefiltered" versions of all AOVs used. These saved features will only go through the first stage of filtering so quality may be less than the complete filter process.  The second mode 'preview' allows Altus to filter the AOVs at the "preview" quality level.  Similarly the third mode 'production' will filter the AOVs at the highest "production" quality level.  Altus will only save filtered versions of AOVs that have been passed via the various AOV flags (i.e. nrm-0/nrm-1, vis-0/vis-1, etc).  This can be combined with --preserve-layers so that any layer not included in filtering AOVs will be preserved in the output image.
* Changed ``--preserve={layers, prefiltered}`` flag, to :option:`--preserve-layers` flag.  This flag lets Altus preserve all layers from a multi-layer EXR given via rgb-0/rgb-1.  The layers will be saved into the output image.  This flag is compatible with :option:`--filter-aov`.
* The settings window for Altus 1.8 GUI is now a slide-out window.
* If Altus 1.8 encounters a licensing error on startup (e.g. you specified a license in ALTUS_LICENSE, but Altus was unable to check out a license), Altus will now quit with an error. Previously, Altus would continue and insert the watermark. If you'd like the old behavior, please use :option:`--force-continue`.

Altus v1.7.1
------------

* Altus 1.5.4 through 1.7.0 would sometimes output artifacts when used with the Intel OpenCL ICD. This is now fixed. While the Intel ICD is faster, if you encounter problems/artifacts we recommend you use the AMD OpenCL ICD.
* Bug fix for GUI first-time registration menu where the menu would pop up each time the GUI is opened.

Altus v1.7.0
------------

* New `--force-continue` flag: Altus' behavior with respect to errors has significantly changed. Previous versions of Altus tried to recover from warnings or errors (i.e. a missing frame in an animation). From v1.7.0 onward, Altus now exits when an error or warning is encountered. Use this flag to behave like Altus 1.6 and earlier, where Altus will try to recover. Attempting to recover may yield black frames (please read Altus' warnings and error messages!); Altus' new behavior will make Altus display an error and quit so you can fix problems.
* With Altus 1.7, we are now using RLM 12.1. On Windows, RLM 12.1 is included in the installer and can be installed as an option. For Linux and macOS, you will need to download the licensing package from our support portal. You may need to upgrade your local RLM server to RLM 12.1.
* Altus 1.7 introduces a new GUI that removes clutter and streamlines the process of running Altus without knowing how to use the CLI. The GUI is beta, but still significantly better than the GUI we were shipping in Altus 1.6 and earlier. Please try it out and report bugs to Innobright support!
* Altus 1.7 ships with a significantly improved "wrapper" executable, "altus-cli". It will automatically select the best version of Altus your system can run.
* Altus for OpenCL is now the preferred version of Altus. Previously, Altus for CUDA was the version of Altus that was selected if you were running on the GPU. Altus for CUDA will only run if your GPU does not support OpenCL (i.e. an old NVIDIA GPU). There is no performance benefit for using Altus for CUDA, so please use the OpenCL version.
* There is now a C++-only version of Altus. This version of Altus will run without OpenCL being installed. However, performance is degraded compared to the OpenCL version of Altus. If you can setup OpenCL, please use the OpenCL version Altus.
* Altus for CUDA will now autoselect the GPU with the most memory, instead of the first GPU.
* New `--preserve={layers, prefiltered}` flag: In the first mode 'layers' Altus can now preserve all layers from a multi-layer EXR given via rgb-0/rgb-1. You do not need to specify which layers you want preserved. The second mode 'prefiltered' allows Altus to save "prefiltered" versions of all AOVs used in consideration of filtering RGB. These saved features will only go through the first stage of filtering so quality may be less than the complete filter process. Altus will only save prefiltered versions of AOVs that have been passed via the various AOV flags (i.e. nrm-0/nrm-1, vis-0/vis-1, etc). This flag has a negligible impact on speed but requires extra memory. Prefiltered AOVs may be useful if you use EXRs Altus de-noises with a compositing program such as Nuke, and is a fast alternative to running Altus on each AOV you want de-noised. Currently, there is no way to save both all AOV layers and prefiltered AOVs; please contact Innobright support if you'd like this feature.
* World position (pos-0, pos-1, and pos-stereo) is now an optional AOV, but highly recommended for the best quality denoising with Altus. You will receive a warning if you do not provide world position. Previously, Altus would quit with an error.
* Verbose mode has been set to true by default.  Use '-q' or '--quiet' to turn off verbose mode.
* New `--kf` flag: filter parameter that controls the sensitivity of all candidates, and the second pass filter, to feature differences. Lowering the kf value may help fine detail preservation and decrease smoothing in the final image. (default 0.6)
* New `--kc_4` flag:  filter parameter that controls the sensitivity of the second pass filter to color differences. A higher value leads to more agressive filtering. (default 0.45)
* Deprecated `--kc_3` flag: kc_3 has been deprecated and no longer does anything. You'll receive a warning if you try to use it.
* Altus for OpenCL and CUDA will now let you select which device to use. This is useful if you have a system with multiple GPUs. Use the `--query-devices`, `--device-id`, and `--platform-id` flags to select devices.
* New `--query-devices` flag: This enumerates the available compute devices which can run Altus. Run Altus with this flag then use device-id and platform-id to select which device to use.
* New `--device-id` flag: Select which device to run Altus on. The Altus for OpenCL will list CPU and GPU devices. The Altus for CUDA only lists GPUs. The C++-only version of Altus has no concept of devices and this flag will do nothing.
* New `--platform-id` flag: Specify the OpenCL platform the device is on. Must be used in conjunction with device-id. This flag is for OpenCL only; it has no effect on Altus for CUDA or the C++-only version of Altus.
* For licensing, the environment variable `altus_LICENSE` (mixed case) has been deprecated; please use `ALTUS_LICENSE` instead (all capitals). The former will continue to work but you will receive a warning.
* `--renderer` now does something for "vray": if your renders were made with Chaos Group's V-Ray renderer, Altus now provides slightly better output if you specify `--renderer=vray`. Optimizations for more renderers is coming soon.
* From now onwards, side-by-side imagery is referred to as such; previously, Altus referred to side-by-side imagery as "stereo". Calling the feature "stereo" is misleading, as Altus does not support actual stereoscopic imagery, where the camera may appear in two different places in each frame. Altus expects the camera to be in the same place in each frame. The CLI options continue to be called "stereo" for the time being, but the GUI refers to these images as "side-by-side".

Altus v1.6.1
------------

* Serious bug with stereo processing fixed

Altus v1.6.0
------------

* In preparation for Altus 2.0, configuration and command-line interface have changed. Your Altus 1.5 configurations will continue to work with Altus 1.6; your 1.6 configurations will not work on 1.5.
* The recommended 12 AOVs (rgb, pos, cau, nor, alb, vis) must now be explicitly specified on the command-line, and not be given as "extra" AOVs. See the usage document for 1.6 . Unfortunately, you will not receive a warning if you do not update how you pass these AOVs, but Innobright strongly suggests you do if you want the best filtering quality possible.
* Short-hand flags for specifying AOVs have been deprecated. Please do not use `-r0`, `-r1`, `-rs`, `-rv`, `-p0`, `-p1`, `-ps`, `-pv`, `-x0`, `-x1`, `-xs`, or `-xv`.
* `--renderer` flag: Altus now suggests you specify your renderer to get the best quality. In 1.6, this does not do anything, but will in later versions. Please start using it now.
* If you have multiple GPUs, Altus 1.5.x may have been selecting the GPU with the least amount of memory, when it should have been selecting the GPU with the most amount of memory. This is fixed.
* Altus now displays an estimate of how long the filtering process will take. Displayed in verbose mode.
* Memory improvements: Altus 1.6 now uses slightly less RAM.
* Cleaner program output. Altus' verbose mode is now somewhat structured, and both easier to read and undertand.
* Fix typo of the Guerilla render
* In Altus 1.5.x, OpenMP runtime was not statically linked on Linux. You would get an error about being unable to load a library if you did not have it or the correct version installed. It is now statically linked in Altus 1.6.

Altus v1.5.4
------------

* Dev021: User facing debug mode
* Dev032: SDK and API v0.1
* Dev035: Frontend optimizations
* Dev036: Backend Optimizations

Altus v1.5.3
------------

* Dev007: Image processing filter size. Known issue that images are processed based on image size and not based on data area.
* Dev006 Addressed workgroup/power of 2 restrictions.
* Add: Version flag for versions going forward.

Altus v1.5.0
------------

* Dev001: Stereo rendered image input : IE side by side renders. Added handling of side by side stereo imagery.
* Dev002: Layered exr implementation. Now accept layered EXRs as input can read layers and use internally to do filter calculations. Layers are stated as such image.exr::layername.
* Dev003: Memory optimization and buffer management. Cleanup of code and memory managemnet and buffer management in system wide memory.
* Dev005: CUDA implementation being addressed. CUDA implementation moved out of BETA status and into main tree will continually included in all releases moving forward.
* Dev014: Extra AOV handling. added functionality to pass unlimited numbers of aovs to the altus only stipulation is that the flags -x0|--extra-0 -x1|--extra-1 have to be consistently passed in order for the system to properly recognize inputs.
* Dev017: Alpha is written regardless of inclusion in input. Alpha was being written if origin image did not have one fixed now origin image determines if the alpha is written.
* Dev018: Layered EXRs sort bottom layer by default. Layered EXRs were sorting the RGB layer(unamed) to the bottom of the stack as a default behaviour. Now fixed RGBA is always read as top layer.
* Dev019: Maxwell renderer stores shadows pass in alpha channel, sort channel properly based on flag. Maxwell shadow passes are stored in the Y channel OpenEXR throws an exception when the RGBA is empty on pixel read fixed behavior to sort Y cahnnel to the front RGB channels on load if RGB is empty.
* Dev020: Adjust animation handling on ingest to handle all padding. Adjusted animation to read @@@@ for padding and %04d for padding this can now be specified for input and output allowing for multiple padding types to be read off of disk.
* Dev024: Internal file handling structure rewrite. Restructuring of internal data handling.
* Dev028: Config files that point to non existent locations crash without output. Config files crashed of the path did not exist, we now print an error.
* Dev031: Adjust the counter to have better output when processing files: animation specifically. Less cumbersome more informative counter and percentage printed to stdOUT. Reports total time and time per frame as well as percentage based on passes and total frame count.

Altus v1.4.0
------------

* Dev030 Addressed memory leak when handling animations. Animations are processed and the frames that are used for temporal consideration are not properly dropped from memory after use.
* Dev023 Addressed Over smoothing artifacts. Quality and feature preservation improvement.
* Dev022 Addressed UX with better error handling. Adjusted handling non existent input to generate better error output and to inform the user of the aov or input that failed.

Altus v1.3.0
------------

* Dev006 Addressed portrait images are no longer a restriction. Portrait images in gpu process top square of data due to work group/power of 2 restrictions.
* (-33)context creation crash addressed CL context -33 should not be raised any longer.
* Local work group was being populated incorrectly causing error handling issues.
* Device selection and fallback added, If gpu is not suitable or produces an error will fall back to the cpu to perform filtering process.
* Compiled with OpenEXR 2.2 and boost 1.55 as static libraries on linux Dependencies other than GCC should no longer be an issue.
* Now preserves the Data and Display window data from the original header.

Altus v1.2.0
------------

* Removed required argument true of --Verbose flag.
* For animation, set default frame radius to 1.
* Fixed Dev002 of Altus v 1.1 Alpha filtering now is handled separately with RGB filtering.
* Added more descriptive OpenCL error reporting.
* Fixed Dev001 of Altus v1.1 Tested and handled superluminous values up to 6,000 in the filtering process.
* Modifed animation function so that if --StartFrame and --EndFrame are given the same frame number, the neighboring frames are taken into account in the averaging.
* Edited the help menu information.
* Added the header information of rgb pass EXR input into filtered output.
* Lightened, randomized, and reduced watermarks.
* Modified final image write to use float type rather than half type.
* Modified final image write to use tiled EXR writing scheme.
* Added support for CentOS 6.x
* CentOS dependency list OpenEXR, OpenCL (intel or AMDSDK), Boost 1.55
* CentOS updates were pulled from the epel repository.
* Discontinuation of Maya Script support: Maya Arnold Script and Maya Vray Script will be offered as is in the downloads section, but will no longer be supported.

Altus v1.2 GUI
--------------

* Updated verbose flag argument for text printed out under GUI debug.
* Added stderr to debug output.

Altus v1.1
----------

* Verbose Flag: Added verbose flag for user interaction and understanding of what is going on.
* Flag Fixes fixed various flags:
* k_red: replaced with kc_1
* k_grn: replaced with kc_2
* k_blu: replaced with kc_3
* --StartFrame: repaired long name
* --EndFrame: repaired long name
* Help Flag -h added help also comes down when no input is present
* String Parsing: animation parsing: any given input will be read as though padded to 4. I.e. 001, 00001, 1, 01, 000001
* Added output so user knows that a license is either invalid or has been dropped.


