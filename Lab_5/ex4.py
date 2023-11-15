import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    x = np.genfromtxt("./archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    N = len(x)

    X = np.fft.fft(x)
    X = abs(X / N)
    X = X[:N // 2]

    Fs = 1 / 3600
    f = Fs * np.linspace(0, N / 2, N // 2) / N

    plt.plot(f, X)
    plt.savefig('ex4.png', format='png')  
    plt.savefig('ex4.pdf', format='pdf')
    
    plt.xlabel("Frecventa")
    plt.ylabel("|X(x)|")
    plt.show()


if __name__ == "__main__":
    main()
