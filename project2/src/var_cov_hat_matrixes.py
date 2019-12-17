from timeit import default_timer as timer
from os.path import dirname
import numpy as np
import pandas as pd
import datetime
import os
from plot_two_arrays import plot_two_arrays
import re


def read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type: str, what_lag: int):
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    theoretical_csv = 'var_cov_hat_theoretical_matrix_{}.csv'.format(noise_type)
    theoretical = pd.read_csv(
        os.path.join(data_folder, theoretical_csv),
        index_col='lag')
      
    native_matrix_csv = 'var_cov_hat_native_matrix_{}.csv'.format(noise_type)
    native_matrix = pd.read_csv(
        os.path.join(data_folder, native_matrix_csv),
        index_col='lag')

    print(theoretical_csv, native_matrix_csv)

    sample_size_array = [int(re.sub("[^0-9]", "", sample_size)) for
                         sample_size in theoretical.columns]

    theoretical_lag = np.array(theoretical.loc['lag {}'.format(what_lag)])
    print('theoretical_lag = ', theoretical_lag)
    native_matrix_lag = np.array(native_matrix.loc['lag {}'.format(what_lag)])
    print('native_matrix_lag = ', native_matrix_lag)

    for index, sample_size in enumerate(sample_size_array):
        native_matrix_lag[index] *= sample_size

    plot_two_arrays(x_array=sample_size_array,
                    first_array=theoretical_lag,
                    first_label='theoretical with lag {}'.format(what_lag),
                    second_array=native_matrix_lag,
                    second_label='native matrix with lag {}'.format(what_lag),
                    title="theoretical vs native matrixes with lag={} and {} noise".format(what_lag, noise_type),
                    x_label="sample size")


if __name__ == '__main__':
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='gaussian', what_lag=0)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='gaussian', what_lag=1)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='bernoulli', what_lag=0)
    read_and_plot_var_cov_hat_theoretical_and_native_matrixes_csv(noise_type='bernoulli', what_lag=1)