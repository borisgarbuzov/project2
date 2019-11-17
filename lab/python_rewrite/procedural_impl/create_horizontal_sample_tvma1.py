import numpy as np
from create_noise import *
from coef import *
from create_t_par_array import *


def create_horizontal_sample_tvma1(sample_size, t_par_count, mean, sigma,
                                   type_of_noise):
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         type_of_noise=type_of_noise)
    t_par_array = create_t_par_array(t_par_count=t_par_count)
    horizontal_sample_tvma1 = np.full(shape=(t_par_count,sample_size),
                                      fill_value=np.nan)
    for i in range(t_par_count):
        for j in range(sample_size):
            horizontal_sample_tvma1[i, j] = coef(t_par=t_par_array[i]) * \
                                            noise[j] + noise[j + 1]
    return horizontal_sample_tvma1
