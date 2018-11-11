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
    mittelpunkte = np.linspace(a + h*0.5, b - h*0.5, (b-a)/h)
    # Funktionswerte an den Intervallmittelpunkten
    fwerte = fhandle(mittelpunkte)
    stammfunktion = np.cumsum(fwerte)*h
    # Letzter Eintrag von cumsum entspricht der gesamt summe
    area = stammfunktion[-1]
    # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
    # rechten Rand des Teilintervalls
    xwerte = mittelpunkte + h*0.5


    return area, xwerte, stammfunktion

#Version von intrect wenn nur die area benötigt wird
def intrect_only_area(fhandle, a, b, h):
    mittelpunkte = np.linspace(a + h*0.5, b - h*0.5, (b-a)/h)
    fwerte = fhandle(mittelpunkte)
    area = np.sum(fwerte)*h
    return area
