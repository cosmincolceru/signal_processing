import numpy as np
import math
import matplotlib.pyplot as plt

f = 10
fs = 20 * 20
t = np.linspace(0, 1, fs)
x = np.sin(2 * np.pi * f * t)

def fig1():
	N = fs 
	n = np.arange(N)
	y = x * math.e ** (-2j * np.pi * n / N)

	fig, axs = plt.subplots(1, 2)

	rl = [i.real for i in y]
	im = [i.imag for i in y]

	axs[0].plot(t, x)
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")

	axs[1].plot(rl, im)
	axs[1].set_xlabel("Real")
	axs[1].set_ylabel("Imaginar")

	# magnitude = np.abs(y)
	# for i in range(N):
	# 	color = plt.cm.viridis(magnitude[i] / np.max(magnitude))  
	# 	axs[1].plot(y[i].real, y[i].imag, marker='o', markersize=3, color=color)

	plt.tight_layout()

	plt.savefig('ex2_1.png', format='png')  
	plt.savefig('ex2_1.pdf', format='pdf')

	plt.show()

def fig2():
	omega = [1, 5, 10, 20]

	N = fs
	n = np.arange(N)

	fig, axs = plt.subplots(2, 2)

	for i, o in enumerate(omega):	
		z = x * math.e ** (-2j * np.pi * o * n / N)

		rl = [i.real for i in z]
		im = [i.imag for i in z]
		
		axs[i // 2, i % 2].plot(rl, im)
		axs[i // 2, i % 2].set_title(f'ω= {o}Hz')
		axs[i // 2, i % 2].set_xlabel("Real")
		axs[i // 2, i % 2].set_ylabel("Imaginar")

	plt.tight_layout()
	plt.savefig('ex2_2.png', format='png')  
	plt.savefig('ex2_2.pdf', format='pdf')
	plt.show()

fig2()
