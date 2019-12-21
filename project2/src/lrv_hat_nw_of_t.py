from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_array_of_t import cov_double_array_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
import src.precision_of_t
import numpy as np
        
    
def lrv_hat_nw_of_t(cov_double_array: np.array, sample_size: int) -> np.array:
    """
    estimate newey west.

    :param cov_matrix: covariance double array
    :return: array of newey west
    """
    t_par_count = len(cov_double_array[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    for t_par_index in range(t_par_count):
        cov_column = np.array(cov_double_array)[:, t_par_index]
        res_array[t_par_index] = lrv_hat_nw_t_free(cov_column=cov_column, sample_size=sample_size)

    return res_array


if __name__ == '__main__':
    try1 = lrv_hat_nw_of_t(cov_double_array=[[1,2,3],[5,6,7]], sample_size=2)
    print(try1)
