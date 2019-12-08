from plot_two_arrays import plot_two_arrays
from os.path import dirname
import pandas as pd
import numpy as np
import os
import re


def read_and_plot_var_cov_hat_csv():
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    bootstrap = pd.read_csv(
        os.path.join(data_folder, 'var_cov_hat_bootstrap_matrix_gaussian.csv'),
        index_col='lag')
    native_matrix = pd.read_csv(
        os.path.join(data_folder, 'var_cov_hat_native_matrix_gaussian.csv'),
        index_col='lag')

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in bootstrap.columns]

    bootstrap_lag_0 = np.array(bootstrap.loc['lag 0'])
    # * sample_size ???
    native_matrix_lag_0 = np.array(native_matrix.loc['lag 0']) 

    plot_two_arrays(x_array=sample_size_array,
                    first_array=bootstrap_lag_0,
                    first_label="bootstrap with lag 0",
                    second_array=native_matrix_lag_0,
                    second_label="native matrix with lag 0",
                    title="bootstrap vs native matrix with gaussian noise",
                    x_label="sample size")


if __name__ == '__main__':
    read_and_plot_var_cov_hat_csv()