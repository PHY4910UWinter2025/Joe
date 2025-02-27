from math import sqrt

class Particle:

	def __init__(self, mass, position, velocity):
		
		self.mass = mass
		self.position = position
		self.velocity = velocity
		
		self.accel = [0, 0, 0]
		
	def x(self):
		return self.position[0]
	
	def radius(self):
		return sqrt(self.position[0]**2 + self.position[1]**2 + self.position[2]**2)
		
	def distance_from(self, p):
		return sqrt((self.position[0] - p.position[0])**2 + (self.position[1] - p.position[1])**2 + (self.position[2] - p.position[2])**2)
	
	def velocity2(self):
		return self.velocity[0]**2 + self.velocity[1]**2 + self.velocity[2]**2
	
	def __str__(self):
		return f"{self.mass} {self.position[0]} {self.position[1]} {self.position[2]} {self.velocity[0]} {self.velocity[1]} {self.velocity[2]}"
		
	@classmethod
	def from_string(cls, s):
		parts = s.split()
		m = float(parts[0])
		x = float(parts[1])
		y = float(parts[2])
		z = float(parts[3])
		vx = float(parts[4])
		vy = float(parts[5])
		vz = float(parts[6])
		
		return cls(m, [x, y, z], [vx, vy, vz])
	
		

if __name__ == "__main__":
	
	sun = Particle(0.9, [-0.10, 0, 0], [0, 0.13333, 0])
	earth = Particle(0.1, [0.9, 0, 0], [0, -1.2, 0])
	print(sun.mass)
	print(sun.position[0])
	print(sun.x())
	print(sun)
	print(earth)
	print(sun.distance_from(earth))
	
	newp = Particle.from_string("1 2 3 4 5 6 7")
	print(newp)
