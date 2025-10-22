import numpy as np
import matplotlib.pyplot as plt

def sinusoid(t, A, freq, faza):
    return A * np.sin(2 * np.pi * freq * t + faza)

def cosinus(t, A, freq, faza):
    return A * np.cos(2 * np.pi * freq * t + faza)

def main():
    freq = 10
    faza = 2
    amp = 2
    start = 1.0
    end = 2.0
    samples = 1000

    signal = np.linspace(start, end, samples)
    res_sin = []
    res_cos = []
    for point in signal:
        res_sin.append(sinusoid(point, amp, freq, faza))
        res_cos.append(cosinus(point, amp, freq, 3 * np.pi / 2 + faza))

    fig, axs = plt.subplots(2)
    axs[0].plot(signal, res_sin)
    axs[1].plot(signal, res_cos)

    plt.savefig("images/ex1.pdf", format="pdf")
    plt.show()

main()
