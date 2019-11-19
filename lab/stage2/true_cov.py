from coef import *


def true_cov_ma1(t_par, sigma, lag):
    if lag == 0:
        return (sigma ** 2) * (1 + (coef(t_par=t_par) ** 2))
    elif lag == 1:
        return coef(t_par=t_par) * (sigma ** 2)
    else:
        return 0


def true_cov_scaled_noise(t_par, sigma, lag):
    if lag == 0:
        return coef(t_par=t_par) ** 2 * sigma ** 2
    elif lag != 0:
        return 0
