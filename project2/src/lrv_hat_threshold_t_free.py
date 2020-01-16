from src.threshold_indicator import threshold_indicator
import numpy as np


def lrv_hat_threshold_t_free(cov_hat_column: np.array,
                             sample_size: int,
                             noise_type: str,
                             sd_type: str,
                             sample_type: str = "ma1") -> int:
    max_lag = len(cov_hat_column)
    indicator_array = []
    print('--------------------------------------------------')
    print('cov_hat_column=', cov_hat_column)
    print('sample_size=', sample_size)
    print('max_lag=', max_lag)
    indicator_value = threshold_indicator(sample_size=sample_size,
                                          cov_hat=cov_hat_column[0],
                                          lag=0,
                                          noise_type=noise_type,
                                          sd_type=sd_type,
                                          sample_type=sample_type)
    indicator_array.append(indicator_value)
    cum_sum = cov_hat_column[0] * indicator_value
    for lag in range(1, max_lag):
        indicator_value = threshold_indicator(sample_size=sample_size,
                                              cov_hat=cov_hat_column[lag],
                                              lag=lag,
                                              noise_type=noise_type,
                                              sd_type=sd_type,
                                              sample_type=sample_type)
        term = 2 * cov_hat_column[lag] * indicator_value
        indicator_array.append(indicator_value)
        cum_sum += term
    print('indicator_array=', indicator_array)
    print('--------------------------------------------------')
    return cum_sum
