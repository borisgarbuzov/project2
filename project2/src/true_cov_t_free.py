def true_cov_ma1_t_free(lag: int, sigma: int):
    if lag == 0:
        return (10 / 3) * (sigma ** 2)
    elif lag == 1:
        return (3 / 2) * (sigma ** 2)
    else:
        return 0


def true_cov_ma3_t_free(lag: int, sigma: int):
    if lag == 0:
        return (29 / 3) * (sigma ** 2)
    elif lag == 1:
        return (3 / 2) * (sigma ** 2)
    elif lag == 2:
        return (- 23 / 6) * (sigma ** 2)
    elif lag == 3:
        return (- 5 / 2) * (sigma ** 2)
    else:
        return 0
