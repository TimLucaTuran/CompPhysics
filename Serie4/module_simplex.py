# -*- coding: utf-8 -*-
import numpy as np

def simplex(fhandle, x_start, N_max, p):
    """ SIMPLEX Minimumssuche mittels des Downhill-Simplex Verfahrens.

    Beispiel
    --------

    fhandle = himmelblau
    x_start = [0 0]
    N_max   = 1e3
    p       = 1e-15
    x_min, f_min, N = simplex(fhandle, x_start, N_max, p)

    Argumente
    ---------
    fhandle : function
        Die zu minimierende Funktion

    x_start : float
        Startpunkt des Simplex

    N_max : int
        Maximale Anzahl an Iterationen

    p : float
        Genauigkeit in x oder f

    Output
    ------
    x_min : float
        Punkt (x,y) des Funktionsminimums (2-tupel)

    f_min : float
        Funktionsminimum

    N : int
        Anzahl der benötigten Schritte
    """
    #x_start eintragen
    simpex_list = np.zeros(3,3)
    simplex_list[0][0] = x_start[0]
    simplex_list[0][1] = x_start[1]
    simplex_list[0][2] = fhandle(simplex_list[0][0], simplex_list[0][1])

    # x1, x2 generieren
    simplex_list[1][0] = x_start[0]+lambda_
    simplex_list[1][1] = x_start[1]
    simplex_list[1][2] = fhandle(simplex_list[1][0], simplex_list[1][1])

    simplex_list[2][0] = x_start[0]
    simplex_list[2][1] = x_start[1]+lambda_
    simplex_list[2][2] = fhandle(simplex_list[2][0], simplex_list[2][1])

    loopcount = 0

    #Start des Loops
    while loopcount <= N_max:
        #Funktionswerte berechnen
        


#==================================================
# Initialisierung
#==================================================

# Die Skalierungsfaktoren des Downhill-Simplex Verfahrens
alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
beta_   = 0.5  # empfohlener Faktor für die Kontraktion
gamma_  = 2.0  # empfohlener Faktor für die Expansion
lambda_ = 0.1  # empfohlene Größe des Startsimplex
