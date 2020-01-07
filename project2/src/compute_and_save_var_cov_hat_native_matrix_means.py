from os.path import dirname
import numpy as np
import pandas as pd
import os
import re
from timeit import default_timer as timer
from src.read_matrix import read_matrix


def compute_and_save_var_cov_hat_native_matrix_means(types_of_noises=('gaussian', 'bernoulli'),
                                                     fix_number_of_lags=None,
                                                     out_name="var_cov_hat_native_matrix_means.csv",
                                                     is_data=True):
    """
    Read from csv and save to csv var cov hat native matrix MEANS:
    Ideally, it should save to CSV file, the constants
    of averaging the values over different sample sizes for every fixed lag.
    It reads CSV file, that was an output of compute_and_save_var_cov_hat_native_matrix.
    And it saves its own CSV.

    :param types_of_noises: types of noise 'gaussian', 'bernoulli'
    :param fix_number_of_lags: lags count of csv file, for example: 'var_cov_hat_native_matrix_gaussian_300_lags.csv'
    :param out_name: name out csv file
    :return: csv
    """
    var_cov_hat_native_matrix_means = list()

    for i, noise_type in enumerate(types_of_noises):

        name = ''
        if fix_number_of_lags:
            name = '_{}_lags'.format(fix_number_of_lags)

        native_matrix = read_matrix(name='var_cov_hat_native_matrix_{}{}.csv'.format(noise_type, name), index_col='lag')

        sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for sample_size in native_matrix.columns]
        max_lag = native_matrix.shape[0]

        means_for_noise_type = np.full(shape=max_lag, fill_value=np.NaN)

        for lag in range(max_lag):
            row_for_each_lag = np.full(shape=len(sample_size_array), fill_value=np.NaN)

            for index_ss, sample_size in enumerate(sample_size_array):
                # get column
                cur_sample_size_name = 'sample size {}'.format(sample_size)
                cur_lag_name = 'lag {}'.format(lag)

                element = np.array(native_matrix[cur_sample_size_name][cur_lag_name]) * sample_size

                row_for_each_lag[index_ss] = element

            means_for_noise_type[lag] = np.mean(row_for_each_lag)

        var_cov_hat_native_matrix_means.append(list(means_for_noise_type))

    # fill 'average' column
    means_for_means = np.full(shape=max_lag, fill_value=np.NaN)
    for lag in range(max_lag):
        means_for_means[lag] = np.mean([var_cov_hat_native_matrix_means[0][lag], var_cov_hat_native_matrix_means[1][lag]])
    var_cov_hat_native_matrix_means.append(list(means_for_means))

    column_names = list(types_of_noises)
    column_names.append('average')
    index_names = ["lag " + str(lag) for lag in range(max_lag)]

    # transpose matrix
    var_cov_hat_native_matrix_means = np.array(var_cov_hat_native_matrix_means).T

    df_var_cov_hat_native_matrix_means = pd.DataFrame(var_cov_hat_native_matrix_means,
                                                      index=index_names,
                                                      columns=column_names)

    parent_dir = dirname(dirname(__file__))

    if is_data:
        data_folder = os.path.join(parent_dir, "data")
    if not is_data:
        data_folder = os.path.join(parent_dir, "output")
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    df_var_cov_hat_native_matrix_means.index.name = 'lag'
    df_var_cov_hat_native_matrix_means.to_csv(os.path.join(data_folder,
                                                           out_name))


if __name__ == '__main__':
    start_time = timer()

    compute_and_save_var_cov_hat_native_matrix_means(fix_number_of_lags=300)

    duration = timer() - start_time
    print('=========================================')
    print('Duration:\t', duration, 'secs')
    print('=========================================\n')
