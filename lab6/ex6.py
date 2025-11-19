import scipy
import numpy as np
import matplotlib.pyplot as plt

def sinus(t):
    return np.sin(2 * np.pi * 100 * t)


def comp_hanning(t, win_size, N):
    return 0.5 * (1 - np.cos(2 * np.pi * t / N))

def main():
    # a)
    data = np.genfromtxt("Train.csv", delimiter=',')[1:, 2]
    signal = data[50:50 + 24 * 3]

    # b)
    w = 7
    filtered = np.convolve(signal, np.ones(w), 'valid') / w
    plt.plot(filtered)
    plt.savefig("images/ex6-a.pdf")
    plt.show()

    # c)
    # In datele din Train.csv se esantioneaza o data la 1 ora
    samp_freq = 1 / 3600
    wn_freq = samp_freq / 7 # not sure how to choose this
    nyq_freq = samp_freq / 2

    # d)
    deg = 5
    rp = 5
    res_butter = scipy.signal.butter(deg, wn_freq, btype='low')
    res_cheb = scipy.signal.cheby1(deg, rp, wn_freq, btype='low')

    _, axs = plt.subplots(2)
    axs[0].plot(res_butter)
    axs[1].plot(res_cheb)
    plt.savefig("images/ex6-b.pdf")
    plt.show()

    # e)
    # f)

main()
