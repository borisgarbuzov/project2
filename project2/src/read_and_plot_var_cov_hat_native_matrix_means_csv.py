import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_means_csv() -> None:
    """
    Plot var cov hat means for both noise types.
    Plot two lines
    the first is gaussian
    the second is bernoulli

    :return: plot 2 lines
    """

    native_matrix = read_matrix(name='var_cov_hat_native_matrix_means.csv', index_col='lag')

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
    print('Made picture "native matrix means"')


if __name__ == '__main__':
    read_and_plot_var_cov_hat_native_matrix_means_csv()
