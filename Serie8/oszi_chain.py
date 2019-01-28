import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt

def dgl_solver(N, T, w, a, c, W, T0):
    def f_ext(t):
        return np.sin(W*t)*np.exp(-(t-3*T0)**2/T0**2)

    """
    Construct Matrix of Form [[-1.  1.  0.  0.] as the interatction between
                             [ 1. -2.  1.  0.]  single ozsillators
                             [ 0.  1. -2.  1.]
                             [ 0.  0.  1. -1.]]
    """
    M = np.zeros((N,N))
    for i in range(N):
        if i == 0:
            M[i,0:2] = [-1, 1]
        elif i == N-1:
            M[i,i-1:] = [1, -1]
        else:
            M[i,i-1:i+2] = [1, -2, 1]

    #Define right hand side of the system y' = f(t, y)
    #First N are Location, Last N are velocity
    def dgl(t, y):
        x = y[:N]
        x_dot = y[N:]
        f_ext_vec = np.zeros(N)
        f_ext_vec[0] = 1
        x_next = x_dot
        #print("x: ",x,"\n", "x_dot: ", x_dot)
        x_dot_next = -w**2*x + -a*x_dot + M@x + f_ext(t)*f_ext_vec
        return np.concatenate((x_next, x_dot_next))


    y0 = np.zeros(2*N)
    sol = sp.solve_ivp(dgl, [0, T], y0, method='RK45', rtol=1e-6, atol=1e-12)
    return sol
