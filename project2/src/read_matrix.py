from os.path import dirname
import os
import pandas as pd


def read_var_cov_hat_native_matrix(name: str) -> pd.DataFrame:
    """

    :param name:
    :return:
    """
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    # read csv
    native_matrix_csv = name
    native_matrix = pd.read_csv(
        os.path.join(data_folder, native_matrix_csv),
        index_col='lag')

    return native_matrix
