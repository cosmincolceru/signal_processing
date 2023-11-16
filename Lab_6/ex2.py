import numpy as np


def main():
	max_coef = 10
	min_coef = -10
	
	N = 5
	
	p_coef = np.random.randint(min_coef, max_coef, size=N)
	q_coef = np.random.randint(min_coef, max_coef, size=N)
	
	p = np.poly1d(p_coef)
	q = np.poly1d(q_coef)

	r_np = np.polymul(p, q)
	print(r_np.c)

	for _ in range(N - 1):
		np.append(p_coef, 0)
		np.append(q_coef, 0)

	P = np.fft.fft(p_coef)
	Q = np.fft.fft(q_coef)

	# R = [P[i] * Q[i] for i in range(N)]
	R = np.multiply(P,  Q)

	r = np.fft.ifft(R)

	print(r)


if __name__ == "__main__":
	main()