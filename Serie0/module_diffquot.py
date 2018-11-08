import numpy as np
def diffquot(fhandle, a, b, h):
    """ Berechne den rechtseitigen Differenzenquotienten.

    Argumente
    ---------
    fhandle : function
        die zu differenzierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Differentiation

    Output: 2-Tupel
    ------
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    ableitung : float
        Ergebnisvektor mit der numerischen Ableitung (1-d array)

    Funktionsaufruf
    ---------------
        xwerte, ableitung = diffquot(fhandle, a, b, h)

    Beispiel
    --------
        xwerte, ableitung = diffquot(np.sin, -10, 10, 0.1)
    """


    # Bestimmung des Definitionsbereichs der Funktion
    xwerte = np.arange(a,b,h)
    # Evaluierung der Funktion 'fhandle'
    funktions_werte = np.array([fhandle(x) for x in xwerte])

    # Berechung der numerischen Ableitung mittels des rechtsseitigen
    # Differenzenquotienten
    ableitung = np.zeros(xwerte.size - 1)
    for i in range(xwerte.size - 1):
        ableitung[i] = (funktions_werte[i+1] - funktions_werte[i])/h
    return (xwerte[:-1], ableitung)
