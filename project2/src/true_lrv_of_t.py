from src.coef import coef
from src.true_cov_of_t import true_cov_scaled_noise_of_t


def true_lrv_ma1_of_t(sigma, t_par):
    lrv = sigma ** 2 * (1 + coef(t_par)) ** 2
    return lrv


def true_lrv_scaled_noise_of_t(sigma, t_par):
    return true_cov_scaled_noise_of_t(t_par, sigma, lag=0)
