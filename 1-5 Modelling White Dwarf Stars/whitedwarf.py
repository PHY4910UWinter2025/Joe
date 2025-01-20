import numpy as np
import matplotlib.pyplot as plt
from phy4910 import ode_rk4

# A. Let's build a nonrelativistic model of a white dwarf!

#
#  Part 1 - Solve Lane-Emden
#
n = 1.5
def f(eta, varrho, z):
	return z
	
def g(eta, varrho, z):
	return -varrho**n - 2*z/eta

eta, varrho, z = ode_rk4(0.0001, 4, 0.0001, 1, 0, f, g)

positivevalues = varrho > 0
eta = eta[positivevalues]
varrho = varrho[positivevalues]
z = z[positivevalues]

plt.plot(eta, varrho)

plt.show()

eta_s = eta[-1]
print(f"The surface is at {eta_s}")

# Part 2 - Calculating m

m = np.trapz(varrho**n * eta**2, eta)

print(f"The dimensionless mass is {m}")

# Part 3 - Converting to real units
# Part a
rho_c = 4.045E5
k_nr = 3.166E12
G = 6.6743E-8
M = 1.989E33 # in grams

lam = np.sqrt((n+1) * k_nr * rho_c**((1-n)/n)/4/np.pi/G) 

print(f"The radial scale factor is {lam/1e5} km")

# Part b
r = lam * eta 
rho = rho_c * varrho**n 

plt.plot(r/1e5, rho)
plt.show()

print(f"The radius of the white dwarf is {r[-1]/1e5} km")

# Part c
m_dwarf = 4*np.pi*rho_c*lam**3*m

print(f"The mass of the white dwarf is {m_dwarf/M} solar masses")







