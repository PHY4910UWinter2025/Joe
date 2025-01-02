import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
f = x*np.exp(-x)

plt.plot(x, f)
plt.show()
