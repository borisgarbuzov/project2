from os.path import dirname
import numpy as np
import pandas as pd
import os
import re
from src.plot_arrays import plot_arrays


def read_and_plot_var_cov_hat_native_matrix_means_csv() -> None:
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
    native_matrix_csv = 'var_cov_hat_native_matrix_means.csv'
    native_matrix = pd.read_csv(
        os.path.join(data_folder, native_matrix_csv),
        index_col='lag')

    noise_type_array = [str(noise_type) for
                         noise_type in native_matrix.columns]

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                  lag in native_matrix.index]

    # create dict for plotting
    arrays_dict = dict()
    for type in noise_type_array:
        arrays_dict[type] = native_matrix[type]

    plot_arrays(x_array=lags_array,
                arrays_dict=arrays_dict,
                title="native matrix means",
                x_label="sample size",
                y_label="var(covHat)")


if __name__ == '__main__':
    read_and_plot_var_cov_hat_native_matrix_means_csv()
