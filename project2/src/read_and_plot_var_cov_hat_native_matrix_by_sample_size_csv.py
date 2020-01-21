import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type: str,
                                                               count_lags: np.array,
                                                               fix_number_of_lags=None,
                                                               sample_type: str = 'ma1') -> None:
    """
    Plot var cov hat vs sample size
    Read from csv and plot len(count_lags) var cov hat lines:

    :param noise_type: type of noise 'gaussian' or 'bernoulli'
    :param count_lags: array of lags, example: [0,1,2,3,4,5]
    :param fix_number_of_lags: for take cur csv
    :param sample_type: 'ma1' or 'ma3'
    :return: plot len(count_lags) lines
    """
    # read csv
    name = ''
    if fix_number_of_lags:
        name = '_{}_lags'.format(fix_number_of_lags)
    native_matrix = read_matrix(name='var_cov_hat_native_matrix_{}{}_{}.csv'.format(noise_type, name, sample_type),
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
                title="native matrix with {} noise and {} sample vs sample sizes".format(noise_type, sample_type),
                x_label="sample size",
                y_label="var(covHat)")

    print('Made picture "native matrix with {} and noise {} sample vs sample sizes"'.format(noise_type, sample_type))


if __name__ == '__main__':
    count_lags = np.arange(0, 5)
    read_and_plot_var_cov_hat_native_matrix_by_sample_size_csv(noise_type='gaussian',   # bernoulli
                                                               count_lags=count_lags,
                                                               fix_number_of_lags=300,
                                                               sample_type='ma3')
