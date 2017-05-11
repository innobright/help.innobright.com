Chaos Group V-Ray and Altus
---------------------------

.. warning::

    This article is mostly out of date, but will be updated soon.

`vraySettings.dmcs_randomSeed` allows you to set the seed.

V-Ray earlier than 3.1 does support setting seeds.

If you are manually setting the seed in Vray using the vray.dmcs_randomSeed setting make sure to leave enough range between seed 1 and seed 2 for the two buffers.

Vray will render to the max samples required adjusting the seed to be +1 until max.

So if you have a max of 128 and a first seed of 10, at minimum you would need to set the second seed to 139 to avoid an over run of the index.

The better option is to use a large range that cannot be encompassed by your max IE 0 and 50000.

More information coming soon.
