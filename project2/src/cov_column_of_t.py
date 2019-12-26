from src.cov_hat_of_t import cov_hat_of_t
import numpy as np


def cov_column_of_t(sample: np.array, t_par: float, max_lag: int):
    cov_column = np.full(shape=max_lag, fill_value=np.nan)
    for lag in range(max_lag):
        cov_column[lag] = cov_hat_of_t(sample=sample, t_par=t_par, lag=lag)

    return cov_column
