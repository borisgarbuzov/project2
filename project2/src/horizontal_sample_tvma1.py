from src.create_noise import create_noise
from src.coef import coef
from src.create_t_par_array import create_t_par_array
import numpy as np


def horizontal_sample_tvma1(sample_size, t_par_count, mean, sigma,
                            noise_type):
    """
    :sample_size: number of observations or number of columns in the returned matrix.
    :t_par_count: number of t values or number of rows in the returned matrix. 
    :mean: mean of the noise. 
    :return: a double array t_par_count by sample_size
    of stationary MA1 samples. Each line, corresponding to tPar value. 
        """
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         noise_type=noise_type)
    t_par_array = create_t_par_array(t_par_count=t_par_count)
    horizontal_sample_tvma1 = np.full(shape=(t_par_count,sample_size),
                                      fill_value=np.nan)
    for i in range(t_par_count):
        for j in range(sample_size):
            horizontal_sample_tvma1[i, j] = coef(t_par=t_par_array[i]) * \
                                            noise[j] + noise[j + 1]
    return horizontal_sample_tvma1
