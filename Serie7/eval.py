# -*- coding: utf-8 -*-
from alpha import alpha_osci
import matplotlib.pyplot as plt
import numpy as np
# Startparameter
x0 = 1
v0 = 0
w  = 1
T  = 20

# Analytische Lösungen
x_ana = x0*np.cos(w*T) +v0/w*np.sin(w*T)
v_ana = -x0*w*np.sin(w*T) + v0*np.cos(w*T)
x_max = np.sqrt(x0**2 + (v0/w)**2)
v_max = w*x_max

alpha = np.array([0, 0.5, 0.501, 0.51, 1])
N = np.ceil(2.0*np.logspace(1,4,60)).astype(int)
dt = T/N
e_global = np.zeros((alpha.size, N.size))
# %% Beispiel 1: Globaler Fehler der Lösung in Abhängigkeit von der Schrittweite in der Zeit
for i in range(alpha.size):
    for j in range(N.size):
        x, v, t = alpha_osci(x0, v0, w, alpha[i], N[j], T)
        e_global[i][j]  = np.sqrt(((x[-1]-x_ana)/x_max)**2+(((v[-1]-v_ana)/v_max))**2)

for i in range(alpha.size):
    plt.loglog(dt, e_global[i], label="α = {}".format(alpha[i]))
    plt.legend(loc="best")
plt.ylabel("Fehler")
plt.xlabel("Schrittweite dt")
plt.show()

#Energieentwicklung:
N = 200
alpha = np.array([0, 0.5, 1])
energie = np.zeros((3,N+1))
for i in range(alpha.size):
    x, v, t = alpha_osci(x0, v0, w, alpha[i], N, T)
    print(x.shape, v.shape)
    energie[i] =  v**2 + w**2*x**2
    plt.plot(t, energie[i], label="α = {}".format(alpha[i]))

plt.xlabel("Zeit")
plt.ylabel("Energie")
plt.legend(loc="best")
plt.show()
