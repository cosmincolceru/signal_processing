import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=3, ncols=1)

fs = 1000
frequency = 50

duration = 1
t = np.linspace(0.0, duration, int(duration * 1000))
amplitude = 1.0  

signal = amplitude * np.sin(2 * np.pi * frequency * t)

axs[0].plot(t, signal)
axs[0].set_title("Semnal original")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

t_2 = t[::4]
signal_2 = signal[::4]

axs[1].plot(t_2, signal_2)
axs[1].set_title("Semnal decimat")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

t_3 = t_2[::4]
signal_3 = signal_2[::4]

axs[2].plot(t_3, signal_3)
axs[2].set_title("Semnal decimat")
axs[2].set_xlabel("Timp")
axs[2].set_ylabel("Amplitudine")

plt.tight_layout()
plt.savefig("ex7.pdf")
plt.show()
