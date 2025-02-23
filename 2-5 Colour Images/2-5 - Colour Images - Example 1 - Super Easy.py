import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch

# open the FITS files; everything is aligned so just grab the image data directly
data_dir = "/home/joe/Data/"
R = fits.open(data_dir + "hst_12193_04_wfc3_uvis_f547m_drz.fits")[1].data
G = fits.open(data_dir + "hst_12193_04_wfc3_uvis_f467m_drz.fits")[1].data
B = fits.open(data_dir + "hst_12193_04_wfc3_uvis_f395n_drz.fits")[1].data

# Now, these images are all weirdly rotated, so we can either rotate (requiring a SciPy call
# to do so) or we can just chop out the centre of the image.  I'm going to do that:
R = R[2000:4000, 2000:4000]
G = G[2000:4000, 2000:4000]
B = B[2000:4000, 2000:4000]

# You should be frequently checking things to make sure everything looks good; let's do that now:
transform = AsinhStretch(0.03) + PercentileInterval(99.3)
fig = plt.figure()
ax = fig.add_subplot(1,3,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='gray_r')
ax = fig.add_subplot(1,3,2)
ax.imshow(transform(G), interpolation='bilinear', cmap='gray_r')
ax = fig.add_subplot(1,3,3)
ax.imshow(transform(B), interpolation='bilinear', cmap='gray_r')
plt.show()

# Like I said, everything works pretty well with this, no real further tweaking required.
# So combine the three images into one RGB image -- think of it as stacking the three images on top
# of each other:

rgb = np.dstack((transform(R),transform(G),transform(B)))

# Let's take a look
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(rgb, interpolation='bilinear', origin='lower')
plt.show()

# Not bad; save it as an image
plt.imsave("m22.png", rgb, origin='lower')
