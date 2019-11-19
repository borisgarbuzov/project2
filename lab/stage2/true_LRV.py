from coef import *
from true_cov import true_cov_scaled_noise


def true_lrv_ma1(sigma, t_par):
    # double check
    lrv =  true_cov_ma1(t_par, sigma, lag=0) + 2* true_cov_ma1(t_par, sigma, lag=1)
    return lrv


def true_lrv_scaled_noise(sigma, t_par):
    return true_cov_scaled_noise(t_par, sigma, lag=0)
