from custom_kernel import *
from compute_b_cov import *


def compute_cov_hat(sample, t_par, lag):
    sample_size = len(sample)

    b_cov = compute_b_cov(sample_size=sample_size)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    partial_sum = 0
    for term_index in range(1, (sample_size - lag) + 1):
        term = (sample[term_index - 1] * sample[(term_index - 1) + lag] *
                custom_kernel((term_index / sample_size - t_par) / b_cov))
        partial_sum += term

    cov_hat = partial_sum / (sample_size * b_cov)
    return cov_hat
