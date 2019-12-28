import numpy as np


def sd_cov_hat(sample_size: int, lag: int=0):
    # sd = 1 / np.sqrt(sample_size)
    sd = np.sqrt(482) / np.sqrt(sample_size)
    return sd
