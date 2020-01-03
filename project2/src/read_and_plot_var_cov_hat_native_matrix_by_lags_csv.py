from os.path import dirname
import numpy as np
import pandas as pd
import os
import re
from src.plot_arrays import plot_arrays


def read_and_plot_var_cov_hat_native_matrix_by_lags_csv(noise_type: str, fix_number_of_lags=None) -> None:
    """
    Plot var cov hat vs lags
    Read from csv and plot len(sample_size_array) var cov hat lines:

    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param fix_number_of_lags: for take cur csv
    :return: plot len(sample_size_array) lines
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

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                         lag in native_matrix.index]

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in native_matrix.columns]

    arrays_dict = dict()
    for sample_size in sample_size_array:

        # get column
        array_for_plot = native_matrix['sample size {}'.format(sample_size)]

        # create dict for plotting
        arrays_dict['sample size {}'.format(sample_size)] = array_for_plot

    plot_arrays(x_array=lags_array,
                arrays_dict=arrays_dict,
                title="native matrix with {} noise vs lags".format(noise_type),
                x_label="lags",
                y_label="var(covHat)")


if __name__ == '__main__':
    read_and_plot_var_cov_hat_native_matrix_by_lags_csv(noise_type='gaussian', fix_number_of_lags=300)
