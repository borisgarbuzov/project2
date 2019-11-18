import numpy as np
from create_t_par_array import *
from compute_cov_hat import *


def compute_cov_double_array(sample, t_par_count, lag_from, lag_by, lag_to):
    lag_array = np.arange(start=lag_from, stop=lag_to, step=lag_by)
    lag_array = np.append(lag_array, lag_array[-1] + lag_by)

    cov_double_array = np.full(shape=(len(lag_array), t_par_count),
                               fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count=t_par_count)

    for lag_index, lag in enumerate(lag_array):
        for t_par in t_par_array:
            cov_double_array[lag_index, :] = compute_cov_hat(
                sample=sample,
                t_par=t_par,
                lag=lag)

    return cov_double_array
