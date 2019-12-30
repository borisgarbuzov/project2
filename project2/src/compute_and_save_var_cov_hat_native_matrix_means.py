from os.path import dirname
import numpy as np
import pandas as pd
import os


def compute_and_save_var_cov_hat_native_matrix_means(types_of_noises=('gaussian', 'bernoulli')):
    """
    Read from csv and save to csv var cov hat native matrix MEANS:
    Ideally, it should save to CSV file, the constants
    of averaging the values over different sample sizes for every fixed lag. 
    It reads CSV file, that was an output of compute_and_save_var_cov_hat_native_matrix.
    And it saves its own CSV.
    :param types_of_noises: types of noise 'gaussian', 'bernoulli'
    :return: csv
    """
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    var_cov_hat_native_matrix_means = list()

    for i, noise_type in enumerate(types_of_noises):

        native_matrix_csv = 'var_cov_hat_native_matrix_{}.csv'.format(noise_type)
        native_matrix = pd.read_csv(os.path.join(data_folder, native_matrix_csv), index_col='lag')
        max_lag = native_matrix.shape[0]
        means_for_noise_type = np.full(shape=max_lag, fill_value=np.NaN)
        for lag in range(max_lag):
            row_for_each_lag = np.array(native_matrix.loc['lag {}'.format(lag)])
            row_for_each_lag_without_nan = [x for x in row_for_each_lag if not np.isnan(x)]
            means_for_noise_type[lag] = np.mean(row_for_each_lag_without_nan)

        # for i in range(len(means_for_noise_type)):
        #     means_for_noise_type[i] *=

        var_cov_hat_native_matrix_means.append(list(means_for_noise_type))


    # for index, sample_size in enumerate(sample_size_array):
    #     native_matrix_lag[index] *= sample_size
    #     theoretical_lag[index] *= sample_size

    column_names = ["lag " + str(lag) for lag in range(max_lag)]
    index_names = types_of_noises

    df_var_cov_hat_native_matrix_means = pd.DataFrame(var_cov_hat_native_matrix_means,
                                                      index=index_names,
                                                      columns=column_names)

    # df_var_cov_hat_native_matrix.index.name = 'lag'

    # save DataFrame to .csv
    # create directory for data if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    df_var_cov_hat_native_matrix_means.to_csv(os.path.join(data_folder, "var_cov_hat_native_matrix_means.csv"))


if __name__ == '__main__':
    compute_and_save_var_cov_hat_native_matrix_means()
