from src.batch_size import batch_size
import numpy as np


def var_cov_hat_bootstrap_statistic(paired_product_array: np.array,
                                    block_sum_array: np.array,
                                    sample_size: int,
                                    g_array=None) -> float:
    if g_array is None:
        g_array = np.random.normal(0, 2, len(block_sum_array))

    if len(g_array) != len(block_sum_array):
        raise IndexError("g_array size should be as block_sum_array, not",
                         len(g_array))

    batch_size_value = batch_size(sample_size=sample_size)
    z_value = np.sum(paired_product_array) / sample_size

    partial_sum = 0

    for index, q_value in enumerate(block_sum_array):
        partial_sum += (q_value - z_value) * g_array[index]

    s_value = partial_sum / np.sqrt(sample_size * batch_size_value)

    return s_value
