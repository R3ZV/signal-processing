import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 50

    p_coeffs = np.random.randint(-10, 10, N + 1)
    q_coeffs = np.random.randint(-10, 10, N + 1)

    res_conv = np.convolve(p_coeffs, q_coeffs)
    conv_len = len(res_conv)
    print(f"Result with convolve: {res_conv}")

    P_fft = np.fft.fft(p_coeffs, n=conv_len)
    Q_fft = np.fft.fft(q_coeffs, n=conv_len)

    R_fft = P_fft * Q_fft

    r_fft_result = np.fft.ifft(R_fft)

    res_fft = np.real(r_fft_result)
    res_fft = res_fft[:len(res_conv)]
    print(f"Result with fft and ifft: {res_fft}")

    diff = np.sum(np.abs(res_conv - res_fft))
    print(f"Total difference: {diff:.10f}")

    if diff < 1e-9:
        print("Results are the same")
    else:
        print("Results don't match")

main()
