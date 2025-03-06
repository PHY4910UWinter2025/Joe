from math import sqrt
from nbody import Particle, System

s = System.read("test.txt")

dt = 0.01
tf = 100
ti = 0

f = open("data.txt", "w")

t = ti
while t < tf:
	
	s.update_positions(0.5 * dt)
	
	s.calc_accels()
	s.update_velocities(dt)
	
	s.update_positions(0.5 * dt)
	
	t += dt
	s.time = t
	
	f.write(f"{t} {s.particles[0].x()} {s.particles[0].y()} {s.particles[1].x()} {s.particles[1].y()}")
	
f.close()
	
	

