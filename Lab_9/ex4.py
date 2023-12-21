import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def main():
    N = 1000
    t = np.linspace(0, N, N)

    trend = 0.0001 * t * t + 0.004 * t + 3
    sezon = 10 * np.sin(2 * np.pi * 20 * t) + 20 * np.sin(2 * np.pi * 35 * t)
    variatii = np.random.normal(5, 4, size=N)
    seria = trend + sezon + variatii

    train_size = int(0.8 * N)
    train_series, test_series = seria[:train_size], seria[train_size:]

    best_aic = np.inf
    best_order = None

    for p in range(1, 21):
        for q in range(1, 21):
            try:
                model = sm.tsa.ARIMA(train_series, order=(p, 0, q))
                results = model.fit()
                aic = results.aic
                print(f'ARIMA({p}, 0, {q}) - AIC: {aic}')
                if aic < best_aic:
                    best_aic = aic
                    best_order = (p, 0, q)
            except Exception as e:
                print(f'Error for ARIMA({p}, 0, {q}): {e}')
                continue

    print(f'Best ARMA Order: {best_order} with AIC: {best_aic}')

    best_model = sm.tsa.ARIMA(train_series, order=best_order)
    best_results = best_model.fit()

    forecast = best_results.forecast(steps=len(test_series))

    plt.plot(t, seria, label='Original Series')
    plt.plot(t[train_size:], forecast, label=f'ARMA model')
    plt.legend()
    plt.show()
   

if __name__ == "__main__":
    main()