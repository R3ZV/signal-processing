import numpy as np
import matplotlib.pyplot as plt

def trend_func(t):
    return 0.420 * t * t + t * 0.6 + 0.9

def sinus(t):
    return 3 * np.sin(2 * np.pi * 15 * t) + 5 * np.sin(2 * np.pi * 11 * t)

def exp1(signal, alpha):
    pred = np.zeros(len(signal))
    pred[0] = signal[0]
    err = 0.0
    for i in range(1, len(pred) - 1):
        pred[i] = alpha * signal[i] + (1 - alpha) * pred[i - 1]
        err += (pred[i] - signal[i + 1]) ** 2

    return pred, err

def exp2(signal, alpha, beta):
    pred = np.zeros(len(signal))
    s = np.zeros(len(signal))
    b = np.zeros(len(signal))

    s[0] = signal[0]
    b[0] = signal[1] - signal[0]

    err = 0.0
    for i in range(1, len(s) - 1):
        s[i] = alpha * signal[i] + (1 - alpha) * (s[i - 1] + b[i - 1])
        b[i] = beta * (s[i] - s[i - 1]) + (1 - beta) * b[i - 1]

    m = 1
    for t in range(len(s) - m):
        pred[t + m] = s[t] + m * b[t]
        err += (pred[t + m] - signal[t + m]) ** 2

    return pred, err

def exp3(signal, alpha, beta, sigma):
    L = 3
    pred = np.zeros(len(signal))
    s = np.zeros(len(signal))
    b = np.zeros(len(signal))
    c = np.zeros(len(signal))

    s[0] = signal[0]
    b[0] = signal[1] - signal[0]
    c[0] = 0

    err = 0.0
    for i in range(L, len(s) - 1):
        s[i] = alpha * signal[i] + (1 - alpha) * (s[i - 1] + b[i - 1])
        b[i] = beta * (s[i] - s[i - 1]) + (1 - beta) * b[i - 1]
        c[i] = sigma * (signal[i] - s[i] - b[i - 1] + (1 - sigma) * c[i - L])

    m = 1
    for t in range(len(s) - m):
        pred[t + m] = s[t] + m * b[t] + c[t - L + 1 + (m - 1) % L]
        err += (pred[t + m] - signal[t + m]) ** 2

    return pred, err

def ma_model(signal, q):
    N = len(signal)
    ma = np.zeros(N)
    errs = np.zeros(N)

    for i in range(q - 1, N):
        window = signal[i - q + 1 : i + 1]
        mean_val = np.mean(window)
        ma[i] = mean_val
        errs[i] = signal[i] - mean_val

    return ma, errs

def main():
    N = 1000
    pixel_noise = 200

    time = np.linspace(0, 1, N)
    noise = np.random.normal(size=N)
    trend = np.vectorize(trend_func)(time)
    season = np.vectorize(sinus)(time)
    signal = noise + trend + season

    _, axs = plt.subplots(4)
    axs[0].plot(time, signal)
    axs[0].set_title("Original")

    alphas = np.linspace(0, 1, 20)
    min_err = 999999
    best_alpha = 0
    for i in range(len(alphas)):
        alpha = alphas[i]
        pred, err = exp1(signal, alpha)
        if err < min_err:
            min_err = err
            best_alpha = i

    pred, err = exp1(signal, alphas[best_alpha])
    axs[1].plot(time, pred)
    axs[1].set_title("Exp 1")
    print("Exp1: err={}, best_alpha={}".format(err, alphas[best_alpha]))

    betas = np.linspace(0, 1, 20)
    min_err = 999999
    best_alpha = 0
    best_beta = 0
    for i in range(len(alphas)):
        alpha = alphas[i]
        for j in range(len(betas)):
            beta = betas[j]

            pred, err = exp2(signal, alpha, beta)
            if err < min_err:
                min_err = err
                best_alpha = i
                best_beta = j

    pred, err = exp2(signal, alphas[best_alpha], betas[best_beta])
    axs[2].plot(time, pred)
    axs[2].set_title("Exp 2")
    print("Exp2: err={}, best_alpha={}, best_beta={}".format(err, alphas[best_alpha], betas[best_beta]))

    sigmas = np.linspace(0, 1, 20)
    min_err = 999999
    best_alpha = 0
    best_beta = 0
    best_sigma = 0
    for i in range(len(alphas)):
        alpha = alphas[i]
        for j in range(len(betas)):
            beta = betas[j]
            for k in range(len(sigmas)):
                sigma = sigmas[k]

                pred, err = exp3(signal, alpha, beta, sigma)
                if err < min_err:
                    min_err = err
                    best_alpha = i
                    best_beta = j
                    best_sigma = k

    pred, err = exp3(signal, alphas[best_alpha], betas[best_beta], sigmas[best_sigma])
    axs[3].plot(time, pred)
    axs[3].set_title("Exp 3")
    print("Exp3: err={}, best_alpha={}, best_beta={}, best_sigma={}".format(err, alphas[best_alpha], betas[best_beta], sigmas[best_sigma]))

    plt.savefig("images/ex2.pdf")
    plt.show()

    q = 50
    ma_res, errs = ma_model(signal, q)
    plt.plot(time[q-1:], ma_res[q-1:])
    plt.show()
    plt.savefig("images/ex3-a.pdf")

    plt.plot(time[q-1:], errs[q-1:])

    plt.savefig("images/ex3-b.pdf")
    plt.show()


if __name__ == "__main__":
    main()
