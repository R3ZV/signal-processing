import numpy as np
import matplotlib.pyplot as plt

def trend_func(t):
    return 0.420 * t * t + t * 0.6 + 0.9

def sinus(t):
    return 3 * np.sin(2 * np.pi * 15 * t) + 5 * np.sin(2 * np.pi * 11 * t)

def ar_predict(signal, m, p):
    N = len(signal)
    err = 0.0
    predictions = []

    for chunk_start in range(m, N):
        win = signal[chunk_start - m : chunk_start]
        expected = signal[chunk_start]

        num_samples = m - p
        Y_train = np.zeros((num_samples, p))
        x_train = np.zeros(num_samples)

        for i in range(num_samples):
            Y_train[i] = win[i : i + p]
            x_train[i] = win[i + p]

        Gamma = np.dot(Y_train.T, Y_train)
        gamma_vec = np.dot(Y_train.T, x_train)
        phi = np.dot(np.linalg.inv(Gamma), gamma_vec)

        prev_ps = win[-p:]
        y_hat = np.dot(prev_ps, phi)
        predictions.append(y_hat)
        err += (y_hat - expected) ** 2

    return np.array(predictions), err

def main():
    # a)
    N = 1000
    pixel_noise = 200

    time = np.linspace(0, 1, N)
    noise = np.random.normal(size=N)
    trend = np.vectorize(trend_func)(time)
    season = np.vectorize(sinus)(time)

    signal = noise + trend + season

    _, axs = plt.subplots(4)
    axs[0].plot(time, signal)
    axs[0].set_xlabel("Time")
    axs[0].set_ylabel("Signal")

    axs[1].plot(time, trend)
    axs[1].set_xlabel("Time")
    axs[1].set_ylabel("Trend")

    axs[2].plot(season)
    axs[2].set_xlabel("Time")
    axs[2].set_ylabel("Season")

    axs[3].plot(time, noise)
    axs[3].set_xlabel("Time")
    axs[3].set_ylabel("Noise")

    plt.savefig("images/ex1.pdf")
    plt.show()

    # b)
    auto_cor = np.correlate(signal, signal, "full")
    plt.plot(auto_cor[len(auto_cor) // 2 :])
    plt.savefig("images/ex2.pdf")
    plt.show()

    # c)
    p = 2
    m = 100
    preds, _ = ar_predict(signal, m, p)

    plt.plot(time[m:], signal[m:])
    plt.plot(time[m:], preds)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.savefig("images/ex3.pdf")
    plt.show()

    best_m = 0
    best_p = 0
    min_err = 9999999

    for p in np.arange(1, 20, 2):
        for m in np.arange(10, 200, 5):
            if m <= p: 
                continue

            _, err = ar_predict(signal, m, p)
            if err < min_err:
                min_err = err
                best_m = m
                best_p = p

    print("Best m={}, p={}".format(best_m, best_p))

if __name__ == "__main__":
    main()
