import numpy as np
import matplotlib.pyplot as plt

def sinus(t):
    return np.sin(2 * np.pi * 100 * t)


def comp_hanning(t, win_size, N):
    return 0.5 * (1 - np.cos(2 * np.pi * t / N))

def main():
    WIN_SIZE = 200
    signal_size = 1000
    signal = np.linspace(0, 1, signal_size)
    res = np.vectorize(sinus)(signal)

    filter_rect = np.ones(WIN_SIZE)
    filter_hanning = np.arange(WIN_SIZE)
    filter_hanning = 0.5 * (1 - np.cos(2 * np.pi * filter_hanning / WIN_SIZE))

    filtered_rect = res[:WIN_SIZE] * filter_rect
    filtered_hanning = res[:WIN_SIZE] * filter_hanning

    _, axs = plt.subplots(3)
    axs[0].plot(signal[:WIN_SIZE], filtered_rect)
    axs[1].plot(signal[:WIN_SIZE], filtered_hanning)
    axs[2].plot(signal, res)

    plt.savefig("images/ex5.pdf")
    plt.show()

main()
