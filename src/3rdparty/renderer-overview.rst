Altus Denoiser uses information from two rendered images to generate a high quality denoised image. This guide will explain how to setup and render the inputs to Altus. There are two concepts that Altus uses to generate denoised outputs:

AOVs (Arbitrary Output Variables) provide a way to render any arbitrary shaded component into different images. Typically renderers will only produce a final color for each pixel of the image (known as the beauty pass, or RGB pass), but you can break out renders into their component parts such as indirect lighting, diffuse color, reflections, shadows, mattes, etc. and save them as files individually or layers as part of a multichannel/multilayer EXR. See :doc:`/inputs/recommended-aovs` for more information.

Two images (called buffers) must be generated for each image. It's important that each buffer is rendered with a different sample seed so that they will have unique noise patterns. The variance between the two buffers is what Altus uses to remove noise. Without variance, there is not enough information to remove noise. See :doc:`/inputs/buffers` for more information.

For information on how to run Altus once the correct inputs have been created see :doc:`/usage`.
