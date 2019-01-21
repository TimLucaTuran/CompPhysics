import numpy as np
import matplotlib.pyplot as plt

def alpha_osci(x0, v0, w, alpha, N, T):
    """Berechnet die Bewegung eines harmonischen Oszillators mit dem
    alpha-Verfahren.

    Beispiel
    --------
     x0 = 1
     v0 = 0
     w  = 1
     alpha = 0.5
     N = 1000
     T = 20
     x, v, t = alpha_osci(x0, v0, w, alpha, N, T)

    Eingabe
    -------
     x0 : float
         Standort
     v0 : float
         Eingangssignal
     w : float
         Eigenfrequenz
     alpha : float
         Parameter des alpha-Verfahrens
     N : Anzahl der Zeitschritte
     T : Maximalzeit

    Ausgabe
    -------
     x : float (1d-array)
         Ergebnisvektor des Ortes der Länge N+1
     v : float (1d-array)
         Ergebnisvektor der Geschwindigkeit der Länge N+1
     t : float (1d-array)
         Stützstellen der Zeit der Länge N+1
    """
    qp = np.zeros((N+1, 2))
    qp[0][0] = x0*w
    qp[0][1] = v0
    t_step = T/N
    A = np.linalg.inv(np.array([[1, -(1-alpha)*w*t_step], [(1-alpha)*w*t_step,1]]))
    B = np.array([[1, alpha*w*t_step], [-alpha*w*t_step, 1]])
    step_matrix = A@B
    #Loop:

    for i in range(N):
        qp[i+1] = step_matrix @ qp[i]

    x = qp[:,0]/w
    v = qp[:,1]
    t = np.linspace(0, T, N+1)
    return x, v, t
