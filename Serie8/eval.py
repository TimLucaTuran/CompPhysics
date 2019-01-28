import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from oszi_chain import dgl_solver


N = 200
c = 3
T = 3000
sol = dgl_solver(N, T, w=1, a=1e-6, c=c, W=1.5, T0=10)
for i in range(4):
    plt.plot(sol.t, sol.y[i])
plt.xlim(0,10)
plt.show()

print(sol.y[:N])
energie = np.zeros((N, sol.t.size))
for i in range(N):
    # Energie E = 1/2 m v**2 + 1/2 c x**2 , m = 1
    energie[i] = 1/2*sol.y[i+N]**2 + 1/2*c*sol.y[i]**2
plt.imshow(energie, extent=[0,T,0,200])
plt.show()
