import numpy as np
import matplotlib.pyplot as plt

def main():
    # a) S-a esantionat o data la fiecare ora

    # b) Incepe pe data de 25-08-2012 00:00
    # si se termina pe data de 25-09-2014 23:00
    # Deci 2 ani 1 luna si 23 de ore

    # c) Tinand cont ca a fost esantionat corect atunci
    # avem jumatate din numarul de esantioane i.e. 18287 / 2

    # d)
    data = np.genfromtxt("Train.csv", delimiter=',')[1:, 2]
    N = data.shape[0]

    freq_s = 1 / 3600
    freqs = freq_s * np.linspace(0, N // 2, N // 2) / N

    furr_res = np.abs((np.fft.fft(data) / N))[:N//2]
    plt.savefig("images/d.pdf")
    plt.yscale("log");
    plt.plot(freqs, furr_res)
    plt.show()

    # e)
    mean = furr_res[0]
    print(mean != 0)
    norm_data = data - mean
    furr_res2 = np.abs((np.fft.fft(norm_data) / N))[:N//2]
    plt.savefig("images/e.pdf")
    plt.plot(freqs, furr_res2)
    plt.yscale("log");
    plt.show()

    # f)
    x = np.argsort(furr_res)[-4:]
    print(x)
    # g)
    # h)
    # i)


if __name__ == "__main__":
    main()
