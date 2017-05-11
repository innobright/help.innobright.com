# System Requirements

All versions of Altus highly recommend installing OpenCL, if available, for your system. See below.

On Windows, Windows 7 or later is supported.
The [Microsoft Visual C++ Redistributable for Visual Studio 2015][vc2015rt] is required (this is included in Altus' installer).

[vc2015rt]: https://www.microsoft.com/en-us/download/details.aspx?id=48145

For Linux, we require a Linux distribution that includes glibc 2.12 or later.
This includes long-term support distributions such CentOS 6.x or Ubuntu 12.04.
Newer distributions will definitely work.
Our release binaries are statically linked, and include libraries such as zlib, OpenEXR, and libgcc and libstdc++, so you do not need to install anything additional on Linux  other than OpenCL.

On macOS, macOS 10.9 or later is supported. macOS includes OpenCL so nothing additional needs to be installed.

## OpenCL

### GPU filtering with OpenCL

For filtering on a GPU, please install the [latest NVIDIA drivers][nvidia-driver] for NVIDIA GPUs or latest drivers for AMD GPUs, depending on what device you have.

Altus for Windows and Linux does not support Intel GPUs (please contact Innobright support if you would like such a build); Altus for macOS does, and will use the OpenCL ICD included with macOS.

[nvidia-driver]: http://www.nvidia.com/Download/index.aspx?lang=en-us

### CPU filtering with OpenCL

For filtering on a CPU, we recommend that you [use the AMD OpenCL ICD][amd-opencl], available as part of their APP SDK. It will run on both Intel and AMD CPUs, albeit at a signficant performance loss.

[amd-opencl]: http://developer.amd.com/tools-and-sdks/opencl-zone/amd-accelerated-parallel-processing-app-sdk/

There are known issues with the [Intel OpenCL ICDs][intel-icd]. While significantly faster if you have supported hardware, if you encounter artifacts Innobright recommends you use the AMD ICD instead of the Intel ICD.

[intel-icd]: https://software.intel.com/en-us/articles/opencl-drivers

## CUDA

Please make sure you have the latest NVIDIA drivers installed.
