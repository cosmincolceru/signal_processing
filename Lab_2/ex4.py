import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=3, ncols=1)

frequency_1 = 300
duration = 3 / frequency_1
t = np.linspace(0.0, duration, int(duration / 0.0001))

# Un semnal de tip sawtooth 
sawtooth_signal = 2 * (t * frequency_1 - np.floor(t * frequency_1 + 1/2))

axs[0].plot(t, sawtooth_signal)
axs[0].set_title("Semnal sawtooth")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

# Un semnal de tip square
frequency_2 = 600
square_signal = np.sign(np.sin(2 * np.pi * t * frequency_2))

axs[1].plot(t, square_signal)
axs[1].set_title("Semnal square")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

# Suma semnalelor
sum_signal = sawtooth_signal + square_signal

axs[2].plot(t, sum_signal)
axs[2].set_title("Suma semnalelor")
axs[2].set_xlabel("Timp")
axs[2].set_ylabel("Amplitudine")


plt.tight_layout()
plt.savefig("ex4.pdf")
plt.show()