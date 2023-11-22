import numpy as np
import matplotlib.pyplot as plt


def rectangular_window(N):
    return np.ones(N)


def hanning_window(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(N) / (N - 1)))


def main():
    N = 200
    f = 100
    a = 1
    phi = 0
    t = np.linspace(0, 0.1, N)
    x = a * np.sin(2 * np.pi * f * t + phi)
    
    rect_window = rectangular_window(N)
    hann_window = hanning_window(N)


    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(t, x)
    axs[0, 0].set_title("Semanal original")
    axs[0, 0].set_xlabel("Timp")
    axs[0, 0].set_ylabel("Amplitudine")
    
    axs[0, 1].plot(t, x * rect_window)
    axs[0, 1].set_title("Fereastra dreptunghiulara")
    axs[0, 1].set_xlabel("Timp")
    axs[0, 1].set_ylabel("Amplitudine")

    axs[1, 0].plot(t, x * hann_window)
    axs[1, 0].set_title("Fereastra Hanning")
    axs[1, 0].set_xlabel("Timp")
    axs[1, 0].set_ylabel("Amplitudine")

    axs[1, 1].plot(t, x * rect_window * hann_window)
    axs[1, 1].set_title("Semanal dreptunghiulara + Hanning")
    axs[1, 1].set_xlabel("Timp")
    axs[1, 1].set_ylabel("Amplitudine")

    plt.tight_layout();
    plt.savefig("ex3.png", format="png")
    plt.savefig("ex3.pdf", format="pdf")
    plt.show()

if __name__ == "__main__":
    main()



