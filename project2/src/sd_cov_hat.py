import numpy as np
import re
from timeit import default_timer as timer
from src.read_var_cov_hat_native_matrix import read_var_cov_hat_native_matrix


def sd_cov_hat(sample_size: int, lag: int = 0, csv_name: str = 'var_cov_hat_native_matrix_means.csv') -> float:
    """
    Duration with csv:      0.04283821600000004 secs
    Duration with fast csv: 0.010607333999999913 secs
    Duration without csv:   0.00002029100000001 secs

    :param sample_size:
    :param lag:
    :param csv_name:
    :return:
    """
    nativ_matrix_means = read_var_cov_hat_native_matrix(name=csv_name)

    # gaussian_array = nativ_matrix_means['gaussian']
    # bernoulli_array = nativ_matrix_means['bernoulli']

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                  lag in nativ_matrix_means.index]

    # make 2 arrays for gaussian and bernoulli from csv
    gaussian_array = np.full(shape=len(lags_array), fill_value=np.NaN)
    bernoulli_array = np.full(shape=len(lags_array), fill_value=np.NaN)

    for lag in lags_array:
        if lag == 0 or lag == 1:
            # gaussian_array[0] = nativ_matrix_means['gaussian'].values[0] or:
            gaussian_array[lag] = nativ_matrix_means.at['lag {}'.format(lag), 'gaussian']
            bernoulli_array[lag] = nativ_matrix_means.at['lag {}'.format(lag), 'bernoulli']
        else:
            row = np.mean(np.array(nativ_matrix_means[lag:lag+1]))
            gaussian_array[lag] = row
            bernoulli_array[lag] = row

    # sd = 1 / np.sqrt(sample_size)
    sd = np.sqrt(482) / np.sqrt(sample_size)
    # later, we need to read the numerator constant to be read from CSV
    # The cell of that CSV is based on lag

    return sd


if __name__ == '__main__':
    start_time = timer()

    sd_cov_hat(sample_size=1)

    duration = timer() - start_time
    print('=========================================')
    print('Duration:\t', duration, 'secs')
    print('=========================================\n')
