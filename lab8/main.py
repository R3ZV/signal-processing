import numpy as np
import matplotlib.pyplot as plt

def trend_func(t):
    return 0.420 * t * t + t * 0.6 + 0.9

def sinus(t):
    return 3 * np.sin(2 * np.pi * 15 * t) + 5 * np.sin(2 * np.pi * 11 * t)

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

    plt.savefig("images/ex1-a.pdf")
    plt.show()

    # b)
    P = 2
    auto_cor = [0 for _ in range(N)]
    for i in range(P, N):
        for j in range(1, P + 1):
            auto_cor[i] += signal[j] * signal[i - j]

    plt.plot(time, auto_cor)
    plt.savefig("images/ex1-b.pdf")
    plt.show()

    # c)

if __name__ == "__main__":
    main()
