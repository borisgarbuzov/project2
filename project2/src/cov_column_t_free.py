from src.cov_hat_t_free import cov_hat_t_free
from src.support_bound import support_bound
import numpy as np


def cov_column_t_free(sample: np.array) -> np.array:
    sample_size = len(sample)

    max_lag = int(support_bound(sample_size=sample_size)) + 1

    cov_column = np.full(shape=max_lag, fill_value=np.nan)

    for lag in range(max_lag):
        cov_column[lag] = cov_hat_t_free(sample=sample,
                                         lag=lag)
        print("cov_column_t_free there are", max_lag - (lag + 1), "lags left")

    return cov_column
