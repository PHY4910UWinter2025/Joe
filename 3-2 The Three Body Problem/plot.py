import numpy as np
import matplotlib.pyplot as plt

t, x1, y1, x2, y2 = np.loadtxt("data.t", unpack=True)

plt.plot(x1, y1, color="black")
plt.plot(x2, y2, color="red")
plt.show()
