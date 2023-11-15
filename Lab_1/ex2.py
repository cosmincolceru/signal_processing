import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=6, ncols=1, figsize=(10, 20))

# Un semnal sinusoidal de frecventa 400 Hz, care sa contina 1600 de esantioane.

frequency = 400  
nr_samples = 1600 
duration = 1.0 / frequency  
t = np.linspace(0.0, duration, nr_samples)

amplitude = 1.0  
signal = amplitude * np.sin(2 * np.pi * frequency * t)

axs[0].plot(t, signal)
# axs[0].stem(t, signal)
axs[0].set_title("Semnal sinusoidal de 400 Hz")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")


# Un semnal sinusoidal de frecventa 800 Hz, care sa dureze 3 secunde.

frequency = 800
duration = 3
t = np.linspace(0.0, duration, int(duration / 0.0001))

amplitude = 1.0  
signal = amplitude * np.sin(2 * np.pi * frequency * t)

axs[1].plot(t, signal)
axs[1].set_title("Semnal sinusoidal de 800 Hz")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")


# Un semnal de tip sawtooth de frecventa 240 Hz

frequency = 240
duration = 3 / frequency
t = np.linspace(0.0, duration, int(duration / 0.0001))

signal = 2 * (t * frequency - np.floor(t * frequency + 1/2))

axs[2].plot(t, signal)
axs[2].set_title("Semnal sawtooth de 240 Hz")
axs[2].set_xlabel("Timp")
axs[2].set_ylabel("Amplitudine")

# Un semnal de tip square de frecventa 300 Hz

frequency = 300
duration = 3 / frequency
t = np.linspace(0.0, duration, int(duration / 0.0001))

signal = np.sign(np.sin(2 * np.pi * t * frequency))

axs[3].plot(t, signal)
axs[3].set_title("Semnal square de 400 Hz")
axs[3].set_xlabel("Timp")
axs[3].set_ylabel("Amplitudine")

# Un semnal 2D aleator

arr = np.random.rand(128, 128)
axs[4].imshow(arr)
axs[4].set_title("Semnal 2D aleator")
axs[4].set_xlabel("X")
axs[4].set_ylabel("Y")

# Un semnal 2D

arr = np.zeros((128, 128))

def draw_sqares(offset):
	line = np.ones(128 - offset * 2)
	arr[offset, offset:-offset] = line
	arr[offset:-offset, offset] = line
	arr[-offset, offset:-offset] = line
	arr[offset:-offset, -offset-1] = line

draw_sqares(20)
draw_sqares(40)
draw_sqares(60)

axs[5].imshow(arr)
axs[5].set_title("Semnal 2D")
axs[5].set_xlabel("X")
axs[5].set_ylabel("Y")


plt.tight_layout()
plt.savefig('ex2.pdf')
plt.show()
