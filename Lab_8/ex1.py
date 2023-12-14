import numpy as np
import matplotlib.pyplot as plt


def a(t, seria, trend, sezon, variatii):
    plt.subplot(221).plot(t, seria)
    plt.title("Sera de timp")
    plt.subplot(222).plot(t, trend)
    plt.title("Trend")
    plt.subplot(223).plot(t, sezon)
    plt.title("Sezon")
    plt.subplot(224).plot(t, variatii)
    plt.title("Variatii")
    plt.show()

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size//2:]

def b(seria):
    autocorrect_vecotr= autocorr(seria)
    autocorrect_vecotr /= np.max(autocorrect_vecotr)
    plt.plot(autocorrect_vecotr)
    plt.title("Vectorul de autocorelatie")
    plt.show()

def main():
    N  = 1000

    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)

    seria = trend + sezon + variatii

    a(t, seria, trend, sezon, variatii)
    b(seria)

if __name__ == "__main__":
    main()


