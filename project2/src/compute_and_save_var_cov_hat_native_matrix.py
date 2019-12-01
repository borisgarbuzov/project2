import numpy as np
from src.support_bound import support_bound
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_hat_t_free import cov_hat_t_free
from timeit import default_timer as timer


def max_lag_array(sample_size_array: np.array) -> np.array:
    return np.array([int(support_bound(sample_size)) + 1 for sample_size in list(sample_size_array)])


def compute_and_save_var_cov_hat_native_matrix(replication_count: int, sample_size_array: np.array, mean: float,
                                               sigma: float, noise_type: str) -> np.array:
    max_lag_array = [int(support_bound(sample_size)) + 1 for sample_size in sample_size_array]

    # result matrix
    var_cov_hat_native_matrix = np.full(shape=(max_lag_array[-1] + 1, len(sample_size_array)), fill_value=np.nan)
    
    for i, sample_size in enumerate(sample_size_array):
        # max lag for current sample_size
        max_lag = max_lag_array[i]  # int(support_bound(sample_size)) + 1

        for lag in range(max_lag + 1):
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean, sigma=sigma, noise_type=noise_type)
                cov_array[r] = cov_hat_t_free(sample, lag)

            var_cov_hat_native_matrix[lag, i] = np.var(cov_array)
            
    return var_cov_hat_native_matrix


def compute_and_save_var_cov_hat_native_dict(replication_count: int, sample_size_array: np.array, mean: float,
                                             sigma: float, noise_type: str) -> dict:
    var_cov_hat_native_dict = dict()

    for sample_size in sample_size_array:
        # max lag for current sample_size
    
        max_lag = int(support_bound(sample_size)) + 1
        var_cov_hat_native_dict[sample_size] = list()

        for lag in range(max_lag + 1):
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean, sigma=sigma, noise_type=noise_type)
                cov_array[r] = cov_hat_t_free(sample, lag)

            var_cov_hat_native_dict[sample_size].append(np.var(cov_array))
            
    return var_cov_hat_native_dict


if __name__ == '__main__':
    sample_size_array = np.arange(1000, 3001, 1000)
    start_time = timer()
    res1 = compute_and_save_var_cov_hat_native_matrix(replication_count=3,
                                                     sample_size_array=sample_size_array,
                                                     mean=0,
                                                     sigma=2,
                                                     noise_type='bernoulli')
    duration = timer() - start_time
    print('Matrix: ', duration, ' secs')
    print(np.around(res1, decimals=3))

    print('\n===================================\n')

    start_time = timer()
    res2 = compute_and_save_var_cov_hat_native_dict(replication_count=3,
                                                   sample_size_array=sample_size_array,
                                                   mean=0,
                                                   sigma=2,
                                                   noise_type='bernoulli')
    duration = timer() - start_time
    print('Dict: ', duration, ' secs')
    
    for key, value in res2.items():
        print(key, ' = ', np.around(value, decimals=3))
