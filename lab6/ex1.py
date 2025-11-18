import numpy as np
import matplotlib.pyplot as plt

B = 1

def signal_f(t):
    return np.sinc(B * t) * np.sinc(B * t)

def main():
    freq = [1, 1.5, 2, 4]
    start_idx = -3
    end_idx = 3

    signal = np.linspace(start_idx, end_idx, 1000)
    res = np.vectorize(signal_f)(signal)
    plt.plot(signal, res)
    plt.savefig("images/ex1-a.pdf")
    plt.show()

    # b)
    signals = [[] for i in range(len(freq))]
    for i in range(len(freq)):
        samples = int(freq[i] * (end_idx - start_idx))

        # 1 more ot make sure we get 0
        if samples % 2 == 0:
            samples += 1

        signals[i] = np.linspace(start_idx, end_idx, samples)

    xs = [[] for i in range(len(freq))]
    fig, axs = plt.subplots(len(freq))
    for i in range(len(freq)):
        xs[i] = np.vectorize(signal_f)(signals[i])
        TS = 1 / freq[i]

        def rec(t):
            kernel = np.sinc(B * (t - signals[i]) / TS)
            return np.dot(xs[i], kernel)

        xs_hat = []
        for t in signal:
            xs_hat.append(rec(t))

        axs[i].plot(signal, res)
        axs[i].stem(signals[i], xs[i])
        axs[i].plot(signal, xs_hat, "g--")


    plt.savefig("images/ex1-b.pdf")
    plt.show()

main()
