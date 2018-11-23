# -*- coding: utf-8 -*-
import numpy as np
from himmelblau import himmelblau

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
    simplex_list = np.zeros((3,3))
    simplex_list[0][0:2] = x_start
    simplex_list[0][2] = fhandle(simplex_list[0][0:2])

    # x1, x2 generieren
    simplex_list[1][0:2] = [x_start[0]+lambda_, x_start[1]]
    simplex_list[1][2] = fhandle(simplex_list[1][0:2])

    simplex_list[2][0:2] = [x_start[0], x_start[1]+lambda_]
    simplex_list[2][2] = fhandle(simplex_list[2][0:2])

    loopcount = 0

    #Start des Loops
    while loopcount <= N_max:
        loopcount += 1
        print("loopcount: ", loopcount)
        #simpex_list sortieren
        simplex_list.view('i8,i8,i8').sort(order=['f2'], axis=0)
        #Berechne den potentiellen nächsten Punkt
        mirror_center = 0.5 * (simplex_list[0][0:2]+simplex_list[1][0:2])
        mirror_point = mirror_center + alpha_*(mirror_center-simplex_list[2][0:2])
        fvalue_mirror_point = fhandle(mirror_point)
        #Expansion
        if fvalue_mirror_point < simplex_list[0][2]:
            expansion_point = mirror_center + gamma_*(mirror_point - mirror_center)
            fvalue_expansion_point = fhandle(expansion_point)
            if fvalue_expansion_point < fvalue_mirror_point:
                simplex_list[2][0:3] = np.append(expansion_point, fvalue_expansion_point)
            else:
                simplex_list[2][0:3] = np.append(mirror_point, fvalue_mirror_point)
        #Spiegeln
        elif fvalue_mirror_point < simplex_list[1][2]:
            simplex_list[2][0:3] = np.append(mirror_point, fvalue_mirror_point)
        #Kontraktion
        elif fvalue_mirror_point < simplex_list[2][2]:
            simplex_list[2][0:3] = np.append(mirror_point, fvalue_mirror_point)

        else:
            contraction_point = mirror_center + beta_*(simplex_list[2][0:2]-mirror_center)
            fvalue_contraction_point = fhandle(contraction_point)
            if fvalue_contraction_point < simplex_list[2][2]:
                simplex_list[2][0:3] = np.append(contraction_point, fvalue_contraction_point)
            #Kompression
            else:
                simplex_list[1][0:2] = 0.5*(simplex_list[1][0:2] + simplex_list[0][0:2])
                simplex_list[1][2] = fhandle(simplex_list[1][0:2])

                simplex_list[2][0:2] = 0.5*(simplex_list[2][0:2] + simplex_list[0][0:2])
                simplex_list[2][2] = fhandle(simplex_list[2][0:2])
        #Überprúfen ob das Minimum gefunden wurde
        #Varianz berechnen:
        variance = np.var(simplex_list, axis=0)[2]
        #Größe des Simplex berechnen:
        a = np.linalg.norm(simplex_list[0][0:2] - simplex_list[0][0:2])
        b = np.linalg.norm(simplex_list[0][0:2] - simplex_list[0][0:2])
        c = np.linalg.norm(simplex_list[0][0:2] - simplex_list[0][0:2])
        s = 0.5*(a+b+c)
        simplex_size = 0.25 * np.sqrt(s*(s-a)*(s-b)*(s-c))
        #Abruchbedingungen überprüfen
        if variance < p**2 and simplex_size < 0.01*lambda_:
            break
    return simplex_list[0][0:2], simplex_list[0][2], loopcount




#==================================================
# Initialisierung
#==================================================

# Die Skalierungsfaktoren des Downhill-Simplex Verfahrens
alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
beta_   = 0.5  # empfohlener Faktor für die Kontraktion
gamma_  = 2.0  # empfohlener Faktor für die Expansion
lambda_ = 0.1  # empfohlene Größe des Startsimplex

fhandle = himmelblau
x_start = [2,4]
N_max   = 1e3
p       = 1e-22
x_min, f_min, N = simplex(fhandle, x_start, N_max, p)
print(f_min, x_min)
