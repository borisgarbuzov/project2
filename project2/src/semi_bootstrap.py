from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.paired_products import paired_products
from src.block_sums import block_sums
from src.batch_size import batch_size
import numpy as np


def semi_bootstrap(sample_size: int,
                   lag: int,
                   mean: int,
                   sigma: int,
                   noise_type: str,
                   sample_type: str="ma1"):
    batch_size_value = batch_size(sample_size=sample_size)
    if sample_type == "ma1":
        sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                       sigma=sigma, noise_type=noise_type)
    elif sample_type == "ma3":
        sample = diagonal_sample_tvma3(sample_size=sample_size, mean=mean,
                                       sigma=sigma, noise_type=noise_type)
    paired_product_array = paired_products(sample=sample, lag=lag)
    block_sum_array = block_sums(paired_product_array=paired_product_array)

    cum_sum = 0

    for index in range(len(block_sum_array) - batch_size_value):
        cum_sum += ((block_sum_array[index] - block_sum_array[
            index + batch_size_value]) / np.sqrt(2 * batch_size_value)) ** 2

    semi_bootstrap_value = cum_sum / sample_size

    return semi_bootstrap_value
