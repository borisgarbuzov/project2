import numpy as np
from create_t_par_array import *
from true_gamma import *
from create_diagonal_sample_tvma1 import *
from create_horizontal_sample_tvma1 import *
from create_diagonal_sample_scaled_noise import *
from create_horizontal_sample_scaled_noise import *
from gamma_hat import *
from gamma_plot import *


def gamma_and_gamma_hats(sample_size, t_par_count, gamma_count, mean, sigma,
                         lag, type_process, type_of_noise, diag_or_horiz):
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "gamma_count": gamma_count,
                "mean": mean,
                "sigma": sigma,
                "lag": lag, "type_process": type_process,
                "type_of_noise": type_of_noise,
                "diag_or_horiz": diag_or_horiz}

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    b_cov = 1 * sample_size ** (-1 / 4)

    true_gamma_array = np.full(shape=t_par_count, fill_value=np.nan)

    gamma_hat_double_array = np.full(shape=(t_par_count, gamma_count),
                                     fill_value=np.nan)

    for t_index in range(t_par_count):
        true_gamma_array[t_index] = true_gamma(t_par=t_par_array[t_index],
                                               sigma=sigma,
                                               lag=lag,
                                               type_process=type_process)

    for index in range(gamma_count):
        if type_process == "MA1":
            if diag_or_horiz == "diag":
                sample = create_diagonal_sample_tvma1(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
            elif diag_or_horiz == "horiz":
                horizontal = create_horizontal_sample_tvma1(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
        elif type_process == "scaled_noise":
            if diag_or_horiz == "diag":
                sample = create_diagonal_sample_scaled_noise(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
            elif diag_or_horiz == "horiz":
                horizontal = create_horizontal_sample_scaled_noise(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    type_of_noise=type_of_noise)
        for t_index in range(t_par_count):
            if diag_or_horiz == "horiz":
                sample = horizontal[t_index]
            gamma_hat_double_array[t_index, index] = gamma_hat(
                sample=sample, t_par=t_par_array[t_index], lag=lag, b_cov=b_cov)

        print("There are", gamma_count - (index + 1), "replications left")

    gamma_plot(t_par_array=t_par_array, hat_double_array=gamma_hat_double_array,
               true_array=true_gamma_array, par_list=par_list)


if __name__ == '__main__':
    gamma_and_gamma_hats(sample_size=10000, t_par_count=11, gamma_count=5,
                         mean=0, sigma=2, lag=2, type_process='MA1',
                         type_of_noise='bernoulli', diag_or_horiz='diag')
