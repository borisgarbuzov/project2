import numpy as np
from create_noise import *
from coef import *


def create_diagonal_sample_tvma1(sample_size: int, mean: float, sigma: float, type_of_noise: str) -> np.array:
    """
    Create diagonal sample tvma1.

    :param sample_size: len of sample
    :param mean: mean
    :param sigma: sigma
    :param type_of_noise: type
    :return: diagonal sample tvma1
    """
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         type_of_noise=type_of_noise)
    diagonal_sample_tvma1 = np.full(shape=sample_size, fill_value=np.nan)
    for i in range(1, sample_size + 1):
        diagonal_sample_tvma1[i - 1] = coef(t_par=i / sample_size) * noise[
            i - 1] + noise[i]
    return diagonal_sample_tvma1
