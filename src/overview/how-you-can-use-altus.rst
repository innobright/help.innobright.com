How you can use Altus
---------------------

Altus Denoiser can be integrated into your production pipeline in several different ways.

Altus CLD:  A command-line denoiser (included in Altus ServerPro) let's you use Altus as a post-process tool.
As a post-process tool, you can create discrete jobs in your render farm automation software to denoise frames after they have completed rendering.
See :ref:`how Altus can integrate with popular render farm queue automation software packages <render-farm-queue-automation-toc>`.

Altus Studio: A graphical user interface that helps you manage your Altus projects with an interactive image viewer.
See :doc:`/usage/gui` for more information.

Several renderers come with Altus integrated.
With a click you can setup renders to generate all the information Altus requires and denoise your renders without additional setup.

If you're a developer, Altus also is available as a Software Development Kit (SDK) that exposes a C++ binary interface to let you pass raw float arrays instead of having to deal with intermedate file formats.
The SDK provides a Dynamic Linked Library (DLL) for Windows and Dynamic Shared Object (DSO) for Linux and macOS for linking directly into your software.
Contact support for more information.
