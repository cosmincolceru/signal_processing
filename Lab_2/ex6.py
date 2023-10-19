import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=3, ncols=1)

fs = 400

duration = 0.05
t = np.linspace(0.0, duration, int(duration / 0.0001))
amplitude = 1.0  

frequency = fs / 2
signal_1 = amplitude * np.sin(2 * np.pi * frequency * t)

axs[0].plot(t, signal_1)
axs[0].set_title("f = f_s / 2")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

frequency = fs / 4
signal_2 = amplitude * np.sin(2 * np.pi * frequency * t)

axs[1].plot(t, signal_2)
axs[1].set_title("f = f_s / 4")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

frequency = 0
signal_2 = amplitude * np.sin(2 * np.pi * frequency * t)

axs[2].plot(t, signal_2)
axs[2].set_title("f = 0 Hz")
axs[2].set_xlabel("Timp")
axs[2].set_ylabel("Amplitudine")

plt.tight_layout()
plt.savefig("ex6.pdf")
plt.show()
