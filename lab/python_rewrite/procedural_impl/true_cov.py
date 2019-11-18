from coef import *


def true_cov(t_par, sigma, lag, type_process):
    if type_process == "MA1":
        if lag == 0:
            return (sigma ** 2) * (1 + (coef(t_par=t_par) ** 2))
        elif lag == 1:
            return coef(t_par=t_par) * (sigma ** 2)
        else:
            return 0
    elif type_process == "scaled_noise":
        if lag == 0:
            return coef(t_par=t_par) ** 2 * sigma ** 2
        elif lag != 0:
            return 0
    else:
        raise ValueError("type_process should be 'MA1' or 'scaled_noise'")
