import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch
from reproject import reproject_interp

# open the FITS files; this time we need the HDUs to reproject the images
hduR = fits.open("jw02733-o001_t001_nircam_clear-f356w_i2d.fits")[1]
hduG = fits.open("jw02733-o001_t001_nircam_clear-f212n_i2d.fits")[1]
hduB = fits.open("jw02733-o001_t001_nircam_clear-f187n_i2d.fits")[1]

# Here's what I mean about not being aligned; I'll stack the images using imshow and transparency
R = hduR.data
G = hduG.data
B = hduB.data

transform = AsinhStretch(0.03) + PercentileInterval(99.3)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='Reds')
ax.imshow(transform(G), interpolation='bilinear', cmap='Greens', alpha=0.5)
ax.imshow(transform(B), interpolation='bilinear', cmap='Blues', alpha=0.5)
plt.show()

# okay, we'll reproject the G and R images so they match the B (the G is pretty close but has a slightly
# different resolution, so we might as well do it as well)

G, footprint = reproject_interp(hduG, hduB.header)
R, footprint = reproject_interp(hduR, hduB.header)

# okay we should check to see if they're okay, plot them again
transform = AsinhStretch(0.03) + PercentileInterval(99.3)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='Reds')
ax.imshow(transform(G), interpolation='bilinear', cmap='Greens', alpha=0.5)
ax.imshow(transform(B), interpolation='bilinear', cmap='Blues', alpha=0.5)
plt.show()

# So, that took WAY too long to do -- once the images are aligned, we should save it and write
# another program to read it in and create the image
rgb = np.dstack((R, G, B))
np.save("ring_data.npy", rgb)

