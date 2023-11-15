
import numpy as np
import math
import matplotlib.pyplot as plt

f1 = 10
f2 = 50
f3 = 35

N = 500
t = np.linspace(0, 1, N)
x = 2 * np.cos(2 * np.pi * f1 * t) + \
  	0.5 * np.cos(2 * np.pi * f2 * t) + \
		np.cos(2 * np.pi * f3 * t)

X = []
for k in range(N):
	Xi = 0
	for n in range(N):
		Xi += x[n] * math.e ** (-2j * np.pi * n * k / N)
	X.append(Xi)

modules = [abs(Xi) for Xi in X]

fig, axs = plt.subplots(1, 2)

axs[0].plot(t, x)
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")


axs[1].stem(modules)
axs[1].set_xlabel("Frecventa")
axs[1].set_ylabel("|X(ω)|")

plt.tight_layout()
plt.savefig('ex3.png', format='png')  
plt.savefig('ex3.pdf', format='pdf')
plt.show()
