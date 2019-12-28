import numpy as np


def sd_cov_hat(sample_size: int, lag: int=0):
    # sd = 1 / np.sqrt(sample_size)
    sd = np.sqrt(482) / np.sqrt(sample_size)
    # later, we need to read the numerator constant to be read from CSV
    # The cell of that CSV is based on lag
    return sd
