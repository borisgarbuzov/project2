from coef import *
from true_cov import true_cov_scaled_noise


def compute_true_lrv_ma1(sigma, t_par):
    return sigma ** 2 * (1 + coef(t_par))


def compute_true_lrv_scaled_noise(sigma, t_par):
    return true_cov_scaled_noise(t_par, sigma, lag=0)
