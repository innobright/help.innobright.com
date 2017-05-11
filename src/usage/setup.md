Setup
=====

On Windows, the installer will install Altus into C:\Program Files\Altus Denoiser\ (by default).

Before using Altus, we recommend that you have either an OpenCL (preferred) Installable Client Driver (ICD) installed, or if filtering on an NVIDIA GPU, a recent NVIDIA driver with CUDA. Altus includes a fallback version that doesn't require OpenCL or CUDA but performance will be limited. See :doc:`/overview/system-requirements`.

Inside C:\Program Files\Altus Denoiser\bin, Altus.exe will open the GUI.

Inside C:\Program Files\Altus Denoiser\bin\, altus-cli.exe is a wrapper executable that will select either a CUDA or OpenCL, or CPU-only compute model for filtering. opencl.exe and cuda.exe are the OpenCL and CUDA filter programs, respectively.

On Linux and macOS, no installer or GUI is available.
The downloads contain the wrapper, OpenCL compute model executable and C++-only versions of Altus.
