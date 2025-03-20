import numpy as np

M = 1.989e30 # solar mass in kg
L = 3.086e16 # parsec in m
s_in_year = 60*60*24*365.25
G = 6.674e-11

T = np.sqrt(1/G * L**3 / M)
print(T)


# I want units of velocity of 1 km/s
#V = 1000  # m/s

#T = L / V  # this will be our time unit, in seconds

G = 6.674e-11 * 1/(L**3) * M * T**2

V = L/T

print(f"Time units are {T:.4g} s ({T/s_in_year / 1e6:.4f} million years)")
print(f"Velocity units are {V:.4g} m/s ({V/1000:.4f} km/s)")
print(f"G = {G}")
