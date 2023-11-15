import numpy as np
import math
import matplotlib.pyplot as plt

N = 8
X = []

F = np.zeros((N, N), dtype=np.complex128)
for i in range(N):
	for k in range(N):
		F[i, k] = math.e ** (-2 * np.pi * 1j * k * i  / N)

fig, axs = plt.subplots(N, figsize=(5, 8))

for i in range(N):
    axs[i].plot(np.real(F[i, :]))
    axs[i].set_title(f'Row {i+1}')

    axs[i].plot(np.imag(F[i, :]))
    axs[i].set_title(f'Row {i+1}')

print(np.allclose(np.eye(N), F.dot(F.T.conj()) / N, atol=1e-3))


plt.tight_layout()

plt.savefig('ex1.png', format='png')  
plt.savefig('ex1.pdf', format='pdf')

# plt.show()
