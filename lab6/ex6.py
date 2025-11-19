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
    nyq_freq = samp_freq / 2
    wn_freq = (samp_freq / 7) / nyq_freq

    # d)
    deg = 5
    rp = 5
    res_butter = scipy.signal.butter(deg, wn_freq, btype='low')
    res_cheb = scipy.signal.cheby1(deg, rp, wn_freq, btype='low')

    filt_butter = scipy.signal.filtfilt(*res_butter, signal)
    filt_cheb = scipy.signal.filtfilt(*res_cheb, signal)

    # e)
    plt.plot(np.arange(len(signal)), signal)
    plt.plot(np.arange(len(filt_butter)), filt_butter, c='g')
    plt.plot(np.arange(len(filt_cheb)), filt_cheb, c='r')
    plt.savefig("images/ex6-b.pdf")
    plt.show()

    # As alege butter pentru ca pare a urmari mai bine trendul semnalului
    # original.

    # f)
    rps = [3, 5, 9, 11]
    degs = [2, 9, 13]

    for r in rps:
        for d in degs:
            res_butter = scipy.signal.butter(d, wn_freq, btype='low')
            res_cheb = scipy.signal.cheby1(d, r, wn_freq, btype='low')

            filt_butter = scipy.signal.filtfilt(*res_butter, signal)
            filt_cheb = scipy.signal.filtfilt(*res_cheb, signal)

            plt.plot(np.arange(len(signal)), signal)
            plt.plot(np.arange(len(filt_butter)), filt_butter, c='g')
            plt.plot(np.arange(len(filt_cheb)), filt_cheb, c='r')
            plt.savefig(f"images/ex6-f-r{r}-d{d}.pdf")
            plt.show()

main()
