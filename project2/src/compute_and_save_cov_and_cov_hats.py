from src.diagonal_sample_tvma1 import *
from src.horizontal_sample_tvma1 import *
from src.diagonal_sample_scaled_noise import *
from src.horizontal_sample_scaled_noise import *
from src.create_t_par_array import *
from src.true_cov import *
from src.cov_hat import *
from src.plot_double_array import *
import numpy as np


def compute_and_save_cov_and_cov_hats(sample_size,
                                      t_par_count,
                                      gamma_count,
                                      mean,
                                      sigma,
                                      lag,
                                      type_process,
                                      type_of_noise,
                                      diag_or_horiz):
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "gamma_count": gamma_count,
                "mean": mean,
                "sigma": sigma,
                "lag": lag, "type_process": type_process,
                "type_of_noise": type_of_noise,
                "diag_or_horiz": diag_or_horiz}

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    true_gamma_array = np.full(shape=t_par_count, fill_value=np.nan)

    gamma_hat_double_array = np.full(shape=(t_par_count, gamma_count),
                                     fill_value=np.nan)

    for t_index in range(t_par_count):
        true_gamma_array[t_index] = true_cov_ma1(t_par=t_par_array[t_index],
                                                 sigma=sigma,
                                                 lag=lag)

    for index in range(gamma_count):
        if type_process == "MA1":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_tvma1(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_tvma1(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
        elif type_process == "scaled_noise":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_scaled_noise(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_scaled_noise(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
        for t_index in range(t_par_count):
            if diag_or_horiz == "horiz":
                sample = horizontal[t_index]
            gamma_hat_double_array[t_index, index] = cov_hat(
                sample=sample,
                t_par=t_par_array[t_index],
                lag=lag)

        print("There are", gamma_count - (index + 1), "replications left")

    plot_double_array(x_array=t_par_array,
                      hat_double_array=gamma_hat_double_array,
                      true_array=true_gamma_array,
                      title='Autocovariance',
                      axis='column',
                      x_label='t par',
                      par_list=par_list)


if __name__ == '__main__':
    compute_and_save_cov_and_cov_hats(sample_size=100,
                                      t_par_count=11,
                                      gamma_count=5,
                                      mean=0,
                                      sigma=2,
                                      lag=2,
                                      type_process='MA1',
                                      type_of_noise='bernoulli',
                                      diag_or_horiz='diag')