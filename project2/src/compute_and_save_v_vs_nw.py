from src.cov_double_array_of_t import cov_double_array_of_t
from src.lrv_hat_of_t_nw_2 import lrv_hat_of_t_nw_2
from src.lrv_hat_of_t_nw import lrv_hat_of_t_nw
from src.true_lrv_of_t import true_lrv_ma1_of_t
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

    cov_double_array = cov_double_array_of_t(sample=sample, t_par_count=11)
    original_nw_array = lrv_hat_of_t_nw(cov_double_aray=cov_double_array,
                                        sample_size=sample_size)

    for index, t_par in enumerate(t_par_array):
        true_lrv_ma1_array[index] = true_lrv_ma1_of_t(sigma=sigma, t_par=t_par)
        double_sum_nw_array[index] = lrv_hat_of_t_nw_2(sample=sample,
                                                       t_par=t_par)
        print("t_par left:", len(t_par_array) - (index + 1))

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
    compute_and_save_v_vs_nw(sample_size=10000, t_par_count=11, mean=0,
                             sigma=2, noise_type='gaussian')
