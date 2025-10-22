import numpy as np
import matplotlib.pyplot as plt

freq_s = 13

def f(t):
    return np.sin(2 * np.pi * (freq_s / 2) * t)

def g(t):
    return np.sin(2 * np.pi * (freq_s / 4) * t)

def h(t):
    return np.sin(2 * np.pi * 0 / 2 * t)


def main():
    start = 1.0
    end = 8.0
    samples = 1000

    signal = np.linspace(start, end, samples)

    res1 = np.vectorize(f)(signal)
    res2 = np.vectorize(g)(signal)
    res3 = np.vectorize(h)(signal)

    fig, axs = plt.subplots(3)
    axs[0].stem(signal, res1)
    axs[1].stem(signal, res2)
    axs[2].stem(signal, res3)

    plt.savefig("images/ex6.pdf", format="pdf")
    plt.show()

main()
