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

    # a)
    signal = np.linspace(start, end, samples)

    # b)
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

    # c)
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

def square_func(t, top):
    pass

def exe2():
    # a)
    start = 0
    end = 4.0
    samples = 1600
    freq = 400

    signal = np.linspace(start, end, samples)
    res = []

    for point in signal:
        res.append(sinusoid(point, 1.0, freq, 0.0))

    fig, axs = plt.subplots(4)
    axs[0].stem(signal, res)

    # b)
    start = 0
    end = 3.0
    freq = 800
    samples = 100

    signal = np.linspace(start, end, samples)
    res = []

    for point in signal:
        res.append(sinusoid(point, 1.0, freq, 0.0))

    axs[1].plot(signal, res)

    # c)
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

    # d)
    start = 0
    end = 10.0
    freq = 300
    samples = 1500

    signal = np.linspace(start, end, samples)
    res = []

    for point in signal:
        res.append(np.sign(sinusoid(point, 1, freq, 0)))

    axs[3].plot(signal, res)

    plt.savefig("images/ex2.pdf", format="pdf")
    plt.show()

    # e)
    rand_signal = np.random.rand(128, 128)
    plt.imshow(rand_signal)
    plt.savefig("images/ex2-rand.pdf", format="pdf")
    plt.show()

    # f)
    signal_2d = np.zeros((128, 128))
    for i in range(128):
        for j in range(128):
            signal_2d[i][j] = euler_identity(i + 1, j + 1)

    plt.imshow(signal_2d)
    plt.savefig("images/ex2-mysignal.pdf", format="pdf")
    plt.show()

# not really but close
def euler_identity(i, j):
    # this one is kind of cool too
    # return np.exp(np.pi * 1j * (j % i))

    return np.exp(np.pi * 1j * (j % i) / i)

def exe3():
    # a)
    # Avand 2000 Hz inseamna ca intr-o secunda am facut 2000 esantioane
    # delimitate egal.
    # Deci se esantioneaza la fiecare 1 / 2000 = 0.005 secunde

    # b) Avem 2000 esantioane pe secunda, 1 ora are 3600 secunde
    # deci 7_200_000 esantioane deci 7_200_000 * 4 biti
    # 3_600_000 B = 3600 KB = 3.6 MB

    print("Check code comments")

def main():
    exe1()
    exe2()
    exe3()

if __name__ == "__main__":
    main()
