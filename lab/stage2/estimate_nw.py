from create_diagonal_sample_tvma1 import *
from compute_cov_double_array import *
from compute_b_nw import compute_b_nw
from custom_kernel import custom_kernel
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
        b_nw = compute_b_nw(t_par_count=t_par_count)
        K = custom_kernel(u=lag, bandwidth=b_nw, kernel_type='triangular')
        for t_par_index in range(t_par_count):
            res_array[t_par_index] += cov_matrix[lag][t_par_index] * K

    return res_array


if __name__ == '__main__':
    diagonal_sample = create_diagonal_sample_tvma1(sample_size=20,
                                                   mean=0,
                                                   sigma=2,
                                                   type_of_noise='bernoulli')

    cov_double_array = compute_cov_double_array(sample=diagonal_sample,
                                                t_par_count=11)

    print(estimate_nw(cov_matrix=cov_double_array))
