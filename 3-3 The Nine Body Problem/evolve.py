from nbody import Particle, System

s = System.read("solar_system_ic.txt")

dt = 0.001
tf = 200
ti = 0

f = open("sun_distances_long_time_data.txt", "w")

t = ti

dt_out = 0.1
t_out = 0

count = 0

while t < tf:
	
	# drift
	s.update_positions(0.5 * dt)
	
	# kick
	s.calc_accels()
	s.update_velocities(dt)
	
	# drift
	s.update_positions(0.5 * dt)
	
	t += dt
	s.time = t
	
	# f.write(f"{t} {s.particles[0].x()} {s.particles[0].y()} {s.particles[1].x()} {s.particles[1].y()}\n")
	sun = s.particles[0]
	
	if t > t_out:
		count += 1
		f.write(f"{t}\t")
		
		for p in s.particles:
			f.write(f"{sun.distance_from(p)}\t")
			
		f.write("\n")
		
		t_out += dt_out
	
f.close()
print(f"We recorded {count} times. (Expected 20_000)")
	
	

