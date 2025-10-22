import numpy as np
import matplotlib.pyplot as plt

def sinusoid(t, A, freq, faza):
    return A * np.sin(2 * np.pi * freq * t + faza)

def shark_func(t, top):
    return np.mod(t, top)

def both(t, A, freq, faza, top):
    return np.mod(t, top) + A * np.sin(2 * np.pi * freq * t + faza)

def main():
    freq = 10
    amp = 1
    faza = 8
    start = 1.0
    end = 8.0
    samples = 1000
    top = 2

    signal = np.linspace(start, end, samples)

    res_sin = []
    res_shark = []
    res_added = []
    for point in signal:
        res_sin.append(sinusoid(point, amp, freq, faza))
        res_shark.append(shark_func(point, top))
        res_added.append(both(point, amp, freq, faza, top))

    fig, axs = plt.subplots(3)
    axs[0].plot(signal, res_sin)
    axs[1].plot(signal, res_shark)
    axs[2].plot(signal, res_added)

    plt.savefig("images/ex4.pdf", format="pdf")
    plt.show()

main()
