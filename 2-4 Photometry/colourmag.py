import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import PercentileInterval
from astropy.stats import sigma_clipped_stats
from astropy.wcs import WCS
from astropy.nddata.utils import Cutout2D
from photutils.detection import IRAFStarFinder
from photutils.aperture import CircularAperture, aperture_photometry

file = fits.open('hst_12311_02_wfc3_uvis_f275w_ibj202_drc.fits')['SCI']#SCI or 1
image_f275 = file.data
print(image_f275)

#slice the image
cutout = Cutout2D(image_f275, (3000,3000), 2000)
image_f275_cut = cutout.data

print(np.max(image_f275_cut))

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) 
transform = PercentileInterval(99.5)
ax.imshow(transform(image_f275_cut), cmap='gray_r', origin='lower')
plt.show()

mean, median, std = sigma_clipped_stats(image_f275_cut, sigma=3) 
print(f"Mean = {mean}\nmedian = {median}\nstandard deviation = {std}")

#Find all the stars
finder = IRAFStarFinder(fwhm=3.0, threshold=10.*std)  
stars = finder(image_f275_cut - median)

#Compute the aperture
positions = np.transpose((stars['xcentroid'], stars['ycentroid']))
apertures = CircularAperture(positions, r=4.)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) 
ax.imshow(transform(image_f275_cut), cmap='gray_r', origin='lower')
apertures.plot(color='red', lw=1.5, alpha=0.5)
plt.show()

phot = aperture_photometry(image_f275_cut, apertures)
flux = phot['aperture_sum']
mags_f275 = 25.0 - 2.5 * np.log10(flux)




file = fits.open('hst_12311_02_wfc3_uvis_f814w_ibj202_drc.fits')['SCI']#SCI or 1
image_f814 = file.data
print(image_f814)

#slice the image
cutout = Cutout2D(image_f814, (3000,3000), 2000)
image_f814_cut = cutout.data

print(np.max(image_f814_cut))

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) 
transform = PercentileInterval(99.5)
ax.imshow(transform(image_f814_cut), cmap='gray_r', origin='lower')
plt.show()
"""
mean, median, std = sigma_clipped_stats(image_f814_cut, sigma=3) 
print(f"Mean = {mean}\nmedian = {median}\nstandard deviation = {std}")

#Find all the stars
finder = IRAFStarFinder(fwhm=3.0, threshold=10.*std)  
stars = finder(image_f814_cut - median)

#Compute the aperture
positions = np.transpose((stars['xcentroid'], stars['ycentroid']))
apertures = CircularAperture(positions, r=4.)
"""

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) 
ax.imshow(transform(image_f814_cut), cmap='gray_r', origin='lower')
apertures.plot(color='red', lw=1.5, alpha=0.5)
plt.show()

phot = aperture_photometry(image_f814_cut, apertures)
flux = phot['aperture_sum']
mags_f814 = 25.0 - 2.5 * np.log10(flux)


UI = mags_f275 - mags_f814
plt.plot(UI, mags_f275, '.')
plt.gca().invert_yaxis()
plt.show()






