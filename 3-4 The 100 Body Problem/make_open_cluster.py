from nbody import Particle, System
import numpy as np

# options
outfile = "open_cluster_ic.txt"
r_max = 5.0
N = 100
G = 0.004301550874918987

rng = np.random.default_rng()

particles = []

for i in range(N):

	# pick mass first
	m = rng.lognormal()
	
	# then positions
	pos = -r_max + 2.0 * r_max * rng.random(3)
	while np.sum(pos**2) > 1.0:
		pos = -r_max + 2.0 * r_max * rng.random(3)
		
	# or
	# theta = np.arccos(1 - 2.0 * rng.random())
	# phi = 2.0*np.pi* rng.random()
	# r = r_max * rng.random()
	# x = ...
	# y = ...
	# z = ...
	
	vel = [0,0,0]
	
	p = Particle(m, pos, vel)
	
	particles.append(p)
	
s = System(particles, G = G)
s.write(outfile)
	
	
	
