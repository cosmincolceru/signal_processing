import numpy as np
import matplotlib.pyplot as plt
import csv


def main():
    x = np.genfromtxt("./archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    N = len(x)

    first_sample = 1056     # luni, 8.10.2012
    no_of_samples = 730     # nr de ore intr-o luna

    x = x[first_sample:first_sample + no_of_samples]
    t = np.arange(730)

    plt.plot(t, x)
    plt.title("O luna de trafic")
    plt.xlabel("Timp")
    plt.ylabel("Trafic")
    plt.savefig('ex7.png', format='png')  
    plt.savefig('ex7.pdf', format='pdf')
    plt.show()


if __name__ == "__main__":
    main()
