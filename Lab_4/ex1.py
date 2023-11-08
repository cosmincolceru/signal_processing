import numpy as np
import math
import matplotlib.pyplot as plt
import time

def main():
    f1 = 10
    f2 = 50
    f3 = 35
    f4 = 40

    N_values = [128, 256, 512, 1024, 2048, 4096, 8192]

    matrix_times = []
    numpy_times = []

    for N in N_values:
        t = np.linspace(0, 1, N)
        x = 2 * np.cos(2 * np.pi * f1 * t) + \
                0.5 * np.cos(2 * np.pi * f2 * t) + \
                    np.cos(2 * np.pi * f3 * t) + \
                        np.cos(2 * np.pi * f4 * t)
        
        start = time.time()
        F = np.zeros((N, N), dtype=np.complex128)
        for i in range(N):
            for k in range(N):
                F[i, k] = math.e ** (-2 * np.pi * 1j * k * i  / N)

        X = np.dot(F, x)
        finish = time.time()

        matrix_time = finish - start
        print(f"N = {N}")
        print(f"X = Fx: {matrix_time}")
        matrix_times.append(matrix_time)

        start = time.time()
        for _ in range(10000):
            X_2 = np.fft.fft(x)
        finish = time.time()
        
        numpy_time = (finish - start) / 10000
        print(f'Numpy.fft: {numpy_time}')
        numpy_times.append(numpy_time)

    print(N_values)
    print(matrix_times)
    print(numpy_times)	

    plt.plot(N_values, matrix_times, label="Matrice")
    plt.plot(N_values, numpy_times, label="Numpy")
    plt.yscale("log")
    plt.grid()
    plt.legend()

    plt.savefig('ex1.png', format='png')  
    plt.savefig('ex1.pdf', format='pdf')
    plt.show()

if __name__ == "__main__":
    main()