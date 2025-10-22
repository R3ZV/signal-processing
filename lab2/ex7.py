import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.sin(2 * np.pi * 5 * t)


def main():
    start = 3.0
    end = 4.0
    samples = 1000

    signal = np.linspace(start, end, samples)
    res1 = np.vectorize(f)(signal)

    signal_trimmed = signal[::4]
    trimmed = res1[::4]

    signal_trimmed2 = signal[1::4]
    trimmed2 = res1[1::4]

    fig, axs = plt.subplots(3)
    axs[0].stem(signal, res1)
    axs[1].stem(signal_trimmed, trimmed)
    axs[2].stem(signal_trimmed2, trimmed2)

    plt.savefig("images/ex7.pdf", format="pdf")
    plt.show()

main()
