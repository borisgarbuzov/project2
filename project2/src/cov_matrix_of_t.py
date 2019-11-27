from src.create_t_par_array import create_t_par_array
from src.cov_hat_of_t import cov_hat_of_t
import numpy as np


def cov_matrix_of_t(sample: np.array, t_par_count: int) -> np.array:
    """
    compute covariance double array.

    :param sample: array
    :param t_par_count: count of t
    :return: double array
    """
    sample_size = len(sample)
    lag_array = np.arange(start=0, stop=sample_size, step=1)

    cov_double_array = np.full(shape=(len(lag_array), t_par_count),
                               fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count=t_par_count)

    for lag_index, lag in enumerate(lag_array):
        for t_par_index in range(t_par_count):
            cov_double_array[lag_index, t_par_index] = cov_hat_of_t(
                sample=sample,
                t_par=t_par_array[t_par_index],
                lag=lag)
        print("There are", len(lag_array) - (lag_index + 1), "lags left")

    return cov_double_array
