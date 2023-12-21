import numpy as np
import matplotlib.pyplot as plt


def a(t, seria, trend, sezon, variatii):
    plt.subplot(221).plot(t, seria)
    plt.title("Sera de timp")
    plt.subplot(222).plot(t, trend)
    plt.title("Trend")
    plt.subplot(223).plot(t, sezon)
    plt.title("Sezon")
    plt.subplot(224).plot(t, variatii)
    plt.title("Variatii")
    plt.show()

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size//2:]

def b(seria):
    autocorrect_vecotr= autocorr(seria)
    autocorrect_vecotr /= np.max(autocorrect_vecotr)
    plt.plot(autocorrect_vecotr)
    plt.title("Vectorul de autocorelatie")
    plt.show()

def build_ar_model(seria, p):
    N = len(seria)
    X = np.zeros((N - p, p))
    y = seria[p:]

    # Create the feature matrix X
    for i in range(p):
        X[:, i] = seria[i:N - p + i]

    # Fit the linear regression model
    coef = np.linalg.lstsq(X, y, rcond=None)[0]

    return coef

def predict_ar_model(coef, seria, p):
    N = len(seria)
    predictions = np.zeros(N)

    for i in range(p, N):
        predictions[i] = np.dot(seria[i - p:i], coef)

    return predictions

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def find_best_parameters(seria, max_p, max_m, train_size):
    best_mse = float('inf')
    best_p = 0
    best_m = 0

    for p in range(1, max_p + 1):
        for m in range(1, max_m + 1):
            mse_values = []

            for i in range(train_size, len(seria) - m):
                train_series = seria[i - train_size:i]
                test_series = seria[i:i + m]

                # Build AR model coefficients on the training set
                coef = build_ar_model(train_series, p)

                # Predict using the AR model on the test set
                test_predictions = predict_ar_model(coef, test_series, p)

                # Calculate MSE for the current prediction
                mse_value = mse(test_series, test_predictions)
                mse_values.append(mse_value)

            avg_mse = np.mean(mse_values)

            # Update best parameters if the current combination is better
            if avg_mse < best_mse:
                best_mse = avg_mse
                best_p = p
                best_m = m

    return best_p, best_m

def main():
    N  = 1000

    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)

    seria = trend + sezon + variatii

    # a(t, seria, trend, sezon, variatii)
    # b(seria)


    train_size = int(0.8 * N)
    p = 10
    train_series, test_series = seria[:train_size], seria[train_size:]
    coef = build_ar_model(train_series, p)
    test_predictions = predict_ar_model(coef, test_series, p)

    plt.plot(t, seria, label='Original Series')
    test_t = np.linspace(train_size, N - 1, N - train_size)
    plt.plot(test_t, test_predictions, label='Predicted Series', linestyle='dashed')
    plt.title(f'AR({p}) Model Predictions on Test Set')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


