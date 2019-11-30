import numpy as np


def cov_hat_t_free(sample: np.array, lag:int) -> float:
    sample_size = len(sample)

    if lag < 0:
        raise ValueError("lag should be equal or more than 0")
    elif lag > sample_size - 1:
        raise ValueError("lag should be less than sample size - 1")

    partial_sum = 0

    for index in range(sample_size - lag):
        partial_sum += sample[index] * sample[index + lag]

    return partial_sum / sample_size


def compute_and_save_var_cov_hat_native_matrix(replication_count, sample_size_array, max_lag_array):
    var_cov_hat_native_matrix = np.full(shape=(sample_size_array[-1], max_lag_array[-1]), fill_value=np.nan)
    print(var_cov_hat_native_matrix.shape)

    i = 0
    for sample_size in sample_size_array:
        # for lag_step in max_lag_array:
        for lag in range(max_lag_array[i]):
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                sample = np.ones(lag + 1)  # generate_tvma1
                cov_array[r] = cov_hat_t_free(sample, lag)
            var_cov_hat_native_matrix[lag, sample_size_array.index(sample_size)] = np.var(cov_array)
        print()
        print(sample_size, max_lag_array[i])
        print(var_cov_hat_native_matrix)
        i += 1
    return var_cov_hat_native_matrix


if __name__ == '__main__':
    res = compute_and_save_var_cov_hat_native_matrix(replication_count=3, sample_size_array=[1, 2, 3, 4, 5],
                                                     max_lag_array=[1, 2, 3, 4, 5])
