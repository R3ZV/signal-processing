def trend_func(t):
    return 0.420 * t * t + t * 0.6 + 0.9

def sinus(t):
    return 3 * np.sin(2 * np.pi * 15 * t) + 5 * np.sin(2 * np.pi * 11 * t)

def ar_predict(signal, m, p):
    N = len(signal)
    err = 0.0
    predictions = []

    for chunk_start in range(m, N):
        win = signal[chunk_start - m : chunk_start]
        expected = signal[chunk_start]

        num_samples = m - p
        Y_train = np.zeros((num_samples, p))
        x_train = np.zeros(num_samples)

        for i in range(num_samples):
            Y_train[i] = win[i : i + p]
            x_train[i] = win[i + p]

        Gamma = np.dot(Y_train.T, Y_train)
        gamma_vec = np.dot(Y_train.T, x_train)
        phi = np.dot(np.linalg.inv(Gamma), gamma_vec)

        prev_ps = win[-p:]
        y_hat = np.dot(prev_ps, phi)
        predictions.append(y_hat)
        err += (y_hat - expected) ** 2

    return np.array(predictions), err

def main():
    N = 1000
    pixel_noise = 200

    time = np.linspace(0, 1, N)
    noise = np.random.normal(size=N)
    trend = np.vectorize(trend_func)(time)
    season = np.vectorize(sinus)(time)
    signal = noise + trend + season

    p = 3
    m = 10
    steps = 5
    prediction = ar_predict(signal, m, p)

    idx_order = []
    for _ in range(steps):
        if idx in idx_order:
            continue

        for i in idx_order:
            Y = [:, i]


if __name__ == "__main__":
    main()
