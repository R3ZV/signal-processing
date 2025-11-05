import numpy as np
import matplotlib.pyplot as plt

f_freq = 3

def sinus1(x):
    return np.sin(2 * np.pi * f_freq * 2 * x)

def sinus2(x):
    return np.sin(2 * np.pi * f_freq * 3 * x)

def sinus3(x):
    return np.sin(2 * np.pi * f_freq * 5 * x)


def main():
    x = np.linspace(0, 1, 1000)
    signal1 = np.vectorize(sinus1)(x)
    signal2 = np.vectorize(sinus2)(x)
    signal3 = np.vectorize(sinus3)(x)

    # > 2 * max_freq
    nyquist_sampling = np.linspace(0, 1, 2 * f_freq * 5)
    ny_res1 = np.vectorize(sinus1)(nyquist_sampling)
    ny_res2 = np.vectorize(sinus2)(nyquist_sampling)
    ny_res3 = np.vectorize(sinus3)(nyquist_sampling)

    fig, axs = plt.subplots(3)

    axs[0].plot(x, signal1)
    axs[0].scatter(nyquist_sampling, ny_res1, color="r")

    axs[1].plot(x, signal2)
    axs[1].scatter(nyquist_sampling, ny_res2, color="r")

    axs[2].plot(x, signal3)
    axs[2].scatter(nyquist_sampling, ny_res3, color="r")

    plt.savefig("images/ex3.pdf")
    plt.show()

main()
