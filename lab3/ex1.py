import numpy as np
import matplotlib.pyplot as plt


def get_fourier(N):
    four_mat = [[ 0 for _ in range(N)] for _ in range(N)]
    for m in range(N):
        for k in range(N):
            four_mat[m][k] = np.exp((-2 * np.pi * 1j * m * k) / N)
    return four_mat


def main():
    N = 4
    four_mat = get_fourier(N)

    fig, axs = plt.subplots(N)
    for i in range(N):
        ims = [x.imag for x in four_mat[i]]
        res = [x.real for x in four_mat[i]]

        axs[i].plot(ims)
        axs[i].plot(res)

    herm_four = np.transpose(np.conjugate(four_mat))
    mult_unit = herm_four * four_mat
    for i in range(N):
        for j in range(N):
            print("({}, {})".format(four_mat[i][j].real, four_mat[i][j].imag), end=" ")
        print()

    print(np.allclose(mult_unit, np.identity(N)))
    plt.savefig("images/ex1.pdf", format="pdf")
    plt.show()


main()
