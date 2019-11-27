import numpy as np


def paired_products(sample: np.array, lag: int) -> np.array:
    sample_size = len(sample)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    paired_product_array = np.full(shape=sample_size - lag, fill_value=np.nan)

    for index in range(sample_size - lag):
        paired_product_array[index] = sample[index] * sample[index + lag]

    return paired_product_array
