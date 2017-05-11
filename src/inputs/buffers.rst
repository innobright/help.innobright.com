Buffers
-------

Altus needs two input images for each scene, which we call call buffers, b0 and b1.

Each of these must be rendered with a different sample seed such that noise varies between images;
we use the difference in noise patterns to remove noise.

Altus needs this variance in noise to effectively remove it from renders. Two buffers are **required**.
