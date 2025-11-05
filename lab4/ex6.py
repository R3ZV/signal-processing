import scipy
import matplotlib.pyplot as plt
import numpy as np

def main():
    rate, data = scipy.io.wavfile.read("images/aeiou.wav")
    N = len(data)
    group_size = int(0.01 * N)
    step = group_size // 2

    divided = []
    for i in range(0, N, step):
        if (i + group_size >= N):
            continue
        group = data[i:i+group_size]
        divided.append(group);

    fft_res_mat = np.zeros( (len(divided), len(divided[0]) // 2) )
    for i in range(len(divided)):
        group = divided[i]
        fft_res = np.abs(np.fft.fft(group))
        fft_res_mat[i] = fft_res[:group_size // 2]

    plt.pcolormesh(10 * np.log10(fft_res_mat.T))
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [sec]")
    plt.colorbar(label="Intensity [dB]")
    plt.savefig("images/ex6.pdf")
    plt.show()

main()
