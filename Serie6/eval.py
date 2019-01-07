from fft_module import my_fft
import numpy as np
import matplotlib.pyplot as plt


#Aufgabe 1
N = 256
signal_length = 30 * np.pi
sample_rate = 2*np.pi*N/signal_length
t = np.linspace(0, signal_length, N)
f = np.linspace(0, sample_rate, N)
x = np.zeros((15,128))
for w in range(15):
    signal = np.sin(5*t) + np.sin(w*t)
    spektrum = np.abs(my_fft(N, signal))
    x[-w] = spektrum[:128]

plt.imshow(x, extent=[0,sample_rate/2,1,15])
plt.xlabel("$w$ Spektrum")
plt.ylabel("$w$ Signal")
plt.show()

#Aufgabe 2
powers = [32, 64, 128, 256, 512]
N = 16
signal_length = 2*np.pi
sample_rate = 2*np.pi*N/signal_length
t = np.linspace(0, signal_length, N)
gauss = np.exp((-(t-np.pi)**2)/0.5)
spektrum = np.abs(my_fft(N, gauss))
spektrum = np.concatenate((spektrum[N//2:], spektrum[:N//2]))
plt.xlabel("$w$ Spektrum")
plt.ylabel("Amplitude")
plt.plot( np.linspace(-6,6, N), spektrum)
plt.text(3,3,"N = 16")
plt.show()
for N in powers:
    gauss_with_zeros = np.concatenate((np.zeros(N//2-8), gauss, np.zeros(N//2-8)))
    spektrum = np.abs(my_fft(N, gauss_with_zeros))
    spektrum = np.concatenate((spektrum[N//2:], spektrum[:N//2]))
    plt.xlabel("$w$ Spektrum")
    plt.ylabel("Amplitude")
    plt.text(3,3,"N = {}".format(N))
    plt.plot( np.linspace(-6,6, N),spektrum)

    plt.show()
