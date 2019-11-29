import numpy as np


def cov_hat_t_free(sample: np.array, lag:int) -> float:
    sample_size = len(sample)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    partial_sum = 0

    for index in range(sample_size - lag):
        partial_sum += sample[index] * sample[index + lag]

    return partial_sum / sample_size
