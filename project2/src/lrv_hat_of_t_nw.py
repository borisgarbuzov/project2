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
        K = src.custom_kernel.triangular_kernel(v=lag / (sample_size * b_nw_value))
        for t_par_index in range(t_par_count):
            res_array[t_par_index] += cov_double_aray[lag][t_par_index] * K

    return res_array

def main():
    sample_size = 1000
    t_par_count = 11
    mean = 0
    sigma = 2
    noise_type = 'bernoulli'

    diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                            mean=mean,
                                            sigma=sigma,
                                            noise_type=noise_type)

    cov_double_array = cov_double_array_of_t(sample=diagonal_sample,
                                             t_par_count=t_par_count)

    # newey west array
    nw_array = lrv_hat_of_t_nw(cov_double_aray=cov_double_array, sample_size=sample_size)

    true_array = np.full(shape=t_par_count, fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count)
    for index, t_par in enumerate(t_par_array):
        true_array[index] = true_lrv_ma1_of_t(sigma=sigma, t_par=t_par)

    print('true_array: \t',true_array)
    print('nw_array: \t', nw_array)

    mse_precision = src.precision.mse_value_by_array_and_array(true_array=true_array, est_array=nw_array)
    print('mse_precision: \t', mse_precision)


if __name__ == '__main__':
    # main()
    
    sample_size = 100
    t_par_count = 5
    mean = 0
    sigma = 2
    noise_type = 'bernoulli'

    diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                            mean=mean,
                                            sigma=sigma,
                                            noise_type=noise_type)
    
    cov_double_array = cov_double_array_of_t(sample=diagonal_sample,
                                                t_par_count=t_par_count)
                                                
    print(cov_double_array)
    print()
    
    # newey west array
    nw_array = lrv_hat_of_t_nw(cov_double_aray=cov_double_array, sample_size=sample_size)

    true_array = np.full(shape=t_par_count, fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count)
    for index, t_par in enumerate(t_par_array):
        true_array[index] = true_lrv_ma1_of_t(sigma=sigma, t_par=t_par)

    print('true_array: \t',true_array)
    print('nw_array: \t', nw_array)

    mse_precision = src.precision.mse_value_by_array_and_array(true_array=true_array, est_array=nw_array)
    print('mse_precision: \t', mse_precision)
    
    
    """
    1000
    [[ 8.72125605 14.95354091 13.5520712  10.04275282  4.57548616]
 [ 3.14820206  6.28948451  6.39147955  5.13008715  2.298094  ]
 [-0.50431687 -0.41616051  0.1018635   0.52224224  0.26979438]]
 
    5000
[[ 9.23983727 16.20520068 13.01070742 10.33105682  4.66499658]
 [ 3.72073755  7.13808022  6.06359474  5.14894286  2.47136957]
 [-0.17431396  0.14704946  0.14600501  0.3592557   0.27742268]
 [-0.26445543 -0.11016734 -0.06247212  0.37769989  0.35056467]
 [-0.28396354 -0.57220552 -0.36170272  0.02086382  0.26266703]]
    
    10000
    [[ 9.47613395 16.37327096 12.81249972  9.89933089  4.16007515]
 [ 3.89581885  7.08109089  5.84893843  4.64293208  1.8753216 ]
 [-0.15201994 -0.20633233  0.06264835  0.01681784 -0.2919742 ]
 [-0.142519   -0.29316836  0.01828688  0.37599524 -0.05507816]
 [ 0.29277547 -0.11838436 -0.07511308  0.19210744  0.02363172]
 [ 0.79244134  0.32585423 -0.10265102 -0.14354587 -0.07021836]]
    """