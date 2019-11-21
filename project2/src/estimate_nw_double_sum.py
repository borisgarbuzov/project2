from src.custom_kernel import gaussian_kernel, triangular_kernel
from src.b_cov import b_cov
from src.b_nw import b_nw
import numpy as np


def estimate_nw_double_sum(sample, t_par):
    sample_size = len(sample)
    b_cov_value = b_cov(sample_size=sample_size)
    b_nw_value = b_nw(sample_size=sample_size)

    nw_hat = 0
    for i, x_i in enumerate(sample, start=1):
        for j, x_j in enumerate(sample, start=1):
            kernel_cov = gaussian_kernel(v=((np.minimum(i, j) / sample_size) -
                                            t_par) / b_cov_value) * (1 / (
                    sample_size * b_cov_value))
            kernel_nw = triangular_kernel(v=np.abs(i - j) / (sample_size *
                                                             b_nw_value))
            nw_hat += kernel_cov * kernel_nw * x_i * x_j

    return nw_hat
