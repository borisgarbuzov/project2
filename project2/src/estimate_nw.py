from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_matrix import cov_matrix
from src.create_t_par_array import create_t_par_array
from src.true_lrv import true_lrv_ma1
import src.custom_kernel
import src.precision
import numpy as np


def estimate_nw(cov_matrix: np.array) -> np.array:
    """
    estimate newey west.

    :param cov_matrix: covariance double array
    :return: array of newey west
    """
    t_par_count = len(cov_matrix[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    for lag in range(len(cov_matrix)):
        # b_nw = compute_b_nw(t_par_count=t_par_count)
        # K = custom_kernel(u=lag, bandwidth=b_nw, kernel_type='triangular')
        K = custom_kernel.triangular_kernel(v=lag)
        for t_par_index in range(t_par_count):
            res_array[t_par_index] += cov_matrix[lag][t_par_index] * K

    return res_array


if __name__ == '__main__':
    t_par_count = 11
    sigma = 2

    diagonal_sample = diagonal_sample_tvma1(sample_size=20,
                                            mean=0,
                                            sigma=sigma,
                                            noise_type='bernoulli')

    cov_double_array = cov_matrix(sample=diagonal_sample,
                                         t_par_count=t_par_count)

    # newey west array
    nw_array = estimate_nw(cov_matrix=cov_double_array)

    true_array = np.full(shape=t_par_count, fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count)
    for index, t_par in enumerate(t_par_array):
        true_array[index] = true_lrv_ma1(sigma=sigma, t_par=t_par)

    mse_precision = precision.mse(true_array=true_array, hat_double_array=nw_array)
    print(mse_precision)