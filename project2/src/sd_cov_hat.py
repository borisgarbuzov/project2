import numpy as np


def sd_cov_hat(sample_size: int, lag: int=0):
    # sd = 1 / np.sqrt(sample_size)
    sd = np.sqrt(482) / np.sqrt(sample_size)
    # later, we need to read the numerator constant to be read from CSV
    # The cell of that CSV is based on lag
# gaussian[1] = 491.6375;	bernoulli[1] = 144.7827951
# 271.12191	202.8997932
# 238.4139233	238.4139233

    return sd
