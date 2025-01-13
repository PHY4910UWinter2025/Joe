
import numpy as np

# solve the ode via euler

def f(x, y, z):
	return z
	
def g(x, y, z):
	return -1/y * z**2

h = 0.01
x = np.arange(0, 10, h)
N = len(x)

y = np.zeros(N)
z = np.zeros(N)

# set BCs
y[0] = 1
z[0] = 1

for i in range(N-1):
	k1 = h * f(x[i], y[i], z[i])
	ell1 = h * g(x[i], y[i], z[i])
	
	y[i+1] = y[i] + k1
	z[i+1] = z[i] + ell1

np.savetxt("euler_data.txt", np.column_stack((x,y,z)))
