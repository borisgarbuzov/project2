from src.create_noise import create_noise
from src.coef import coef, coef_2, coef_3
import numpy as np


def diagonal_sample_tvma3(sample_size: int,
                          mean: int,
                          sigma: int,
                          noise_type: str):
    noise = create_noise(noise_size=sample_size + 3, mean=mean, sigma=sigma,
                         noise_type=noise_type)
    diagonal_sample_tvma3 = np.full(shape=sample_size, fill_value=np.nan)
    for i in range(1, sample_size + 1):
        diagonal_sample_tvma3[i - 1] = noise[i + 2] + \
        coef(t_par=i / sample_size) * noise[i + 1] + \
        coef_2(t_par=i / sample_size) * noise[i] + \
        coef_3(t_par=i / sample_size) * noise[i - 1]
    return diagonal_sample_tvma3
