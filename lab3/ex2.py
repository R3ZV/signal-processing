import numpy as np
import matplotlib.pyplot as plt

def plot_flower(omega):
    start = 0.0
    end = 1.0
    samples = 1000

    signal = np.linspace(start, end, samples)
    x_n = np.vectorize(lambda x : np.sin(2 * np.pi * 5 * x))(signal)
    y_n = []
    for i in range(len(x_n)):
        y_n.append(x_n[i] * np.exp(-2 * np.pi * 1j * signal[i]))

    x, y = [], []
    for elem in y_n:
        x.append(elem.real)
        y.append(elem.imag)

    plt.plot(x, y)

    plt.savefig("images/ex2-a.pdf", format="pdf")

def main():
    plt.show()


main()
