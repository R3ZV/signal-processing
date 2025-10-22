import scipy
import numpy as np
import sounddevice

def f(t):
    return np.sin(2 * np.pi * 500 * t)

def g(t):
    return np.sin(2 * np.pi * 325 * t)

def main():
    start = 1.0
    end = 3.0
    samples = int(44100 * (end - start + 1))

    signal = np.linspace(start, end, samples)
    res1 = np.vectorize(f)(signal)
    res2 = np.vectorize(g)(signal)

    res = res1 + res2

    rate = int(10e5)
    scipy.io.wavfile.write("images/audio2.wav", rate, res)
    rate, x = scipy.io.wavfile.read("images/audio2.wav")
    sounddevice.play(x, 44100)
    sounddevice.wait()

main()
