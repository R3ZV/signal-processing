import numpy as np
import matplotlib.pyplot as plt

def fx(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def fy(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def fz(t):
    return np.cos(120 * np.pi * t + np.pi / 3)

def exe1():
    start = 0.0
    end = 0.03
    step = 0.0005
    samples = int(end / step)

    signal = np.linspace(start, end, samples)
    fx_res = []
    fy_res = []
    fz_res = []

    for point in signal:
        fx_res.append(fx(point))
        fy_res.append(fy(point))
        fz_res.append(fz(point))

    fig, axs = plt.subplots(3)
    axs[0].plot(signal, fx_res)
    axs[1].plot(signal, fy_res)
    axs[2].plot(signal, fz_res)

    freq = 200
    samples = int(freq * end)
    signal2 = np.linspace(start, end, samples)
    fx_res2 = []
    fy_res2 = []
    fz_res2 = []

    for point in signal2:
        fx_res2.append(fx(point))
        fy_res2.append(fy(point))
        fz_res2.append(fz(point))

    axs[0].stem(signal2, fx_res2)
    axs[1].stem(signal2, fy_res2)
    axs[2].stem(signal2, fz_res2)

    plt.savefig("images/ex1.pdf", format="pdf")
    plt.show()


def sinusoid(t, A, freq, delta):
    return A * np.sin(2 * np.pi * freq * t + delta)


def shark_func(t, top):
    return np.mod(t, top)

def exe2():
    start = 0
    end = 4.0
    samples = 1600
    freq = 400

    signal = np.linspace(start, end, samples)
    res = []

    for point in signal:
        res.append(sinusoid(point, 1.0, freq, 0.0))

    fig, axs = plt.subplots(3)
    axs[0].stem(signal, res)

    start = 0
    end = 3.0
    freq = 800
    samples = 100

    signal = np.linspace(start, end, samples)
    res = []

    for point in signal:
        res.append(sinusoid(point, 1.0, freq, 0.0))

    axs[1].plot(signal, res)

    start = 0
    end = 10.0
    freq = 240
    samples = 1000

    signal = np.linspace(start, end, samples)
    res = []

    top = 2
    for point in signal:
        res.append(shark_func(point, top))

    axs[2].plot(signal, res)

    plt.savefig("images/ex2.pdf", format="pdf")
    plt.show()

def main():
    # exe1()
    exe2()

if __name__ == "__main__":
    main()
