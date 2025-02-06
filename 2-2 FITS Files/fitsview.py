#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch
import argparse
from sys import argv

# this is to make the fonts on the plots better
#matplotlib.rcParams['font.family'] = 'STIXGeneral'
#plt.rcParams.update({'font.size':14})
#plt.rc('axes', labelsize=16)
#plt.rcParams.update({'figure.autolayout': True})

# this is to be able to pass in arguments -- like the file name -- to the program
parser = argparse.ArgumentParser(description='Display FITS image.')
parser.add_argument('filename', type=str, help='file name containing data in columns')
parser.add_argument('-hdu', dest='hdu', default=0, type=int, help='HDU to get image data from')
args = parser.parse_args()

# open the FITS file and get the header and image
f = fits.open(args.filename)
hdu = f[args.hdu]
header = hdu.header
image = hdu.data

# print the header (repr will keep the formatting)
print(repr(header))

# get the world coordinate system info from the header
wcs = WCS(hdu.header)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=wcs)

# create a transform for showing the image; see AstroPy docs
transform = AsinhStretch(0.9) + PercentileInterval(99.5)

# show the image
ax.imshow(transform(image), cmap='gray', origin='lower')
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\delta$')
plt.show()



