import numpy as np

N = 5

def poly_mult(p, q):
    p_poly = np.poly1d(p)
    q_poly = np.poly1d(q)

    r_np = np.polymul(p_poly, q_poly)
    return r_np.c


def fft_mult(p, q):
    size = 2 ** (int(np.log2(len(p) + len(q) - 1)) + 1)

    P = np.fft.fft(p, size)
    Q = np.fft.fft(q, size)

    R = P * Q

    r = np.fft.ifft(R)

    return np.real(r[:(2 * N - 1)])


def main():
    max_coef = 10
    min_coef = -10
        
    p = np.random.randint(min_coef, max_coef, size=N)
    q = np.random.randint(min_coef, max_coef, size=N)
    
    print(poly_mult(p, q))
    print(fft_mult(p, q))


if __name__ == "__main__":
    main()
