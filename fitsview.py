#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch, LinearStretch
import argparse
from sys import argv

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams.update({'font.size':14})
plt.rc('axes', labelsize=16)
plt.rcParams.update({'figure.autolayout': True})

parser = argparse.ArgumentParser(description='Display FITS image.')
parser.add_argument('filename', type=str, help='file name containing data in columns')
parser.add_argument('-hdu', dest='hdu', default=0, type=int, help='HDU to get image data from')
parser.add_argument('-p', dest='percent', type=float, help='Apply a percentile interval to the image')
parser.add_argument('-s', dest='asinh', type=float, help='Apply a arcsinh stretch to the image')
parser.add_argument('-l', dest='log', type=float, help='Apply a log stretch to the image')
parser.add_argument('-g', dest='grid', help='Draw the RA/DEC gridlines', action='store_true')
args = parser.parse_args()

f = fits.open(args.filename)
hdu = f[args.hdu]
header = hdu.header
image = hdu.data

print(repr(header))

wcs = WCS(hdu.header)

fig = plt.figure()
ax = fig.add_subplot(111, projection=wcs)

transform = LinearStretch()
if args.asinh is not None:
	print("Applying arcsinh transform")
	transform += AsinhStretch(args.asinh)
if args.log is not None:
	print("Applying log transform")
	transform += LogStretch(args.log)
if args.percent is not None:
	print("Applying percentile interval transform")
	transform += PercentileInterval(args.percent)

ax.imshow(transform(image), cmap='gray', origin='lower')

if args.grid: ax.coords.grid(color='white', alpha=0.3, linestyle='solid')

plt.show()



