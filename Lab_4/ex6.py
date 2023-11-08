import scipy
import numpy as np
import matplotlib.pyplot as plt

def main():
    signal_file = scipy.io.wavfile.read("ex6.wav")
    signal = signal_file[1]
    N = len(signal)

    group_size = int(0.01 * N)
    
    i = 0
    j = group_size

    group = signal[i:j]
    fft = np.fft.fft(group)
    values = abs(fft)

    spectogram = np.array(values)
    spectogram = spectogram[:, np.newaxis]

    while j <= N:
        group = signal[i:j]

        fft = np.fft.fft(group)
        values = abs(fft)

        new_column = np.array(values)
        new_column = new_column[:, np.newaxis]

        spectogram = np.append(spectogram, new_column, axis=1)

        i =  j  - (group_size // 2)
        j = i + group_size

    plt.imshow(spectogram)
    plt.savefig('ex6.png', format='png')  
    plt.savefig('ex6.pdf', format='pdf')
    plt.xlabel("Timp")
    plt.ylabel("Frecventa")
    plt.show()

if __name__ == "__main__":
    main()