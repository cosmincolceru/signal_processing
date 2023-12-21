import numpy as np
import matplotlib.pyplot as plt

def main():
    N  = 1000

    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)

    seria = trend + sezon + variatii

    plt.plot(seria)
    plt.show()


if __name__ == "__main__":
    main()