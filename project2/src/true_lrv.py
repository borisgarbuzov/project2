from src.coef import coef
from src.true_cov import true_cov_scaled_noise


def true_lrv_ma1(sigma, t_par):
    lrv = sigma ** 2 * (1 + coef(t_par)) ** 2
    return lrv


def true_lrv_scaled_noise(sigma, t_par):
    return true_cov_scaled_noise(t_par, sigma, lag=0)
