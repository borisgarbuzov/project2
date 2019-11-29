import src.cov_hat_t_free
import numpy as np


def compute_and_save_var_cov_hat_native_matrix(replication_count, sample_size_array, max_lag_array):
    for sample_size in sample_size_array:
        for lag in max_lag_array:
            var_cov_hat_native_matrix = np.full(shape=(sample_size, lag), fill_value=np.nan)
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                cov_array[r] = src.cov_hat_t_free.cov_hat_t_free(sample, lag)

            var_cov_hat_native_matrix[sample_size, lag] = np.var(cov_array)
