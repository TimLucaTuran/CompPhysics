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

def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if N == 1:  # this cutoff should be optimized
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even + factor[N // 2:] * X_odd])
"""
N = 256
w = 2
signal_length = 15
sample_rate = N/signal_length
t = np.linspace(0, signal_length, N)
f = np.linspace(0, sample_rate, N)

signal = 5*np.sin(5*2*np.pi*t) + np.sin(w*2*np.pi*t)
plt.plot(np.arange, signal[:N//6])
plt.show()
plt.plot(f[:N//2], 2/N*np.abs(my_fft(N, signal))[:N//2])
plt.show()
"""
