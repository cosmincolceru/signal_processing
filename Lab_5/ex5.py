import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.genfromtxt("./archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    N = len(x)
    t = np.arange(N)

    dc_offset = np.mean(x)
    print(f"DC offest = {dc_offset}")
    
    x_no_offset = x - dc_offset
    
    fig, axs = plt.subplots(1, 2)

    axs[0].plot(t, x)
    axs[0].set_title("Semanl original")
    axs[0].set_xlabel("Timp")
    axs[0].set_ylabel("Nr masini")

    axs[1].plot(t, x_no_offset)
    axs[1].set_title("Semnal fara componenta cotinua")
    axs[1].set_xlabel("Timp")
    axs[1].set_ylabel("Nr masini")

    plt.tight_layout()
    plt.savefig("ex5.pdf", format="pdf")
    plt.savefig("ex5.png", format="png")
    plt.show()


if __name__ == "__main__":
    main()
