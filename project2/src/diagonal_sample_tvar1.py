from src.create_noise import create_noise
from src.coef import coef, coef_2, coef_3, coef_1_ar
import numpy as np


def diagonal_sample_tvar1(sample_size: int,
                          mean: int,
                          sigma: int,
                          noise_type: str,
                          noise=None):
    """
    Creates the diagonal time-varying AR1 sample, given
    sample size, mean, sigma and noise type.
    :param sample_size: size of a sample to be generated.
    :param mean: mean of the noise to generate, if not given.
    :param sigma: sigma of the noise to generate, if not given.
    :param noise_type: type of the noise to generate, if not given.
    :param noise: an array of the size sample_size+3. If it is given (not None), then sample size agreement is checked,
    and other arguments ignored.
    """
    if not noise:
        noise = create_noise(noise_size=sample_size + 3, mean=mean, sigma=sigma,
                             noise_type=noise_type)
        print('noise')
    elif len(noise) != sample_size + 3:
        raise ValueError("length of noise should be sample_size + 3")

    tvar1 = np.full(shape=sample_size, fill_value=np.nan)
    scale = sigma / (1 - 0.5**2)
    tvar1[0] = np.random.normal(loc=mean, scale=scale)

    for i in range(1, sample_size):
        tvar1[i] = noise[i] + coef_1_ar(t_par=i / sample_size) \
                   * tvar1[i - 1]

    return tvar1


if __name__ == '__main__':
    d = diagonal_sample_tvar1(sample_size=3,
                              mean=0,
                              sigma=1,
                              noise_type='gaussian')
