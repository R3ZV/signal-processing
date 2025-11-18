import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 100

    x = np.random.rand(N)
    signals = [x]
    curr_x = x

    for i in range(3):
        curr_x = np.convolve(curr_x, curr_x)
        signals.append(curr_x)

    _, axs = plt.subplots(4)
    for i, sig in enumerate(signals):
        axs[i].plot(sig)

    plt.savefig("images/ex2-random.pdf")
    plt.show()

    x = np.zeros(N)
    x[40:60] = 1.0

    signals = [x]
    curr_x = x

    for i in range(3):
        curr_x = np.convolve(curr_x, curr_x)
        signals.append(curr_x)

    _, axs = plt.subplots(4)
    for i, sig in enumerate(signals):
        axs[i].plot(sig)

    plt.savefig("images/ex2-block.pdf")
    plt.show()

main()
