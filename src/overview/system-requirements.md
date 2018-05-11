# System Requirements

All versions of Altus Denoiser highly recommend installing OpenCL, if available, for your system. This will result in faster denosing performance. See below.

All versions of Altus Denoiser work on 64-bit computers and operating systems only.

## OpenCL

#### GPU filtering with OpenCL

For NVIDIA GPUs, Please ensure the [latest NVIDIA drivers][nvidia-driver] are installed.

For AMD GPUs, Please ensure the [latest AMD drivers][amd-opencl] are installed.

[amd-opencl]: https://support.amd.com/en-us/kb-articles/Pages/OpenCL2-Driver.aspx

[nvidia-driver]: http://www.nvidia.com/Download/index.aspx?lang=en-us

#### CPU filtering with OpenCL

For filtering on a CPU, we recommend that you [use the AMD OpenCL ICD][amd-icd] or [use the Intel OpenCL ICD][intel-icd], available as part of their APP SDK.

[amd-icd]: https://support.amd.com/en-us/kb-articles/Pages/OpenCL2-Driver.aspx

[intel-icd]: https://software.intel.com/en-us/articles/opencl-drivers


## OS Details
On Windows, Windows 7 or later is supported.

For Linux, we require a Linux distribution that includes glibc 2.12 or later. This includes long-term support distributions such CentOS 6.x or Ubuntu 12.04. Newer distributions will definitely work.

On macOS, macOS 10.9 or later is supported. macOS includes OpenCL so nothing additional needs to be installed.


### Other requirements

For Windows: the [Microsoft Visual C++ Redistributable for Visual Studio 2015][vc2015rt] is required (this is included in Altus' standalone installers).

[vc2015rt]: https://www.microsoft.com/en-us/download/details.aspx?id=48145