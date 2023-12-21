import numpy as np
import matplotlib.pyplot as plt

def main():
    N  = 1000

    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)

    seria = trend + sezon + variatii

    train_size = int(0.8 * N)
    train_series, test_series = seria[:train_size], seria[train_size:]
    q = 5
    epsilon_train = np.random.normal(0, 1, size=N) 

    X_train = np.zeros((train_size - q, q))
    for i in range(q):
        X_train[:, i] = epsilon_train[i:train_size - q + i]

    ma_coefficients = np.linalg.lstsq(X_train, epsilon_train[q:train_size], rcond=None)[0]

    ma_model_train = np.convolve(np.concatenate((np.zeros(q), epsilon_train)), ma_coefficients, mode='same')[:train_size]

    ma_model_test = np.convolve(np.concatenate((np.zeros(q), test_series - (trend[train_size:] + sezon[train_size:]))), ma_coefficients, mode='same')[:len(test_series)]

    plt.figure(figsize=(12, 6))
    plt.plot(t, seria, label='Original Series')
    plt.plot(t[:train_size], trend[:train_size] + sezon[:train_size] + ma_model_train, label=f'Estimated MA({q}) Model (Training)')
    plt.plot(t[train_size:], trend[train_size:] + sezon[train_size:] + ma_model_test, label=f'Predicted MA({q}) Model (Testing)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()