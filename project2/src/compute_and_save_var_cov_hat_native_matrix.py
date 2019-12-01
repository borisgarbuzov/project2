"""
[1000 2000 3000 4000 5000]
Matrix:  0.7354644009997173 secs
Dict:    0.5799892780000846 secs

[ 1000  2000  3000  4000  5000  6000  7000  8000  9000 10000]
Matrix:  2.3802585929997804 secs
Dict:    2.372086022000076 secs

[ 1000  2000  3000  4000  5000  6000  7000  8000  9000 10000 11000 12000
 13000 14000 15000 16000 17000 18000 19000 20000]
Matrix:  10.752176271999815 secs
Dict:    10.519024473999707 secs

[ 1000  2000  3000  4000  5000  6000  7000  8000  9000 10000 11000 12000
 13000 14000 15000 16000 17000 18000 19000 20000 21000 22000 23000 24000
 25000 26000 27000 28000 29000 30000 31000 32000 33000 34000 35000 36000
 37000 38000 39000 40000]
Matrix:  44.49741579300007 secs
Dict:    44.31950395199965 secs
"""


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
    sample_size_array = np.arange(1000, 40001, 1000)
    start_time = timer()
    res1 = compute_and_save_var_cov_hat_native_matrix(replication_count=3,
                                                     sample_size_array=sample_size_array,
                                                     mean=0,
                                                     sigma=2,
                                                     noise_type='bernoulli')
    duration = timer() - start_time
    print(sample_size_array)
    print('Matrix:\t', duration, 'secs')
    

    start_time = timer()
    res2 = compute_and_save_var_cov_hat_native_dict(replication_count=3,
                                                   sample_size_array=sample_size_array,
                                                   mean=0,
                                                   sigma=2,
                                                   noise_type='bernoulli')
    duration = timer() - start_time
    print('Dict:\t', duration, 'secs')
    
    print('=========================================\n')
    
    print(np.around(res1, decimals=3))
    print()
    for key, value in res2.items():
        print(key, ' = ', np.around(value, decimals=3))
