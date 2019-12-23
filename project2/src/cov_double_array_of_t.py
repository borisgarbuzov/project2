from src.create_t_par_array import create_t_par_array
from src.cov_hat_of_t import cov_hat_of_t
import numpy as np


def cov_double_array_of_t(sample: np.array,
                          t_par_count: int,
                          max_lag: int) -> np.array:
    """
    compute covariance double array.

    :param sample: array
    :param t_par_count: count of t
    :return: double array
    """

    cov_double_array = np.full(shape=(max_lag, t_par_count),
                               fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count=t_par_count)

    for lag in range(max_lag):
        for t_par_index in range(t_par_count):
            cov_double_array[lag, t_par_index] = cov_hat_of_t(
                sample=sample,
                t_par=t_par_array[t_par_index],
                lag=lag)
        print("cov_double_array_of_t there are", max_lag - (lag + 1),
              "lags left")

    return cov_double_array
