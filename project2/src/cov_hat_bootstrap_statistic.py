from src.batch_size import batch_size
import numpy as np


def cov_hat_bootstrap_statistic(paired_product_array: np.array,
                                block_sum_array: np.array,
                                sample_size: int) -> int:
    batch_size_value = batch_size(sample_size=sample_size)

    z_value = np.sum(paired_product_array) / sample_size

    partial_sum = 0

    for q_value in block_sum_array:
        partial_sum += (q_value - z_value) * np.random.normal(0, 2, sample_size)

    s_value = partial_sum / np.sqrt(sample_size * batch_size_value)

    return s_value
