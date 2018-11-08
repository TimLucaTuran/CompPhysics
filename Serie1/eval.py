# -*- coding: utf-8 -*-
""" Dieses Skript führt die Funktion 'intrect' aus.

Die numerische Integration nach der Rechteckregel wird an den Funktionen
f(x) = x, f(x) = x^2 und f(x) = exp(x) durchgeführt. Anhand der berechneten
Stammfunktionen und Flächeninhalte wird das Konvergenzverhalten zum jeweiligen
analytischen Ergebnis verglichen.
"""

import numpy as np
import matplotlib.pyplot as plt
from module_intrect import intrect

# Berechnung der exakten Flächeninhalte
int_analytic_lin = np.poly1d([1/2, 0])
int_analytic_quad = np.poly1d([1/3, 0, 0])
int_analytic_exp = np.exp

# %% Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle

# logarithmisch äquidistanter Vektor der Schrittweiten
h = np.logspace(-4, -1)


# Definition der Funktionen (vgl. MatLab function handles)
lin = np.poly1d([1])
quad = np.poly1d([1, 0])
exp = np.exp
a, b = 0, 10
error_lin = np.zeros(h.size)
error_quad = np.zeros(h.size)
error_exp = np.zeros(h.size)
# Schleife über alle h zur Berechnung von Integral und dessen Fehler
for i in range(h.size):
    # f(x) = x
    area, xwerte, stamm_funk = intrect(lin, a, b, h[i])
    error_lin[i] = abs((int_analytic_lin(b) - int_analytic_lin(a)) - area )

    # f(x) = x^2
    area, xwerte, stamm_funk = intrect(quad, a, b, h[i])
    error_quad[i] = abs(int_analytic_quad(b) - area )

    # f(x) = exp(x)
    area, xwerte, stamm_funk = intrect(exp, a, b, h[i])
    error_exp[i] = abs(int_analytic_exp(b) - area )

# logarithmischer Plot Fehler vs. Schrittweite h
#plt.plot(h, error_lin)
#plt.show()
print(error_lin)
# %% Abhaengigkeit der Integrationskonstante vom linken Intervallrand
# am Bsp. der Stammfunktion F von x^2

# rechte Intervallgrenze fest

# linke Intervallgrenze mit verschiedenen Werten
