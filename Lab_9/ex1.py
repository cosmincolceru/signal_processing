import numpy as np
import matplotlib.pyplot as plt

def main():
    N  = 1000

    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)

    seria = trend + sezon + variatii



    solutions = []
    alpha_values = [x / 100.0 for x in range(1, 100, 1)]
    for alpha in alpha_values:
        mediere_exponentiala = [seria[0]]
        for i in range(1, N):
            mediere_exponentiala.append(alpha * seria[i] + (1 - alpha) * seria[i - 1])

        total = 0
        for j in range(N - 1):
            total += (mediere_exponentiala[j] - seria[j + 1]) ** 2
        
        print(alpha, total)
        solutions.append(total)

    idx = np.argmin(solutions)
    print(idx, alpha_values[idx])

    mediere_exponentiala = [seria[0]]
    alpha = alpha_values[idx]
    for i in range(1, N):
        mediere_exponentiala.append(alpha * seria[i] + (1 - alpha) * seria[i - 1])

    plt.subplot(211).plot(seria)
    plt.subplot(212).plot(mediere_exponentiala)
    plt.show()


if __name__ == "__main__":
    main()