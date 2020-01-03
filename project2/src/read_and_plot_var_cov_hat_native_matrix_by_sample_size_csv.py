from os.path import dirname
import numpy as np
import pandas as pd
import os
import re
from src.plot_arrays import plot_arrays


def read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type: str, count_lags: np.array, fix_number_of_lags=None) -> None:
    """
    Plot var cov hat vs sample size
    Read from csv and plot len(count_lags) var cov hat lines:

    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param count_lags: array of lags, example: [0,1,2,3,4,5]
    :param fix_number_of_lags: for take cur csv
    :return: plot len(count_lags) lines
    """
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    # read csv
    name = ''
    if fix_number_of_lags:
        name = '_{}_lags'.format(fix_number_of_lags)
    native_matrix_csv = 'var_cov_hat_native_matrix_{}{}.csv'.format(noise_type, name)
    native_matrix = pd.read_csv(
        os.path.join(data_folder, native_matrix_csv),
        index_col='lag')

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in native_matrix.columns]

    matrix_for_plot = np.full(shape=(len(count_lags), len(sample_size_array)), fill_value=np.NaN)

    # get 1 row from csv
    for i, lag in enumerate(count_lags):
        row = native_matrix[lag:lag+1]
        matrix_for_plot[i] = row

    # create dict for plotting
    arrays_dict = dict()
    for i, lag in enumerate(count_lags):
        arrays_dict['lag {}'.format(lag)] = matrix_for_plot[i]

    plot_arrays(x_array=sample_size_array,
                arrays_dict=arrays_dict,
                title="native matrix with {} noise vs sample sizes".format(noise_type),
                x_label="sample size",
                y_label="var(covHat)")


if __name__ == '__main__':
    count_lags = np.arange(100, 111, 2)
    read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type='gaussian', count_lags=count_lags, fix_number_of_lags=300)
