from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_array_of_t import cov_double_array_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t
import src.custom_kernel
import src.precision
import numpy as np
    
    
def lrv_hat_of_t_nw(cov_double_aray: np.array) -> np.array:
    """
    estimate newey west.

    :param cov_matrix: covariance double array
    :return: array of newey west
    """
    t_par_count = len(cov_double_aray[0])
    res_array = np.full(shape=t_par_count, fill_value=0.0)

    for lag in range(len(cov_double_aray)):
        K = src.custom_kernel.triangular_kernel(v=lag)
        for t_par_index in range(t_par_count):
            res_array[t_par_index] += cov_double_aray[lag][t_par_index] * K

    return res_array


if __name__ == '__main__':
    t_par_count = 11
    sigma = 2

    diagonal_sample = diagonal_sample_tvma1(sample_size=20,
                                            mean=0,
                                            sigma=sigma,
                                            noise_type='bernoulli')

    cov_double_array = cov_double_array_of_t(sample=diagonal_sample,
                                             t_par_count=t_par_count)

    # newey west array
    nw_array = lrv_hat_of_t_nw(cov_double_aray=cov_double_array)

    true_array = np.full(shape=t_par_count, fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count)
    for index, t_par in enumerate(t_par_array):
        true_array[index] = true_lrv_ma1_of_t(sigma=sigma, t_par=t_par)

    print('true_array: \t', list(true_array))
    print('nw_array: \t\t', list(nw_array))

    mse_precision = src.precision.mse(true_array=true_array, array=nw_array)
    print('mse_precision: \t', list(mse_precision))

    mse2_precision = src.precision.mse2(true_array, nw_array)
    print('mse2_precision: \t', mse2_precision)