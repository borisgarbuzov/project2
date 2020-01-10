def true_cov_t_free(lag: int,
                    sigma: int):
    if lag == 0:
        return (10 / 3) * (sigma ** 2)
    elif lag == 1:
        return (3 / 2) * (sigma ** 2)
    else:
        return 0
