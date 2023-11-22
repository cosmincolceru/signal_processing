import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, lfilter, freqz


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def b(N, x):
    t = np.arange(N)
    
    sizes = [5, 9, 13, 17, 25]
    
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].plot(t, x)
    axs[0, 0].set_title("Original")
    axs[0, 0].set_xlabel("Timp")
    axs[0, 0].set_ylabel("Nr masini")

    for i, w in enumerate(sizes):
        filtered_x = moving_average(x, w)
        axs[(i + 1) // 3, (i + 1) % 3].plot(t[:len(filtered_x)], filtered_x)
        axs[(i + 1) // 3, (i + 1) % 3].set_title(f"w = {w}")
        axs[(i + 1) // 3, (i + 1) % 3].set_xlabel("Timp")
        axs[(i + 1) // 3, (i + 1) % 3].set_ylabel("Nr masini")

    plt.tight_layout()
    plt.savefig("ex4_b.png", format="png")
    plt.savefig("ex4_b.pdf", format="pdf")
    plt.show()


def d(N, x, Wn):
    order = 5
    rp = 5 
    
    butter_b, butter_a = butter(order, Wn, btype='low', analog=False, output='ba')
    filtered_signal_butter = lfilter(butter_b, butter_a, x)

    cheby_b, cheby_a = cheby1(order, rp, Wn, btype='low', analog=False, output='ba')
    filtered_signal_cheby = lfilter(cheby_b, cheby_a, x)

    return filtered_signal_butter, filtered_signal_cheby


def e(N, x, filtered_signal_butter, filtered_signal_cheby):
    fig, axs = plt.subplots(1, 3)

    axs[0].plot(x)
    axs[0].set_title("Original")
    axs[0].set_xlabel("Timp")
    axs[0].set_ylabel("Nr masini")
    
    axs[1].plot(filtered_signal_butter)
    axs[1].set_title("Butterworth")
    axs[1].set_xlabel("Timp")
    axs[1].set_ylabel("Nr masini")

    axs[2].plot(filtered_signal_cheby)
    axs[2].set_title("Chebyshev")
    axs[2].set_xlabel("Timp")
    axs[2].set_ylabel("Nr masini")

    plt.tight_layout()
    plt.savefig("ex4_e.png", format="png")
    plt.savefig("ex4_e.pdf", format="pdf")

    plt.show()
    

def f(N, x, Wn):
    fig, axs = plt.subplots(3, 2)

    butter_b, butter_a = butter(2, Wn, btype='low', analog=False, output='ba')
    filtered_signal_butter = lfilter(butter_b, butter_a, x)
    axs[0, 0].plot(filtered_signal_butter)
    axs[0, 0].set_title("Butterworth order = 2")
    axs[0, 0].set_xlabel("Timp")
    axs[0, 0].set_ylabel("Amplitudine")

    cheby_b, cheby_a = cheby1(2, 5, Wn, btype='low', analog=False, output='ba')
    filtered_signal_cheby = lfilter(cheby_b, cheby_a, x)
    axs[0, 1].plot(filtered_signal_cheby)
    axs[0, 1].set_title("Chebyshev order = 2, rp = 5")
    axs[0, 1].set_xlabel("Timp")
    axs[0, 1].set_ylabel("Amplitudine")

    butter_b, butter_a = butter(8, Wn, btype='low', analog=False, output='ba')
    filtered_signal_butter = lfilter(butter_b, butter_a, x)
    axs[1, 0].plot(filtered_signal_butter)
    axs[1, 0].set_title("Butterworth order = 8")
    axs[1, 0].set_xlabel("Timp")
    axs[1, 0].set_ylabel("Amplitudine")

    cheby_b, cheby_a = cheby1(8, 5, Wn, btype='low', analog=False, output='ba')
    filtered_signal_cheby = lfilter(cheby_b, cheby_a, x)
    axs[1, 1].plot(filtered_signal_cheby)
    axs[1, 1].set_title("Chebyshev order = 8, rp = 5")
    axs[1, 1].set_xlabel("Timp")
    axs[1, 1].set_ylabel("Amplitudine")

    cheby_b, cheby_a = cheby1(5, 2, Wn, btype='low', analog=False, output='ba')
    filtered_signal_cheby = lfilter(cheby_b, cheby_a, x)
    axs[2, 0].plot(filtered_signal_cheby)
    axs[2, 0].set_title("Chebyshev order = 5, rp = 2")
    axs[2, 0].set_xlabel("Timp")
    axs[2, 0].set_ylabel("Amplitudine")
    
    cheby_b, cheby_a = cheby1(5, 7, Wn, btype='low', analog=False, output='ba')
    filtered_signal_cheby = lfilter(cheby_b, cheby_a, x)
    axs[2, 1].plot(filtered_signal_cheby)
    axs[2, 1].set_title("Chebyshev order = 5, rp = 7")
    axs[2, 1].set_xlabel("Timp")
    axs[2, 1].set_ylabel("Amplitudine")

    plt.tight_layout()
    plt.savefig("ex4_f.png", format="png")
    plt.savefig("ex4_f.pdf", format="pdf")

    plt.show()


def main():
    x = np.genfromtxt("../Laborator_5/archive/Train.csv", delimiter=",")
    x = x[1:, -1]
    
    # a) extrage esantionaele corespunzatoare primelor 3 zie (72 esantioane)
    N = 72
    x = x[:N]
    
    # b)
    # b(N, x)

    # c)
    Wn = 0.15
    
    # d)
    filtered_signal_butter, filtered_signal_cheby = d(N, x, Wn)

    # e)
    # e(N, x, filtered_signal_butter, filtered_signal_cheby)

    # f)
    f(N, x, Wn)


if __name__ == "__main__":
    main()


