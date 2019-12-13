from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.paired_products import paired_products
from src.block_sums import block_sums
from src.var_cov_hat_bootstrap_statistic import var_cov_hat_bootstrap_statistic
import numpy as np


def var_cell_bootstrap(sample_size: int,
                       replication_count: int,
                       lag: int,
                       mean: int,
                       sigma: int,
                       noise_type: str) -> float:
    s_array = np.full(shape=replication_count, fill_value=np.nan)

    sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                   sigma=sigma, noise_type=noise_type)

    for replication in range(replication_count):
        paired_product_array = paired_products(sample=sample, lag=lag)
        block_sum_array = block_sums(paired_product_array=paired_product_array)
        s_array[replication] = var_cov_hat_bootstrap_statistic(
            block_sum_array=block_sum_array,
            sample_size=sample_size)

    return np.var(s_array)
