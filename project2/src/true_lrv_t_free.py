def true_lrv_ma1_t_free(sigma: float):
    """
    Result of integration from 0 to 1 of the t-dependent LRV
    Basically, averaging.

    :param sigma: float number
    :return: true value for lrv without t
    """
    return (19 / 3) * (sigma ** 2)


def true_lrv_ma3_t_free(sigma: float):
    return (sigma ** 2) * (148 / 3)
