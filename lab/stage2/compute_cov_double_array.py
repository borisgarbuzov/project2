import numpy as np
from create_t_par_array import *
from compute_cov_hat import *


def compute_cov_double_array(sample, t_par_count):
    sample_size = len(sample)
    lag_array = np.arange(start=0, stop=sample_size, step=1)

    cov_double_array = np.full(shape=(len(lag_array), t_par_count),
                               fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count=t_par_count)

    for lag_index, lag in enumerate(lag_array):
        for t_par_index in range(t_par_count):
            cov_double_array[lag_index, t_par_index] = compute_cov_hat(
                sample=sample,
                t_par=t_par_array[t_par_index],
                lag=lag)
        print("There are", len(lag_array) - (lag_index + 1), "lags left")

    return cov_double_array
