Setup
=====

Before using Altus Denoiser, **we recommend that you have either an OpenCL (preferred) Installable Client Driver (ICD) installed**. Altus includes a fallback version that doesn't require OpenCL or CUDA but performance will be limited. See :doc:`/overview/system-requirements`.

On Windows, the installer will install Altus into :file:`C:\\Program Files\\Altus Denoiser\\`.

Inside :file:`C:\\Program Files\\Altus Denoiser\\bin`, :command:`Altus.exe` will open the GUI.
See :doc:`/usage/gui`.

Inside :file:`C:\\Program Files\\Altus Denoiser\\bin`, :command:`altus-cli.exe` is a wrapper executable that will select either a CUDA or OpenCL, or CPU-only compute model for filtering automatically based on what will run best on your computer.
:command:`altus-opencl.exe` and :command:`altus-cuda.exe` are the OpenCL and CUDA compute models of Altus, respectively.
:command:`altus-cpp.exe` is the CPU-only compute model of Altus that will run if OpenCL is not installed.
You can invoke this programs manually rather than through the :command:`altus-cli.exe` wrapper in case you would like to force usage of a particular compute model.

On Linux and macOS, no installer or GUI is available.
The downloads contain the wrapper, OpenCL compute model executable and C++-only versions of Altus.
