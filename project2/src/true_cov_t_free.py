def true_cov_ma1_t_free(lag: int, sigma: int):
    """
    True global autocovariance for given parameters. 
    :param sigma: standard deviation of noise used to simulate the MA1 sample. 
    :param lag: lag of autocovariance to be computed. 
    :return: true autocovariance value. 
    """    
    if lag == 0:
        return (10 / 3) * (sigma ** 2)
    elif lag == 1:
        return (3 / 2) * (sigma ** 2)
    else:
        return 0


def true_cov_ma3_t_free(lag: int, sigma: int):
    """
    True global autocovariance for given parameters. 
    :param sigma: standard deviation of noise used to simulate the MA3 sample. 
    :param lag: lag of autocovariance to be computed. 
    :return: true autocovariance value. 
    """    
    if lag == 0:
        return (59 / 3) * (sigma ** 2)
    elif lag == 1:
        return (5 / 2) * (sigma ** 2)
    elif lag == 2:
        return (53 / 6) * (sigma ** 2)
    elif lag == 3:
        return (7 / 2) * (sigma ** 2)
    else:
        return 0


def true_cov_ar1_t_free(lag: int, sigma: int):
    if lag == 0:
        return 1.435085 * (sigma ** 2)
    elif lag == 1:
        return 0.76214 * (sigma ** 2)
    elif lag == 2:
        return 0.435085 * (sigma ** 2)
    elif lag == 3:
        return 0.262125 * (sigma ** 2)
    elif lag == 4:
        return 0.16425125 * (sigma ** 2)
    else:
        return 0



