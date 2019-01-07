import numpy as np
import matplotlib.pyplot as plt

def my_fft(N, signal):
    if N == 1:
    # Rekursionsende
        return signal
    else:
    # Ab hier laufen wir im Rekursionsbaum nach unten.
        even = my_fft(N//2, signal[::2])
        odd = my_fft(N//2, signal[1:N:2])
        spektrum = np.zeros(N, dtype=complex)
        #dtype=complex essentiell da sonst imaginärteil verloren geht
        scalar_list = np.exp(-2j*np.pi*np.arange(N//2)/N)
        spektrum[:N//2] = even + scalar_list * odd
        spektrum[N//2:] = even - scalar_list * odd
        return spektrum
