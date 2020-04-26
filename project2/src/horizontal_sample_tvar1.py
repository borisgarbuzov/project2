from src.coef import coef, coef_2, coef_3, coef_1_ar
from src.create_noise import create_noise
from src.create_t_par_array import create_t_par_array
import numpy as np


def horizontal_sample_tvar1(sample_size: int,
                            t_par_count: int,
                            mean: int,
                            sigma: int,
                            noise_type: str,
                            noise=None):
    """
    Generates MA(3) sample for the given noise or its parameters.
    :sample_size: number of observations or number of columns in the returned matrix.
    :t_par_count: number of t values or number of rows in the returned matrix.
    :mean: mean of the noise.
    :return: a double array t_par_count by sample_size
    of stationary MA1 samples. Each line, corresponding to tPar value.
    """
    if noise is None:
        noise = create_noise(noise_size=sample_size + 3, mean=mean, sigma=sigma,
                             noise_type=noise_type)
    elif len(noise) != sample_size + 3:
        raise ValueError("length of noise should be sample_size + 3")
    t_par_array = create_t_par_array(t_par_count=t_par_count)
    horizontal_sample_tvar1 = np.full(shape=(t_par_count, sample_size),
                                      fill_value=np.nan)

    scale = sigma / (1 - 0.5 ** 2)

    for i in range(t_par_count):
        horizontal_sample_tvar1[i, 0] = np.random.normal(loc=mean, scale=scale)
        for j in range(1, sample_size):
            t_par = t_par_array[i]
            horizontal_sample_tvar1[i, j] = noise[j] + coef_1_ar(t_par=t_par) * horizontal_sample_tvar1[i][j - 1]

    return horizontal_sample_tvar1


if __name__ == '__main__':
    horizontal = horizontal_sample_tvar1(
        sample_size=5,
        t_par_count=2,
        mean=0,
        sigma=2,
        noise_type='gaussian')
