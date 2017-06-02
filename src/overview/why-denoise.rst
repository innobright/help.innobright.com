Why denoise?
------------

When rendering using Monte Carlo raytracing, the image will initally be noisy and overtime it will converge to a high quality noiseless image.  Unfortunetly physically based rendering in general can take a long time for a render to converge to a completely noise free image.  The render will need more samples in order for the image to converge and reduce noise.  Unfortunately more samples will take more time to render.  Here is an image showing the noise reduction as you increase the samples per pixel.  


However sample count suffers from diminishing returns.  As sample counts get higher and higher, the difference in quality becomes more and more subtle.  We can visulize the convergence with a graph showing the relationship between noise level and the number of samples taken in a render.


Denoising offers a solution.  Altus Denoiser gives you the quality you want, in a fraction of the time – at least 70% for pre-renders and 40% for final renders. Altus lets you generate fast, noisy renders with smaller samples per pixel (SPP) and filters them to produce high quality images/animation.  Altus also preserves depth of field and motion blur effects. 
