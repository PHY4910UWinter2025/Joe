import numpy as np
import matplotlib.pyplot as plt

t, r0, r1, r2, r3, r4, r5, r6, r7, r8 = np.loadtxt("sun_distances_long_time_data.txt", unpack=True)

plt.plot(t, r0)
plt.plot(t, r1)
plt.plot(t, r2)
plt.plot(t, r3)
plt.plot(t, r4)
plt.plot(t, r5)
plt.plot(t, r6)
plt.plot(t, r7)
plt.plot(t, r8)
# plt.plot(x2, y2, color="red")
# plt.axis("equal")
plt.semilogy()
plt.show()
