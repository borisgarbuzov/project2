from src.threshold_indicator import threshold_indicator
import numpy as np


def lrv_hat_threshold_of_single_t(cov_hat_column: np.array,
                                  sample_size: int) -> int:
    max_lag = len(cov_hat_column)
    cum_sum = cov_hat_column[0] * threshold_indicator(sample_size=sample_size,
                                                     cov_hat=cov_hat_column[0],
                                                     lag=0)

    for lag in range(1, max_lag):
        term = 2 * cov_hat_column[lag] * threshold_indicator(
            sample_size=sample_size, cov_hat=cov_hat_column[lag], lag=lag)
        cum_sum += term

    return cum_sum
