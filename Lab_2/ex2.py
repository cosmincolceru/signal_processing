import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 1)

frequency = 300
amplitude = 1
nr_samples = 1600 
duration = 2.0 / frequency  
t = np.linspace(0.0, duration, nr_samples)

snr = 0.1
for phase in range(4):
	signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)
	z = np.random.normal(0, 1, 1600)

	norm_x = np.sum([x * x for x in signal])
	norm_z = np.sum([zi * zi for zi in z])

	gamma = np.sqrt(norm_x / (norm_z * snr))

	axs[0].plot(t, signal)
	axs[1].plot(t, signal + gamma * z)

	snr *= 10

axs[0].set_title("Original")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")
axs[1].set_title("Cu zgomot")
axs[1].set_xlabel("Timp")
axs[1].set_ylabel("Amplitudine")

plt.tight_layout()
plt.savefig('ex2.pdf')
plt.show()
