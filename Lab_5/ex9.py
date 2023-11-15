import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.genfromtxt("./archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    N = len(x)
    t = np.arange(N)

    dc_offset = np.mean(x)
    x = x - dc_offset

    # moving average filter
    window_size = 15
    filtered_x = np.convolve(x, np.ones(window_size) / window_size, mode="valid")

    plt.plot(t, x, label="Semnal original")
    plt.plot(t[:len(filtered_x)], filtered_x, label="Semnal filtrat")
    plt.xlabel("Timp")
    plt.ylabel("Nr masini")
    plt.legend()
    plt.savefig("ex9.pdf", format="pdf")
    plt.savefig("ex9.png", format="png")
    plt.show()


if __name__ == "__main__":
    main()

