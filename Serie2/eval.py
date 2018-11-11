""" Dieses Skript führt die Funktion 'diffquot' aus.

Es wird die numerische Ableitung der Funktion sin(x) mittels rechtsseitigem
Differenzenquotienten berechnet und mit ihrer analytischen Ableitung, cos(x),
verglichen. Dabei wird insbesondere das Verhalten der Differenz aus beiden
untersucht.
"""

import numpy as np
import matplotlib.pyplot as plt
from module_diffquot import diffquot
# Aufruf der Ableitungsfunktion und Speichern des Ergebnis in zwei Variablen.
# Wir nutzen hier die Werte für den Beispielaufruf der Funktion diffquot.
fhandle = np.sin  # Definition der input-Funktion
a = -50          # untere Intervallgrenze
b = 50           # obere Intervallgrenze
h = 0.1           # Schrittweite

xwerte, ableitung = diffquot(fhandle, a, b, h)

# Darstellung der Funktion und ihrere Ableitung in einem Plot
fig, ax = plt.subplots()
ax.plot(xwerte, np.sin(xwerte), label='sin(x)')
ax.plot(xwerte, ableitung, label='num. diff.')
ax.set_title('Funktion und ihre Ableitung')
ax.legend(loc='best')
fig.tight_layout()
plt.show()

#%% Gesamtfehler in Abhängigkeit der Schrittweite

anzahl_h = 300
h_min = 0.1
h_max = 3

# äquidistanter Vektor im Intervall [h_min, h_max] der Länge anzahl_h
h_list = np.linspace(h_min, h_max, anzahl_h)

# Intialisierung des Gesamtfehler-Vektors
gesamtfehler = np.zeros(anzahl_h)

for i in range(anzahl_h):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h_list[i])

    # berechne die analytische Ableitung
    analytische_ableitung = np.array([np.cos(x) for x in xwerte])

    # berechne den Gesamtfehler für jedes h
    ##summe = [h_list[i] * abs(analytische_ableitung[x] - ableitung[x]) for x in xwerte]
    for k in range(xwerte.size):
        gesamtfehler[i] += h_list[i] * abs(analytische_ableitung[k] - ableitung[k])
# Darstellung als Linienplot
plt.plot(h_list, gesamtfehler)
plt.xlabel('h')
plt.ylabel('Delta(h)')
plt.title("Error Plot")
plt.legend()
plt.show()
#%% lokaler Fehler für feste Schrittweiten

# überschreibe h erneut
h = [0.2, 1, 2.5]

fig, ax = plt.subplots()

for index in range(3):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h[index])

    # berechne die analytische Ableitung
    analytische_ableitung = np.array([np.cos(x) for x in xwerte])
    # Darstellung des Betrags der Differenz beider Ableitungen als Linienplot
    ax.plot(xwerte, np.array([abs(analytische_ableitung[i] - ableitung[i]) for i in range(xwerte.size)]) ,
     label='h=%.1f' % h[index])

# Plotbeschriftung
ax.legend(loc='best')
ax.set_xlabel('Koordinate x')
ax.set_ylabel('lokaler Fehler')
ax.set_title('Lokaler Fehler')
fig.tight_layout()
plt.show()
"""
Diskussion:

Der Gesamtfehler steigt zunächst linear an. Bei h-Werten in der nähe von h=3 beginnt der Gesamtfehler
von dieser linearität abzuweichen. Vermutlich ist h hier so unrealistisch groß, dass schon der Differenzial-
operator auserhalb seines Anwendungsbereiches benutzt wird.

Der  lokaler Fehler variiert periodisch und die lokale Differenz steigt mit wachsendem h. Diese Periodizität
stammt aus dem Sinus. Immer wenn sich dieser weinig ändert ist seine Ableitung schwer abzuschätzen.
"""
