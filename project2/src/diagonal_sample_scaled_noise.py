from src.create_noise import create_noise
from src.coef import coef
import numpy as np


def diagonal_sample_scaled_noise(sample_size, mean, sigma,
                                 noise_type):
    """
    Currently unused.
    Copied from the first project with translation from R to Python. 
    Forms a diagonal sample of noise, stretched by coef(t) values 
    at each index point. 
    """
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         noise_type=noise_type)
    diagonal_sample_scaled_noise = np.full(shape=sample_size, fill_value=np.nan)
    for i in range(1, sample_size + 1):
        diagonal_sample_scaled_noise[i - 1] = coef(t_par=i / sample_size) * \
                                              noise[i - 1]
    return diagonal_sample_scaled_noise
