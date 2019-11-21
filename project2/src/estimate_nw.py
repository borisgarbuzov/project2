from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_matrix import cov_double_matrix
from src.custom_kernel import triangular_kernel
from src.b_nw import b_nw
import numpy as np


def estimate_nw(cov_matrix: np.array) -> np.array:
    """
    estimate Newey-West.

    :param cov_matrix: covariance double array
    :return: array of Newey-West
    """
    t_par_count = len(cov_matrix[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    for lag in range(len(cov_matrix)):
        b_nw_value = b_nw(sample_size=t_par_count)
        K = triangular_kernel(lag / (t_par_count * b_nw_value))
        for t_par_index in range(t_par_count):
            res_array[t_par_index] += cov_matrix[lag][t_par_index] * K

    return res_array


if __name__ == '__main__':
    diagonal_sample = diagonal_sample_tvma1(sample_size=20,
                                            mean=0,
                                            sigma=2,
                                            noise_type='bernoulli')

    cov_double_array = cov_double_matrix(sample=diagonal_sample,
                                         t_par_count=11)

    print(estimate_nw(cov_matrix=cov_double_array))
