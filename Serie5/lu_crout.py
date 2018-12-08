# -*- coding: utf-8 -*-

import numpy as np
import time


def elimination(L, U, b):
    '''Löst ein Gleichungssystem A*x=b durch Vorwärts- und Rückwärtselimination
    für die LU-Zerlegung von A=L*U.

    Beispiel
    --------
    x = elimination(L, U, b)

    Eingabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix

    b : float (vector)
        Inhomogenitätsvektor des Gleichungssystems

    Ausgabe
    -------
    x : float (vector)
        Lösungsvektor
    '''
    n = L.shape[0]
    x = np.zeros(n)
    y = np.zeros(n)

    # Vorwärtselimination
    y[0] = b[0]
    for i in range(1,n):
        y[i] = b[i] - L[i][0:i] @ y[0:i]
    # Rückwärtselimination
    x[n-1] = y[n-1]/U[n-1][n-1]
    for i in range(n-2, -1,-1):
        x[i] = (y[i] - U[i][i+1:] @ x[i+1:])/U[i][i]
    return x


def myLU(A):
    '''LU-Zerlegung einer Matrix A=L*U mittels Crout-Algorithmus.

    Beispiel
    --------
    L, U = myLU(A)

    Eingabe
    -------
    A : float (2d array)
        Die zu zerlegende Matrix

    Ausgabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix
    '''
    n = A.shape[0]
    L = np.identity(n, dtype=float)
    U = np.copy(A)
    for k in range(n):
        for i in range(k+1, n):
            L[i][k] = U[i][k]/U[k][k]
            U[i][k] = 0
            U[i][k+1:] -= L[i][k]*U[k][k+1:]
    return L, U

A = np.array([[1,1,0],[4,0,2],[0,2,1]], dtype=float)
L, U = myLU(A)
b = np.array([2,6,1])
x = elimination(L,U,b)
print("sol: ",x)
print("LU check: ", L @ U )
print("sol check: ", A @ x, "=", b )
