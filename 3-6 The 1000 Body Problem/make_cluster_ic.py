from nbody import *
import numpy as np

# options
outfile = "open_cluster_ic.bin"
vel_max = 5 / 0.0656
r_max = 5.0
N = 1000

rng = np.random.default_rng()

particles = []
mtot = 0
for i in range(N):

    # pick a mass, in solar units
    m = rng.lognormal()
    mtot += m

    # positions, in pc
    pos = -r_max + 2.0 * r_max * rng.random(3)
    while np.sum(pos**2) > 1.0:
	    pos = -r_max + 2.0 * r_max * rng.random(3)
    
    # velocities, in km/s
    vel = -vel_max + 2.0 * vel_max * rng.random(3)
    
    p = Particle(m, pos, vel)
    particles.append(p)
    
print(f"Total mass of cluster: {mtot} M_sun")

rho = mtot / (4.0/3.0*np.pi * r_max**3)

s = System(particles)
s.write_binary(outfile)


