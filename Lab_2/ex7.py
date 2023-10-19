import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=2, ncols=1)

fs = 1000

duration = 1
t = np.linspace(0.0, duration, int(duration * 1000))
amplitude = 1.0  

signal = amplitude * np.sin(2 * np.pi * fs * t)

axs[0].plot(t, signal)
axs[0].set_title("Semnal original")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

t_2 = [t[i] for i in range(0, len(t), 4)]
signal_2 = [signal[i] for i in range(0, len(signal), 4)]

axs[1].plot(t_2, signal_2)
axs[1].set_title("Semnal decimat")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

plt.tight_layout()
plt.show()
