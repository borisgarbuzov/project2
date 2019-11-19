import numpy as np
from create_noise import *
from coef import *


def create_diagonal_sample_scaled_noise(sample_size, mean, sigma,
                                        type_of_noise):
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         type_of_noise=type_of_noise)
    diagonal_sample_scaled_noise = np.full(shape=sample_size, fill_value=np.nan)
    for i in range(1, sample_size + 1):
        diagonal_sample_scaled_noise[i - 1] = coef(t_par=i / sample_size) * \
                                              noise[i - 1]
    return diagonal_sample_scaled_noise