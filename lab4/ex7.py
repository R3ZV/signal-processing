def main():
    # P_semnal = 90db
    # SNR_db = 80dB
    # P_zgomot = ?

    # R_zgomot = 10 * log_10(P_zgomot / P0)
    # R_zgomot / 10 = log_10(P_zgomot / P0)
    # 10 ^ (R_zgomot / 10) = P_zgomot / P0
    # (10 ^ (R_zgomot / 10)) * P0 = P_zgomot
    # analog si pentru R_semnal
    # P_semanl = (10 ^ (R_semnal / 10)) * P0

    # SNR_db = 10 * log_10(P_semnal / P_zgomot)
    # 80 = 10 * log_10( (10^(R_semnal / 10)) * P0    /    (10^(R_zgomot / 10)) * P0)
    # 80 = 10 * log_10(10^(R_semnal / 10 - R_zgomot / 10)
    # 80 = 10 * (R_semnal / 10 - R_zgomot / 10)
    # 80 = R_semnal - R_zgomot => R_zgomot = 90 - 80 = 10db

main()
