import numpy as np
import matplotlib.pyplot as plt

def sinusoid(t, A, freq, faza):
    return A * np.sin(2 * np.pi * freq * t + faza)

def main():
    freq = 10
    amp = 1
    faze = [2, 4, 8, 16]
    start = 1.0
    end = 2.0
    samples = 1000

    signal = np.linspace(start, end, samples)
    res = [[] for _ in range(len(faze))]
    for i in range(len(faze)):
        for point in signal:
            res[i].append(sinusoid(point, amp, freq, faze[i]))

    for i in range(len(faze)):
        plt.plot(signal, res[i])

    plt.savefig("images/ex2-a.pdf", format="pdf")
    plt.show()

    snrs = [0.1, 1, 10, 100]
    noise = np.random.normal(0, 0.1, samples)
    fig, axs = plt.subplots(len(snrs))
    for j in range(len(snrs)):
        gamma = np.sqrt(np.linalg.norm(res[0]) ** 2 / (snrs[j] * np.linalg.norm(noise)**2))
        new_signal = []
        for i in range(len(res[0])):
            new_signal.append(res[0][i] + gamma * noise[i])

        axs[j].plot(signal, new_signal)

    plt.savefig("images/ex2-b.pdf", format="pdf")
    plt.show()

main()
