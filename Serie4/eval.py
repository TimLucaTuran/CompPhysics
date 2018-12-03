from module_simplex import simplex , fhandle
import matplotlib.pyplot as plt
import numpy as np
plotpoints = 200
fvalues = np.zeros((plotpoints))
N_max_values = np.arange(1, plotpoints+1)
for N_max in N_max_values:
    x_min, f_min, n = simplex(fhandle, [1,1], N_max, 0)
    if N_max%20 == 0:
        print("N_max", N_max)
        print(f_min, x_min)
    fvalues[N_max-1] = np.linalg.norm([3,2]-x_min)
plt.plot(N_max_values, fvalues)
plt.xlabel("N_max")
plt.ylabel("f_min")
plt.show()
"""
print(simplex(fhandle, [-1,-1], 1000, 1e-20))
"""
