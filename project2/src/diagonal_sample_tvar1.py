from src.create_noise import create_noise
from src.coef import coef, coef_2, coef_3, coef_1_ar
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
import numpy as np
from src.plot_hist import plot_hist
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1


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
    elif len(noise) != sample_size + 3:
        raise ValueError("length of noise should be sample_size + 3")

    tvar1 = np.full(shape=sample_size, fill_value=np.nan)
    # our phi is around 0.5
    scale = sigma / (1 - 0.5**2)
    tvar1[0] = np.random.normal(loc=mean, scale=scale)
    # It does not matter what the first element is. 
    # The process forgets it very quickly for later indexes. 

    for i in range(1, sample_size):
        tvar1[i] = noise[i] + coef_1_ar(t_par=i / sample_size) \
                   * tvar1[i - 1]

    return tvar1


if __name__ == '__main__':
    ar1 = diagonal_sample_tvar1(sample_size=1000,
                                mean=0,
                                sigma=1,
                                noise_type='gaussian')
    plot_hist(array=ar1, name='ar1', title='ar1', show=False)

    ma1 = diagonal_sample_tvma1(sample_size=1000,
                                mean=0,
                                sigma=1,
                                noise_type='gaussian')
    plot_hist(array=ma1, name='ma1', title='ma1', show=False)

    ma3 = diagonal_sample_tvma3(sample_size=1000,
                                mean=0,
                                sigma=1,
                                noise_type='gaussian')
    plot_hist(array=ma3, name='ma3', title='ma3', show=False)
