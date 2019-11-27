import numpy as np


def block_sum_products(paired_product_array: np.array) -> np.array:
    sample_size = len(paired_product_array)

    m_batch = 2 # this is temporary here we should call a function

    block_sum_prod_array = np.full(shape=sample_size - m_batch + 1,
                                   fill_value=np.nan)

    for index in range(sample_size - m_batch + 1):
        block_sum_prod_array[index] = np.sum(paired_product_array[index:index +
                                                                  m_batch])

    return block_sum_prod_array
