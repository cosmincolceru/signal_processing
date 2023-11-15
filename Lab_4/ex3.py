import numpy as np
import math
import matplotlib.pyplot as plt
import time

def main():
    fs = 20
    # original signal
    f = 10
    t = np.linspace(0, 1, 1000)
    x = np.sin(-2 * np.pi * f * t)

    # sampled signal with fs = 20 Hz
    t_2 = np.linspace(0, 1, fs)
    x_2 = np.sin(-2 * np.pi * f * t_2)

    f_2 = 2
    t_3 = np.linspace(0, 1, 1000)
    x_3 = np.sin(-2 * np.pi * f_2 * t_3)

    t_3_sampled = np.linspace(0, 1, fs)
    x_3_sampled = np.sin(-2 * np.pi * f_2 * t_3_sampled)

    f_3 = 4
    t_4 = np.linspace(0, 1, 1000)
    x_4 = np.sin(-2 * np.pi * f_3 * t_4)

    t_4_sampled = np.linspace(0, 1, fs)
    x_4_sampled = np.sin(-2 * np.pi * f_3 * t_4_sampled)

    fig, axs = plt.subplots(4)

    axs[0].plot(t, x)
    axs[0].set_title("Semnal original (frecventa 10 Hz)")
    axs[0].set_xlabel("Timp")
    axs[0].set_ylabel("Amplitudine")


    axs[1].plot(t, x)
    axs[1].set_title("Semnal esantionat cu fs = 20")
    axs[1].set_xlabel("Timp")
    axs[1].set_ylabel("Amplitudine")
    axs[1].plot(t_2, x_2, 'yo')

    axs[2].plot(t_3, x_3)
    axs[2].plot(t_2, x_2, 'yo')
    axs[2].plot(t_3_sampled, x_3_sampled, 'go')
    axs[2].set_title("Semnal de frecventa 2 Hz")
    axs[2].set_xlabel("Timp")
    axs[2].set_ylabel("Amplitudine")

    axs[3].plot(t_4, x_4)
    axs[3].plot(t_2, x_2, 'yo')
    axs[3].plot(t_4_sampled, x_4_sampled, 'go')
    axs[3].set_title("Semnal de frecventa 4 Hz")
    axs[3].set_xlabel("Timp")
    axs[3].set_ylabel("Amplitudine")    

    plt.tight_layout()
    plt.savefig('ex3.png', format='png')  
    plt.savefig('ex3.pdf', format='pdf')
    plt.show()

if __name__ == "__main__":
    main()
