import numpy as np
import matplotlib.pyplot as plt


def main():
    N = 100
    x = np.random.rand(N)
    t = np.arange(N)
    
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(t, x)
    axs[0, 0].set_title("Original")

    for i in range(3):
        x = np.convolve(x, x, "full")
        N = 2 * N - 1
       

        t = np.arange(N)
        axs[(i + 1) // 2, (i + 1) % 2].plot(t, x)
        axs[(i + 1) // 2, (i + 1) % 2].set_title(f"Iteratia {i + 1}")

    plt.tight_layout()
    plt.savefig("ex1.pdf", format="pdf")
    plt.savefig("ex1.png", format="png")
    plt.show()


if __name__ == "__main__":
    main()


# x converge la o gausiana


