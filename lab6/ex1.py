import numpy as np
import matplotlib.pyplot as plt

def signal_f(t):
    return np.sinc(1 * t) * np.sinc(1 * t)

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
    signals = [0 for i in range(len(freq))]
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
        xs_hat = [ [] for i in range(len(signals[i]))]

        TS = 1 / freq[i]

        for t in signals[i]:
            for j in range(len(freq)):
                print(len(np.dot(xs[j], np.sinc((t - j * TS) / TS))))
                xs_hat[j].append(np.dot(xs[j], np.sinc((t - j * TS) / TS)))

        axs[i].stem(signals[i], xs[i])
        axs[i].plot(signals[i], xs_hat[i], "g--")
        axs[i].plot(signal, res)


    plt.savefig("images/ex1-b.pdf")
    plt.show()

main()
