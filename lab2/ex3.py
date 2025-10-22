import scipy
import sounddevice
import numpy as np

def fx(t):
    return np.cos(840 * np.pi * t + np.pi / 3)

def main():
    start = 1.0
    end = 3.0
    samples = int(44100 * (end - start + 1))

    signal = np.linspace(start, end, samples)
    res = np.vectorize(fx)(signal)

    rate = int(10e5)
    scipy.io.wavfile.write("images/audio.wav", rate, res)
    rate, x = scipy.io.wavfile.read("images/audio.wav")
    sounddevice.play(x, 44100)
    sounddevice.wait()

main()
