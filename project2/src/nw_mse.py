from src.estimate_nw import estimate_nw
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_matrix import cov_matrix
from src.create_t_par_array import create_t_par_array
from src.true_lrv import true_lrv_ma1
import src.precision
import numpy as np


def main(replication_count, t_par_count, sigma, sample_size, mean):
    nw_matrix = list()

    for r in range(replication_count):
        diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                                mean=mean,
                                                sigma=sigma,
                                                noise_type='bernoulli')

        cov_double_array = cov_matrix(sample=diagonal_sample,
                                      t_par_count=t_par_count)

        # newey west array
        nw_array = estimate_nw(cov_matrix=cov_double_array)
        nw_matrix.append(nw_array)

    true_array = np.full(shape=t_par_count, fill_value=np.nan)
    t_par_array = create_t_par_array(t_par_count)
    for index, t_par in enumerate(t_par_array):
        true_array[index] = true_lrv_ma1(sigma=sigma, t_par=t_par)

    print(src.precision.mse_matrix(true_array, nw_matrix))


if __name__ == '__main__':

    # main(replication_count = 10, 
    #      t_par_count = 11, 
    #      sigma = 2, 
    #      sample_size = 20, 
    #      mean = 0)

    l1 = [3, 3, 3, 3, 3]
    l2 = [1, 2, 3, 4, 5]

    print(src.precision.mse(l1, l2))
    print(src.precision.mse2(l1, l2))
    

    print(src.precision.mse2(3, l2))