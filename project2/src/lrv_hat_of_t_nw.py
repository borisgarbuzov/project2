from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_array_of_t import cov_double_array_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t
import src.custom_kernel
import src.precision
import numpy as np
from src.b_nw import b_nw
    

def lrv_hat_of_t_nw_single_t(t_column: np.array) -> float:
    sample_size = len(t_column)
    b_nw_value = b_nw(sample_size=sample_size)
    out_value = 0.0
    
    for lag in range(sample_size):
        if lag == 0:
            rep = 1
        else:
            rep = 2
        K = src.custom_kernel.triangular_kernel(v=lag / (sample_size * b_nw_value)) * rep
        out_value += t_column[lag] * K
    return out_value
        
    
def lrv_hat_of_t_nw(cov_double_array: np.array, sample_size: int) -> np.array:
    """
    estimate newey west.

    :param cov_matrix: covariance double array
    :return: array of newey west
    """
    t_par_count = len(cov_double_array[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    for t_par_index in range(t_par_count):
        t_column = np.array(cov_double_array)[:, t_par_index]
        res_array[t_par_index] = lrv_hat_of_t_nw_single_t(t_column=t_column)

    return res_array


if __name__ == '__main__':
    try1 = lrv_hat_of_t_nw(cov_double_array=[[1,2,3],[5,6,7]], sample_size=2)
    print(try1)