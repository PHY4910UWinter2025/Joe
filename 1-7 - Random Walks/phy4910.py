import numpy as np
import matplotlib.pyplot as plt
    
def ode_euler(x_start, x_end, h, y0, z0, f, g):
    """
    Solves a coupled pair of ODEs using euler
     
    Takes as arguments:
      x_start - starting point for independent coordinate
      x_end - ending point
      h - difference between x_i and x_i+1 (i.e., delat x)
      y0 - initial value for first variable y(x_start)
      z_0 - initial value for second variable z(x_start)
      f - function for derivative of first variable (i.e., f = dy/dx)
      g - function for deriviative of second variable (i.e., g = dz/dx)
        
      returns three arrays, x[0,N-1], y[0,N-1], and z[0,N-1].
    """
    
    x = np.arange(x_start, x_end, h)
    N = len(x)
    y = np.zeros(N)
    y[0] = y0
    z = np.zeros(N)
    z[0] = z0
    
    for i in range(0, N-1):
        k1 = h * f(x[i], y[i], z[i])
        l1 = h * g(x[i], y[i], z[i])
            
        y[i+1] = y[i] + k1
        z[i+1] = z[i] + l1
                
    return x, y, z
    


def ode_rk4(x_start, x_end, h, y0, z0, f, g):
    """ 
    Solves a coupled pair of ODEs using runge kutta.
     
    Takes as arguments:
      x_start - starting point for independent coordinate
      x_end - ending point
      h - difference between x_i and x_i+1 (i.e., delat x)
      y0 - initial value for first variable y(x_start)
      z_0 - initial value for second variable z(x_start)
      f - function for derivative of first variable (i.e., f = dy/dx)
      g - function for deriviative of second variable (i.e., g = dz/dx)
      
      returns three arrays, x[0,N-1], y[0,N-1], and z[0,N-1].
    """
    
    x = np.arange(x_start, x_end, h)
    N = len(x)
    y= np.zeros(N)
    y[0] = y0
    z = np.zeros(N)
    z[0] = z0
    
    for i in range(0, N-1):
        k1 = h * f(x[i], y[i], z[i])
        l1 = h * g(x[i], y[i], z[i])
        k2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k1, z[i] + 0.5 * l1)
        l2 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * k1, z[i] + 0.5 * l1)
        k3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k2, z[i] + 0.5 * l2)
        l3 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * k2, z[i] + 0.5 * l2)
        k4 = h * f(x[i] + h, y[i] + k3, z[i] + l3)
        l4 = h * g(x[i] + h, y[i] + k3, z[i] + l3)
    
        y[i+1] = y[i] + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        z[i+1] = z[i] + (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0
        
    return x, y, z
    

def pick_direction(rng):
	"""
	picks a random direction, returns theta and phi
	"""
	
	theta = np.arccos(1 - 2 * rng.random())
	phi = 2*np.pi * rng.random()
	
	return theta, phi
	
def pick_optical_depth(rng):
	"""
	returns a random optical depth from distribution e^-tau
	"""
	
	x = rng.random()
	return -np.log(1 - x)
	
	
if __name__ == '__main__':

	# test!
	
	rng = np.random.default_rng()
	
	N = 40000
	theta = np.zeros(N)
	phi = np.zeros(N)
	
	for i in range(N):
		theta[i], phi[i] = pick_direction(rng)
		
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	
	ax.plot(np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta), ',')
	#ax.set_aspect('equal')
	
	plt.show()
	
	
	
	
	
	
	
	
	
	
	
