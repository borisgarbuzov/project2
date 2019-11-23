from src.cov_matrix import cov_matrix
from src.estimate_nw_double_sum import estimate_nw_double_sum
from src.estimate_nw import estimate_nw
from src.true_lrv import true_lrv_ma1
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.create_t_par_array import create_t_par_array
from src.plot_two_arrays import plot_two_arrays
import numpy as np


def compute_and_save_v_vs_nw(sample_size, t_par_count, mean, sigma,
                             noise_type):
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                   sigma=sigma, noise_type=noise_type)

    double_sum_nw_array = np.full(shape=t_par_count, fill_value=np.nan)
    true_lrv_ma1_array = np.full(shape=t_par_count, fill_value=np.nan)

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    cov_double_array = cov_matrix(sample=sample, t_par_count=11)
    original_nw_array = estimate_nw(cov_matrix=cov_double_array)

    for index, t_par in enumerate(t_par_array):
        true_lrv_ma1_array[index] = true_lrv_ma1(sigma=sigma, t_par=t_par)
        double_sum_nw_array[index] = estimate_nw_double_sum(sample=sample,
                                                            t_par=t_par)

    plot_two_arrays(x_array=t_par_array,
                    first_array=double_sum_nw_array,
                    first_label='Double sum Newey-West',
                    second_array=original_nw_array,
                    second_label='Original Newey-West',
                    true_array=true_lrv_ma1_array,
                    title='Double sum vs original Newey-West',
                    x_label='t par',
                    par_list=par_list)


if __name__ == '__main__':
    compute_and_save_v_vs_nw(sample_size=100, t_par_count=11, mean=0,
                             sigma=2, noise_type='bernoulli')
