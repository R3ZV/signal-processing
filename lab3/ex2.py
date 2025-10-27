import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 1.0
samples = 1000

signal = np.linspace(start, end, samples)
x_n = np.vectorize(lambda x : np.sin(2 * np.pi * 5 * x + np.pi / 2))(signal)

def get_flower(omega):
    y_n = []
    for i in range(len(x_n)):
        y_n.append(x_n[i] * np.exp(-2 * np.pi * 1j * signal[i] * omega))

    x, y = [], []
    for elem in y_n:
        x.append(elem.real)
        y.append(elem.imag)

    return np.array(x), np.array(y)

def main():
    omegas = [1, 2, 5, 7]
    fig, axs = plt.subplots(len(omegas) + 1)
    for i in range(len(omegas)):
        axs[i].set_xlim(-1.1, 1.1)
        axs[i].set_ylim(-1.1, 1.1)
        axs[i].set_aspect('equal', adjustable='box')

        x, y = get_flower(omegas[i])
        dists = x ** 2 + y ** 2

        step = 15
        for k in range(0, len(x), step):
            axs[i].scatter(x[k:k+step], y[k:k+step], color=plt.cm.viridis(dists[k:k+step]))
            plt.pause(0.001)


    axs[-1].plot(signal, x_n)
    plt.tight_layout()
    plt.savefig("images/ex2.pdf", format="pdf")
    plt.show()

main()
