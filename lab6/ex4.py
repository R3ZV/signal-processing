import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 20
    for d in np.random.randint(1, 19, 10):
        x = np.random.rand(N)
        y = np.roll(x, shift=d)

        d_rev1 = np.fft.ifft(np.fft.fft(x).conj() * np.fft.fft(y))
        d_rev2 = np.fft.ifft(np.fft.fft(y) / np.fft.fft(x))

        print(f"Real d: {np.argmax(d_rev1)}")
        print(f"Method1 d: {np.argmax(d_rev1)}")
        print(f"Method2 d: {np.argmax(d_rev2)}")
        print("--------------------------------")

main()
