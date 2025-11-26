from skimage import data

from scipy import ndimage, datasets
import numpy as np
import matplotlib.pyplot as plt

def func1(n1, n2):
    return np.sin(2 * np.pi * n1 + 3 * np.pi * n2)

def func2(n1, n2):
    return np.sin(4 * np.pi * n1) + np.cos(6 * np.pi * n2)

def main():
    # LAB INFO

    # X = datasets.face(gray=True)
    # plt.imshow(X, cmap=plt.cm.gray)
    # plt.show()
    #
    # Y = np.fft.fft2(X)
    # freq_db = 20*np.log10(abs(Y))
    #
    # plt.imshow(freq_db)
    # plt.colorbar()
    # plt.show()
    #
    # rotate_angle = 45
    # X45 = ndimage.rotate(X, rotate_angle)
    # plt.imshow(X45, cmap=plt.cm.gray)
    # plt.show()
    #
    # Y45 = np.fft.fft2(X45)
    # plt.imshow(20*np.log10(abs(Y45)))
    # plt.colorbar()
    # plt.show()
    #
    # freq_x = np.fft.fftfreq(X.shape[1])
    # freq_y = np.fft.fftfreq(X.shape[0])
    #
    # plt.stem(freq_x, freq_db[:][0])
    # plt.show()
    #
    # freq_cutoff = 120
    #
    # Y_cutoff = Y.copy()
    # Y_cutoff[freq_db > freq_cutoff] = 0
    # X_cutoff = np.fft.ifft2(Y_cutoff)
    # X_cutoff = np.real(X_cutoff)    # avoid rounding erros in the complex domain,
    #                                 # in practice use irfft2
    # plt.imshow(X_cutoff, cmap=plt.cm.gray)
    # plt.show()
    #
    # pixel_noise = 200
    #
    # noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=X.shape)
    # X_noisy = X + noise
    # plt.imshow(X, cmap=plt.cm.gray)
    # plt.title('Original')
    # plt.show()
    # plt.imshow(X_noisy, cmap=plt.cm.gray)
    # plt.title('Noisy')
    # plt.show()

    # 1)
    N = 128
    image_signal = [np.zeros(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            image_signal[i][j] = func1(i, j)

    plt.savefig("images/ex1-func1.pdf")
    plt.imshow(image_signal, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    image_signal = [np.zeros(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            image_signal[i][j] = func2(i, j)

    plt.savefig("images/ex1-func2.pdf")
    plt.imshow(image_signal, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    image_signal = [np.zeros(N) for _ in range(N)]
    image_signal[0][5] = image_signal[0][N - 5] = 1
    rev_image = np.real(np.fft.ifft2(image_signal))
    plt.savefig("images/ex1-func3.pdf")
    plt.imshow(rev_image, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    image_signal = [np.zeros(N) for _ in range(N)]
    image_signal[5][0] = image_signal[N-5][0] = 1
    rev_image = np.real(np.fft.ifft2(image_signal))
    plt.savefig("images/ex1-func4.pdf")
    plt.imshow(rev_image, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    image_signal = [np.zeros(N) for _ in range(N)]
    image_signal[5][5] = image_signal[N-5][N-5] = 1
    rev_image = np.real(np.fft.ifft2(image_signal))
    plt.savefig("images/ex1-func5.pdf")
    plt.imshow(rev_image, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    # 2)
    freq_max = 1_000_000
    img_raton = datasets.face(gray=True)
    fft_raton = np.fft.fft2(img_raton)

    for i in range(len(fft_raton)):
        for j in range(len(fft_raton[i])):
            if np.abs(fft_raton[i][j]) >= freq_max:
                fft_raton[i][j] = 0;

    rev_img = np.real(np.fft.ifft2(fft_raton))
    plt.savefig("images/ex2.pdf")
    plt.imshow(rev_img, cmap=plt.cm.gray)
    plt.show()

    # 3)
    img_raton = datasets.face(gray=True)

    pixel_noise = 200
    noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=img_raton.shape)
    img_raton_noise = img_raton + noise

    curr_snr = np.mean(img_raton.astype(np.float64) ** 2) / np.mean(noise.astype(np.float64) ** 2)
    print(f"Before SNR: {curr_snr}")

    fft_raton2 = np.fft.fft2(img_raton_noise)
    freq_max = 900_000

    for i in range(len(fft_raton2)):
        for j in range(len(fft_raton2[i])):
            if np.abs(fft_raton2[i][j]) >= freq_max:
                fft_raton2[i][j] = 0;

    rev_img = np.real(np.fft.ifft2(fft_raton2))
    plt.savefig("images/ex3.pdf")
    plt.imshow(rev_img, cmap=plt.cm.gray)
    plt.show()

    curr_snr = np.mean(rev_img.astype(np.float64) ** 2) / np.mean(noise.astype(np.float64) ** 2)
    print(f"After SNR: {curr_snr}")


if __name__ == "__main__":
    main()
