import numpy as np
import re
from timeit import default_timer as timer
from src.read_matrix import read_matrix


def sd_cov_hat(sample_size: int, noise_type: str, lag: int = 0, csv_name: str = 'var_cov_hat_native_matrix_means.csv') -> float:
    """

    :param sample_size:
    :param lag:
    :param csv_name:
    :return:
    """
    nativ_matrix_means = read_matrix(name=csv_name, index_col='lag')

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                  lag in nativ_matrix_means.index]

    # make array for current noise type from csv
    noise_type_array = np.full(shape=len(lags_array), fill_value=np.NaN)

    for index_lag in lags_array:
        if index_lag == 0 or index_lag == 1:
            # noise_type_array[index_lag] = nativ_matrix_means[noise_type].values[0] or:
            noise_type_array[index_lag] = nativ_matrix_means.at['lag {}'.format(index_lag), noise_type]
        else:
            mean_elem = nativ_matrix_means.at['lag {}'.format(index_lag), 'average']
            noise_type_array[index_lag] = mean_elem

    cell = noise_type_array[lag]
    sd = np.sqrt(cell) / np.sqrt(sample_size)

    return sd


if __name__ == '__main__':
    start_time = timer()

    sd_cov_hat(sample_size=1000, lag=0, noise_type='gaussian')

    duration = timer() - start_time
    print('=========================================')
    print('Duration:\t', duration, 'secs')
    print('=========================================\n')
