import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.genfromtxt("./archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    N = len(x)
 
    X = np.fft.fft(x)
    X = abs(X / N)
    X = X[:N // 2]
   
    top_indices = np.argsort(X)[-4:]
    top_X_list = X[top_indices]
    
    Fs = 1 / 3600
    f = Fs * np.linspace(0, N / 2, N // 2) / N
    top_freq_list = f[top_indices]

    for x, freq in zip(top_X_list, top_freq_list):
        print(f"Modulul transformatei: {x}, frecventa: {freq}")

    plt.plot(f, X)
    plt.plot(top_freq_list, top_X_list, "yo")
    plt.xlabel("Frecventa")
    plt.ylabel("|X(x)|")
    plt.savefig("ex6.png", format="png")
    plt.savefig("ex6.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    main()


