import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 1)

frequency = 300
amplitude = 2
phase = 1

nr_samples = 1600 
duration = 2.0 / frequency  
t = np.linspace(0.0, duration, nr_samples)

sin_signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)
cos_signal = amplitude * np.cos(-2 * np.pi * frequency * t + phase)

axs[0].plot(t, sin_signal)
axs[0].set_title("Semnal de tip sinus")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

axs[1].plot(t, cos_signal)
axs[1].set_title("Semnal de tip cosinus")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

plt.tight_layout()
plt.savefig('ex1.pdf')
plt.show()