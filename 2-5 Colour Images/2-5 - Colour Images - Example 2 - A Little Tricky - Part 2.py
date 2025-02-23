import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch, MinMaxInterval

# Read in that data file
rgb = np.load("ring_data.npy")

# What does this image look like?
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
transform = AsinhStretch(0.3) +  PercentileInterval(99.5)
ax.imshow(transform(rgb), interpolation='bilinear')
plt.show()

# That's ... okay, but there's improvements to be made.  Split the data back into three images:
print("Splitting image ...")
R, G, B = np.dsplit(rgb, 3)

# Chop off the edges, those are NaNs
R = R[500:4500, 500:4500]
G = G[500:4500, 500:4500]
B = B[500:4500, 500:4500]

# There's still more NaNs that are causing the centre of the stars to be black.  Here's how we can fix that:
# Step 1 - transform the images so that the data goes from 0 to 1
print("Fixing NaNs ...")
minmax = MinMaxInterval()
R = minmax(R)
G = minmax(G)
B = minmax(B)
# Step 2 - make all NaNs equal to 1 (the maximum)
R = np.nan_to_num(R, nan=1)
G = np.nan_to_num(G, nan=1)
B = np.nan_to_num(B, nan=1)

# Now we can make each image have the same median value by dividing; this will ensure 
# each rgb channel has around the same amount
print("Dividing by median ...")
R = R / np.median(R)
G = G / np.median(G)
B = B / np.median(B)

# Finally, we can transform each channel separately however we want
transformR = AsinhStretch(0.1) + PercentileInterval(99.6)
transformG = AsinhStretch(0.1) + PercentileInterval(99.9)
transformB = AsinhStretch(0.1) + PercentileInterval(99.6)

R = transformR(R)
G = transformG(G)
B = transformB(B)

# And save as an rgb image
print("Packing as rgb ...")
rgb = np.dstack(((R),(G),(B)))
plt.imsave("southern_ring.png", rgb, origin='lower')
