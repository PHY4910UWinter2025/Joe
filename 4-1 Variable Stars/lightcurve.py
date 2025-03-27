import numpy as np
import matplotlib.pyplot as plt
import pandas
from astropy.timeseries import LombScargle

df = pandas.read_csv('1743036620079O-result.csv')
print(df)

print(list(df))

rows_to_keep = df['filter'] == 'ACS_F814W'
print(rows_to_keep)

df = df[rows_to_keep]

date = df['lightcurve_d']
cm = df['lightcurve_cm']
err = df['lightcurve_e']

#plt.errorbar(date, cm, yerr = err, marker='o', linestyle='--', linewidth=0.5, color='black')
#plt.gca().invert_yaxis()
#plt.xlabel('Modified Julian Date (days)')
#plt.ylabel('Correct Magnitude')
#plt.show()

ls = LombScargle(date, cm, err)
freq, power = ls.autopower(minimum_frequency=1, maximum_frequency=2)

#plt.plot(freq, power)
#plt.show()

f = freq[np.argmax(power)]
period = 1/f
print(f'The frequency is {f} and period is {period}')

# make a periodogram
phase = date / period % 1
plt.errorbar(phase, cm, yerr=err, fmt='o', color='black')
plt.errorbar(phase + 1, cm, yerr=err, fmt='o', color='black')
plt.gca().invert_yaxis()
plt.show()

df = pandas.read_csv('1743036620079O-result.csv')
rows_to_keep = df['filter'] == 'ACS_F606W'
df = df[rows_to_keep]

date2 = df['lightcurve_d'][0:-2]
cm2 = df['lightcurve_cm'][0:-2]
err2 = df['lightcurve_e'][0:-2]

ls = LombScargle(date2, cm2, err2)
freq2, power2 = ls.autopower(minimum_frequency=1, maximum_frequency=2)

f2 = freq2[np.argmax(power2)]
period2 = 1/f2
print(f'The frequency is {f2} and period is {period2}')

# make a periodogram
phase2 = date2 / period2 % 1
plt.errorbar(phase, cm, yerr=err, fmt='o', color='black')
plt.errorbar(phase + 1, cm, yerr=err, fmt='o', color='black')
plt.errorbar(phase2, cm2, yerr=err2, fmt='o', color='red')
plt.errorbar(phase2 + 1, cm2, yerr=err2, fmt='o', color='red')

plt.gca().invert_yaxis()

plt.show()
