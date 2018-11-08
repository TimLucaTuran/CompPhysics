# -*- coding: utf-8 -*-
import numpy as np
def intrect(fhandle, a, b, h):
    """ Numerische Integration einer beliebigen integrierbaren Funktion mittels
    der Rechteckregel.

    Argumente
    ---------
    fhandle : function
        die zu integrierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Teilintervalle

    Output: 3-Tupel
    ---------------
    area : float
        Berechnete Fläche
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    stamm_funk : float
        Berechnete Funktionswerte der Stammfunktion (1-d array)

    Funktionsaufruf
    ---------------
        area, xwerte, stamm_funk = intrect(fhandle, a, b, h)

    Beispiel
    --------
        area, xwerte, stamm_funk = intrect(np.exp, 0, 10, 0.01)
    """



    # Mittelpunkte der Intervalle ermitteln
    mittelpunkte = np.linspace(a+h/2, b-h/2, (b-a)/h)
    # Funktionswerte an den Intervallmittelpunkten
    fwerte = np.array([fhandle(x) for x in mittelpunkte])
    # Aufsummierung von Teilintervallen
    N = mittelpunkte.size
    area = 0
    stamm_funk = np.zeros(N)
    xwerte = np.zeros(N)
    for i in range(N):
        area += h*fwerte[i]
        stamm_funk[i] = area
        xwerte[i] = mittelpunkte[i] - h/2
    # Berechnung der Fläche

    # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
    # rechten Rand des Teilintervalls


    return area, xwerte, stamm_funk
