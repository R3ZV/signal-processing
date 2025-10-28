import numpy as np
import matplotlib.pyplot as plt

def get_fourier(N):
    four_mat = [[ 0 for _ in range(N)] for _ in range(N)]
    for m in range(N):
        for k in range(N):
            four_mat[m][k] = np.exp((-2 * np.pi * 1j * m * k) / N)
    return four_mat

def multiple_sins(x):
    return np.sin(2 * np.pi * 5 * x) + np.sin(2 * np.pi * 7 * x) + np.sin(2 * np.pi * 11 * x)

def main():
    start = 0.0
    end = 1.0
    samples = 256
    N = 256

    signal = np.linspace(start, end, samples)
    res = np.vectorize(multiple_sins)(signal)
    plt.plot(signal, res)
    plt.savefig("images/ex3-a.pdf");
    plt.show()

    fur_mat = get_fourier(N)

    mat_res = np.matmul(res, fur_mat)
    res_vec = np.abs(mat_res)

    idxs = [i for i in range(1, N + 1)]
    plt.stem(idxs, res_vec)
    plt.savefig("images/ex3-b.pdf");
    plt.show()


main()
