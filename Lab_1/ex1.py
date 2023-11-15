import matplotlib.pyplot as plt
import numpy as np

def x(t):
	return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
	return np.cos(280 * np.pi * t + np.pi / 3)

def z(t):
	return np.cos(120 * np.pi * t + np.pi / 3)


def b():
	# axa reala de timp
	samples = np.linspace(0, 0.03, int(0.03 / 0.0005))
	
	fig, axs = plt.subplots(3, 1)

	axs[0].plot(samples, x(samples))
	axs[0].set_title('x(t)')
	axs[0].set_xlabel('Timp')
	axs[0].set_ylabel('Amplitudine')

	axs[1].plot(samples, y(samples))
	axs[1].set_title('y(t)')
	axs[1].set_xlabel('Timp')
	axs[1].set_ylabel('Amplitudine')

	axs[2].plot(samples, z(samples))
	axs[2].set_title('z(t)')
	axs[2].set_xlabel('Timp')
	axs[2].set_ylabel('Amplitudine')

	plt.tight_layout()
	plt.savefig('ex1b.pdf')
	plt.show()

def c():
	samples_cont = np.linspace(0, 0.25, 1000)
	samples = np.linspace(0, 0.25, 50)

	fig, axs = plt.subplots(3, 1)
	axs[0].plot(samples_cont, x(samples_cont))
	axs[0].stem(samples, x(samples))
	axs[0].set_title('x(t)')
	axs[0].set_xlabel('Timp')
	axs[0].set_ylabel('Amplitudine')

	axs[1].plot(samples_cont, y(samples_cont))
	axs[1].stem(samples, y(samples))
	axs[1].set_title('y(t)')
	axs[1].set_xlabel('Timp')
	axs[1].set_ylabel('Amplitudine')

	axs[2].plot(samples_cont, z(samples_cont))
	axs[2].stem(samples, z(samples))
	axs[2].set_title('z(t)')
	axs[2].set_xlabel('Timp')
	axs[2].set_ylabel('Amplitudine')

	plt.tight_layout()
	plt.savefig('ex1c.pdf')
	plt.show()

c()