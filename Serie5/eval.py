# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from lu_crout import myLU, elimination
from timeit import default_timer as timer

max_matrix_size = 500
repititions = 1
time_data_average = np.zeros(max_matrix_size)
for i in range(1, max_matrix_size+1):
    #Initialise rand matrix
    print("Matrix size: ", i)
    time_data = np.zeros(repititions)
    for j in range(repititions):
        A = np.random.rand(i, i)*100
        b = np.random.rand(i)
        start = timer()
        L, U = myLU(A)
        x = elimination(L,U,b)
        end = timer()
        time_data[j] = end - start
    time_data_average[i-1] = np.average(time_data)
print("time max matrix: ", time_data_average[-1])
max_matrix_size_list = np.arange(1, max_matrix_size+1)
plt.loglog(max_matrix_size_list, time_data_average, label="Data")
#plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list,label="x")
plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list**2,label="x**2")
plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list**3,label="x**3")
plt.loglog(max_matrix_size_list, 1e-6*max_matrix_size_list,label="x")
plt.xlabel('Matrix Size')
plt.ylabel('Time(s)')
plt.legend()
plt.show()
