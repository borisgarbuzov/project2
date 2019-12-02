from src.batch_size import batch_size
import numpy as np


def var_cov_hat_bootstrap_statistic(block_sum_array: np.array,
                                    sample_size: int,
                                    g_array=None) -> float:
    batch_size_value = batch_size(sample_size=sample_size)

    if g_array is None:
        g_array = np.random.normal(0, 2,
                                   len(block_sum_array - batch_size_value))

    if len(g_array) != len(block_sum_array - batch_size_value):
        raise IndexError("g_array size should be as block_sum_array, not",
                         len(g_array))

    partial_sum = 0

    for index in range(len(block_sum_array) - batch_size_value):
        partial_sum += block_sum_array[index] - block_sum_array[
            index + batch_size_value] * g_array[index]

    s_value = partial_sum / np.sqrt(sample_size * 2 * batch_size_value)

    return s_value
