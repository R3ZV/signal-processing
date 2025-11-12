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
    plt.yscale("log");
    plt.plot(freqs, furr_res)
    plt.savefig("images/d.pdf")
    plt.show()

    # e)
    mean = furr_res[0]
    print(mean != 0)
    norm_data = data - mean
    furr_res2 = np.abs((np.fft.fft(norm_data) / N))[:N//2]
    plt.plot(freqs, furr_res2)
    plt.yscale("log");
    plt.savefig("images/e.pdf")
    plt.show()

    # f)
    x = np.argsort(furr_res)[-4:]
    print(x)
    for i in range(4):
        print("[{}] has freq: {} Hz".format(x[i], freqs[x[i]]))

    # g)
    monday_idx = 1057

    # hours in a day * days in a month
    samples = 24 * 30
    month_data =  data[monday_idx:monday_idx + samples]
    day_idx = np.linspace(0, samples, samples)
    plt.plot(day_idx, month_data)
    plt.savefig("images/g.pdf")
    plt.show()

    # h)
    # Metoda:
    # Ne putem uita la datele pe un an pe care le cunoastem (din anii trecuti) si
    # sa folosim fft pentru a determina frecvente maxime. Intrucat trendul cumpararii
    # biletelor este un obicei ce se repeta si este predictibil am putea sa observam
    # in ce luna / zi a saptamanii oamenii tind sa cumpere cele mai multe bilete,
    # probabil reprezentand o zi semnificativa din an si am putea compara cu graful nostru.

    # Limitare:
    # Daca nu s-a esantionat suficient am putea gresi in care dintre spikeuri sunt,
    # poate noi prezicem ca datele aparting perioadei de craciun cand de fapt in
    # realitate poate si vara cand vine perioada de mers la mare o sa existe un spike similar.

    # i)
    furr_res = np.fft.fft(data)
    furr_init = furr_res

    fig, axs = plt.subplots(2)
    # elementele precedente din argsort
    rmv_idx = [1, 2, 762]
    for i in rmv_idx:
        furr_res[i] = 0
        furr_res[N - i - 1] = 0
    furr_filtered = np.abs(np.fft.ifft(furr_res))
    axs[0].plot(np.arange(N), furr_init)
    axs[0].title.set_text("Initial Fourier")
    axs[1].plot(np.arange(N), furr_filtered)
    axs[1].title.set_text("Filtered Fourier")
    plt.savefig("images/i.pdf")
    plt.show()


if __name__ == "__main__":
    main()
