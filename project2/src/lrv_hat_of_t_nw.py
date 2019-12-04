from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_array_of_t import cov_double_array_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t
import src.custom_kernel
import src.precision
import numpy as np
from src.b_nw import b_nw
    
    
def lrv_hat_of_t_nw(cov_double_aray: np.array, sample_size: int) -> np.array:
    """
    estimate newey west.

    :param cov_matrix: covariance double array
    :return: array of newey west
    """
    t_par_count = len(cov_double_aray[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    b_nw_value = b_nw(sample_size=sample_size)

    for lag in range(len(cov_double_aray)):
        print("lrv_hat_of_t_nw: lag =", lag)
        if lag == 0:
            rep = 1
        else :
            rep = 2
        K = src.custom_kernel.triangular_kernel(v=lag / (sample_size * b_nw_value)) * rep
        for t_par_index in range(t_par_count):

            res_array[t_par_index] += cov_double_aray[lag][t_par_index] * K

    return res_array


if __name__ == '__main__':
    pass
