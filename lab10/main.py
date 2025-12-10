def trend_func(t):
    return 0.420 * t * t + t * 0.6 + 0.9

def sinus(t):
    return 3 * np.sin(2 * np.pi * 15 * t) + 5 * np.sin(2 * np.pi * 11 * t)

def main():
    N = 1000
    pixel_noise = 200

    time = np.linspace(0, 1, N)
    noise = np.random.normal(size=N)
    trend = np.vectorize(trend_func)(time)
    season = np.vectorize(sinus)(time)
    signal = noise + trend + season


if __name__ == "__main__":
    main()
