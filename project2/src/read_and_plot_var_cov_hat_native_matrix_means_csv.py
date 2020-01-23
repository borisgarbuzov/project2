import numpy as np
import re
from src.plot_arrays import plot_arrays
from src.read_matrix import read_matrix


def read_and_plot_var_cov_hat_native_matrix_means_csv(sample_type: str = "ma1") -> None:
    """
    Plot var cov hat means for both noise types.
    Plot two lines
    the first is gaussian
    the second is bernoulli
    plot 2 lines
    :param sample_type: 'ma1' or 'ma3'
    """

    native_matrix = read_matrix(name='var_cov_hat_native_matrix_means_{}.csv'.format(sample_type), index_col='lag')

    noise_type_array = [str(noise_type) for noise_type in native_matrix.columns][:2]

    lags_array = [int(re.sub("[^0-9]", "", lag)) for
                  lag in native_matrix.index]

    # create dict for plotting
    arrays_dict = dict()
    for type in noise_type_array:
        arrays_dict[type] = native_matrix[type]

    plot_arrays(x_array=lags_array,
                arrays_dict=arrays_dict,
                title="native matrix means with {} sample".format(sample_type),
                x_label="lags",
                y_label="var(covHat)")
    print('Made picture "native matrix means with {} sample"'.format(sample_type))


if __name__ == '__main__':
    read_and_plot_var_cov_hat_native_matrix_means_csv(sample_type='ma3')
