# -*- coding: utf-8 -*-
""" Dieses Skript führt die Funktion 'intrect' aus.

Die numerische Integration nach der Rechteckregel wird an den Funktionen
f(x) = x, f(x) = x^2 und f(x) = exp(x) durchgeführt. Anhand der berechneten
Stammfunktionen und Flächeninhalte wird das Konvergenzverhalten zum jeweiligen
analytischen Ergebnis verglichen.
"""

import numpy as np
import matplotlib.pyplot as plt
from module_intrect import intrect, intrect_only_area

# Berechnung der exakten Flächeninhalte
a, b = 0, 10
stamm_lin = np.poly1d([1/2, 0, 0])
int_analytic_lin = stamm_lin(b) - stamm_lin(a)
stamm_quad = np.poly1d([1/3, 0, 0, 0])
int_analytic_quad = stamm_quad(b) - stamm_quad(a)
int_analytic_exp = np.exp(b) - np.exp(a)

# %% Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle

# logarithmisch äquidistanter Vektor der Schrittweiten
h = np.logspace(-4, -1, num=100)


# Definition der Funktionen (vgl. MatLab function handles)
lin = np.poly1d([1,0])
quad = np.poly1d([1, 0, 0])
exp = np.exp
error_lin = np.zeros(h.size)
error_quad = np.zeros(h.size)
error_exp = np.zeros(h.size)
# Schleife über alle h zur Berechnung von Integral und dessen Fehler
for i in range(h.size):
    # f(x) = x
    area = intrect_only_area(lin, a, b, h[i])
    error_lin[i] = abs(int_analytic_lin - area )

    # f(x) = x^2
    area= intrect_only_area(quad, a, b, h[i])
    error_quad[i] = abs(int_analytic_quad - area )

    # f(x) = exp(x)
    area = intrect_only_area(exp, a, b, h[i])
    error_exp[i] = abs(int_analytic_exp - area )

    print("Calculating point nr: ", i)

# logarithmischer Plot Fehler vs. Schrittweite h
#plt.plot(h, error_lin)
#plt.show()
plt.loglog(h , error_lin, label="lin")
plt.loglog(h , error_quad, label="quad")
plt.loglog(h , error_exp, label="exp")
plt.legend()
plt.show()
# %% Abhaengigkeit der Integrationskonstante vom linken Intervallrand
# am Bsp. der Stammfunktion F von x^2

# rechte Intervallgrenze fest
# linke Intervallgrenze mit verschiedenen Werten
stamm_quad_werte = np.array([])
for i in range(1,5):

    area, xwerte, stammfunktion = intrect(quad, a+2*i, b, 0.01)
    if  stamm_quad_werte.size == 0:
        stamm_quad_werte = xwerte
    plt.plot(xwerte, stammfunktion, label="a = {}".format(a+i))
plt.plot(stamm_quad_werte, stamm_quad(stamm_quad_werte), label="1/3 x^3")
axes = plt.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([-50,250])
plt.legend()
plt.show()
