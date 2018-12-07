# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from lu_crout import myLU, elimination
from timeit import default_timer as timer
#%% Initialisiere gemeinsame Parameter

# Matrix A des aufgestellten Grundstoff-Gleichungssystems

# Inhomogenitätenvektoren für diverse Glühweinzutaten


#%% Beispiel 1: Glühweinproduktion

# Zerlege Matrix A

# Berechne für jede Glühweinzutat die nötige Menge an Grundstoffen

# Konsolenausgabe

#%% Beispiel 2: Laufzeit der LU-Zerlegung in Abhängigkeit von der Matrixgröße
max_matrix_size = 30
repititions = 50
time_data_average = np.zeros(max_matrix_size)
for i in range(1, max_matrix_size):
    #Initialise rand matrix
    print("Matrix size: ", i)
    time_data = np.zeros(repititions)
    for j in range(repititions):
        A = np.random.rand(i,i)
        start = timer()
        L, U = myLU(A)
        end = timer()
        time_data[j] = end - start
    time_data_average[i] = np.average(time_data)
print("time max matrix: ", time_data_average[-1])
max_matrix_size_list = np.arange(1, max_matrix_size+1)
plt.loglog(max_matrix_size_list, time_data_average, label="Data")
plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list**2,label="x**2")
plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list**3,label="x**3")
plt.show()
