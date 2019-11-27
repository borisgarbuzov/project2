import numpy as np


def cov_hat_t_free(paired_product_array: np.array, sample_size:int) -> int:
    gamma_hat = np.sum(paired_product_array)

    return gamma_hat / sample_size
