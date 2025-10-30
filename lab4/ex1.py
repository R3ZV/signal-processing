import matplotlib.pyplot as plt
from time import perf_counter
import numpy as np

def get_fourier(N):
    four_mat = [[ 0 for _ in range(N)] for _ in range(N)]
    for m in range(N):
        for k in range(N):
            four_mat[m][k] = np.exp((-2 * np.pi * 1j * m * k) / N)
    return four_mat

def multiple_sins(x):
    return np.sin(2 * np.pi * 5 * x) + np.sin(2 * np.pi * 7 * x) + np.sin(2 * np.pi * 11 * x)

def my_fft(x):
    N = int(len(x))
    if N <= 1:
        return x

    X_even = my_fft(x[::2])
    X_odd = my_fft(x[1::2])
    fact = np.exp(-2j * np.pi * np.arange(N) / N)
    X = np.concatenate(\
            [X_even + fact[:int(N/2)] * X_odd,
            X_even + fact[int(N/2):] * X_odd]
    )

    return X


def main():
    N = [128, 256, 512, 1024, 2048, 4096, 8192]
    times = [[], [], []]
    for n in N:
        start = 0.0
        end = 1.0
        samples = n

        signal = np.linspace(start, end, samples)
        res = np.vectorize(multiple_sins)(signal)
        fur_mat = get_fourier(n)

        t_start = perf_counter()
        np.matmul(res, fur_mat)
        t_end = perf_counter()
        elapsed = t_end - t_start
        times[0].append(elapsed * 1000)
        print(f"N = [{n}] Elapsed time for DFT:", elapsed)

        t_start = perf_counter()
        my_fft(res)
        t_end = perf_counter()
        elapsed = t_end - t_start
        times[1].append(elapsed * 1000)
        print(f"N = [{n}] Elapsed time for MY FFT:", elapsed)

        t_start = perf_counter()
        fur_mat = np.fft.fft(res)
        t_end = perf_counter()
        elapsed = t_end - t_start
        times[2].append(elapsed * 1000)
        print(f"N = [{n}] Elapsed time for NP FFT:", elapsed)

    plt.plot(N, times[0])
    plt.plot(N, times[1])
    plt.plot(N, times[2])
    plt.yscale("log")
    plt.savefig("images/ex1.pdf");
    plt.show()

main()
