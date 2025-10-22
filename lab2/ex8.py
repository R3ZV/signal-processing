import numpy as np
import matplotlib.pyplot as plt

def sinx(t):
    return np.sin(t)

def sin_small(t):
    return t

def sin_pade(t):
    x = t - (7 * t**3) / 60
    y = 1 + t ** 2 / 20;
    return x / y


def main():
    start = -np.pi / 2
    end = np.pi / 2
    samples = 1000

    signal = np.linspace(start, end, samples)

    res1 = np.vectorize(sinx)(signal)
    res2 = np.vectorize(sin_small)(signal)
    res3 = np.vectorize(sin_pade)(signal)

    fig, axs = plt.subplots(5)
    axs[0].plot(signal, res1)
    axs[1].plot(signal, res2)
    axs[2].plot(signal, res3)
    axs[3].plot(signal, res1 - res2)
    axs[4].plot(signal, res1 - res3)

    plt.savefig("images/ex8-a.pdf", format="pdf")
    plt.show()

    # log scale
    fig, axs = plt.subplots(5)
    axs[0].plot(signal, res1)
    axs[0].set_yscale('log')

    axs[1].plot(signal, res2)
    axs[1].set_yscale('log')

    axs[2].plot(signal, res3)
    axs[2].set_yscale('log')

    axs[3].plot(signal, res1 - res2)
    axs[3].set_yscale('log')

    axs[4].plot(signal, res1 - res3)
    axs[4].set_yscale('log')

    plt.savefig("images/ex8-b.pdf", format="pdf")
    plt.show()

main()
