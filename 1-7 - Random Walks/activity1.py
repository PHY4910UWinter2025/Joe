import numpy as np
import matplotlib.pyplot as plt
from phy4910 import *

def move_photon(taumax, zmax, rng):

	x_list = [0]
	y_list = [0]
	z_list = [0]
	
	n = 0
	
	while True:
	
		theta, phi = pick_direction(rng)
		tau = pick_optical_depth(rng)
		
		s = tau/taumax
		
		x = x_list[-1] + s * np.sin(theta) * np.cos(phi)
		y = y_list[-1] + s * np.sin(theta) * np.sin(phi)
		z = z_list[-1] + s * np.cos(theta)
		
		x_list.append(x)
		y_list.append(y)
		z_list.append(z)
		
		n += 1
		
		print(f"Scatter {n}: Photon at {x:.3f}, {y:.3f}, {z:.3f}")
		
		if z < 0:
			# start again
			x_list = [0]
			y_list = [0]
			z_list = [0]
			n = 0
			
		if z > zmax:
			print(f"All done!")
			return x_list, y_list, z_list
		

rng = np.random.default_rng()
x, y, z = move_photon(10, 1, rng)

fig  = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
	
ax.plot(x, y, z, '-')
plt.show()
	
