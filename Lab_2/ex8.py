import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi/2, np.pi/2, 1000)

sin_alpha = np.sin(alpha)

pade_approximation = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

error_alpha = np.abs(sin_alpha - alpha)
error_pade = np.abs(sin_alpha - pade_approximation)

fig, axs = plt.subplots(3, 1)

axs[0].plot(alpha, sin_alpha, label='sin(α)')
axs[0].plot(alpha, alpha, label='α')
axs[0].plot(alpha, pade_approximation, label='Aproximare Pade')
axs[0].set_title('Comparare α si sin(α)')
axs[0].legend()

axs[1].plot(alpha, error_alpha, label='Eroare între sin(α) și α')
axs[1].set_title('Eroare sin(α)')
axs[1].legend()

axs[2].plot(alpha, error_pade, label='Eroare între sin(α) și aproximarea Pade')
axs[2].set_title('Eroare proximarea Pade')
axs[2].legend()


plt.tight_layout()
plt.savefig("ex8.pdf")
plt.show()
