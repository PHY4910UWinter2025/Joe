from pycbc import catalog
import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time

c = catalog.Catalog(source='GWTC-1-confident')

# Names of mergers in the catalog
print(c.names)

# get data from the first found merger
m = c['GW150914-v3']
print(m.common_name)

h = m.strain('H1')
# print some stuff:
print(f"This time series data is {h.get_duration()} s long, with {h.get_delta_t()} s in between each data point.")
print(f"The sample rate is {h.get_sample_rate()} Hz")
#plt.plot(h.sample_times, h)
#plt.title("Raw strain data for GW150914 H1")
#plt.xlabel("Time (s)")
#plt.ylabel("Strain")
#plt.show()

# let's take a look at the power spectral density, which tells us
# which frequencies in the signal contain the most power
psd = h.psd(4)  # the 4 here is the segment duration -- how long to use for each sample.  Changing it doesn't
                # affect the spectrum that much

plt.loglog(psd.sample_frequencies, psd)

plt.title("PSD from raw strain data")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectrum")
plt.show()

# in terms of signal analysis, the first thing we want to do is whiten the data:
hw = h.whiten(4, 4) # 4 seconds of each sample used in PSD estimate, 4 second duration of filter

psdw = hw.psd(4)
plt.loglog(psdw.sample_frequencies, psdw)

plt.title("PSD from whitened strain data")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectrum")
plt.show()

# compare things with and without whitening:
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(h.sample_times, h)
axs[0,1].loglog(psd.sample_frequencies, psd)
axs[1,0].plot(hw.sample_times, hw)
axs[1,1].loglog(psdw.sample_frequencies, psdw)
plt.show()

# still lots of high-frequency and low-frequency noise, so let's run
# a high-pass filter on the whitened strain:
hf = hw.highpass_fir(30, 512) # lets through frequencies larger than 30 Hz (the 512 is the sample size)
psdf = hf.psd(4)

# compare things with and without filtering:
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(hw.sample_times, hw)
axs[0,1].loglog(psdw.sample_frequencies, psdw)
axs[1,0].plot(hf.sample_times, hf)
axs[1,1].loglog(psdf.sample_frequencies, psdf)
plt.show()

# and a low-pass filter:
hf = hf.lowpass_fir(250, 512) # let's through frequencies smaller than 250 Hz
psdf = hf.psd(4)

# compare things with and without filtering:
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(hw.sample_times, hw)
axs[0,1].loglog(psdw.sample_frequencies, psdw)
axs[1,0].plot(hf.sample_times, hf)
axs[1,1].loglog(psdf.sample_frequencies, psdf)
plt.show()


# well?
plt.plot(hf.sample_times, hf)
plt.title("Whitened and filtered strain data for GW150914 H1")
plt.show()

# what's that around the middle?  Zoom in (we know the actual merger time, so use that)
hz = hf.time_slice(m.time - 0.5, m.time + 0.5)
plt.plot(hz.sample_times, hz)
plt.title("Zoomed in on the signal")
plt.show()

# that's it!
# let's make a fancy Q transform plot; it looks better with just the whitened data
hwz =  hw.time_slice(m.time - 0.5, m.time + 0.5)
times, freqs, power = hwz.qtransform(.001, logfsteps=100, frange=(30, 250))
plt.pcolormesh(times, freqs, power)
plt.yscale('log')
plt.show()
