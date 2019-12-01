from src.var_cell_bootstrap import var_cell_bootstrap
import numpy as np
import pandas as pd
from os.path import dirname
import os


def compute_and_save_var_bootstrap(sample_size_from: int,
                                   sample_size_to: int,
                                   sample_size_by: int,
                                   replication_count: int,
                                   mean: int,
                                   sigma: int,
                                   noise_type: str):
    # create directory for data if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    sample_size_array = np.arange(start=sample_size_from, stop=sample_size_to,
                                  step=sample_size_by)

    variance_double_array = np.full(shape=(sample_size_array[-1],
                                           len(sample_size_array)),
                                    fill_value=np.nan)

    for col_index, sample_size in enumerate(sample_size_array):
        for lag in range(sample_size):
            variance_double_array[lag, col_index] = var_cell_bootstrap(
                sample_size=sample_size,
                replication_count=replication_count,
                lag=lag,
                mean=mean,
                sigma=sigma,
                noise_type=noise_type)
            print("lags left:", sample_size - (lag + 1))
        print("sample sizes left:", len(sample_size_array) - (col_index + 1))

    column_names = ["sample size " + str(sample_size) for sample_size in
                    sample_size_array]

    df_variance_matrix = pd.DataFrame(variance_double_array,
                                      columns=column_names)

    df_variance_matrix.to_csv(os.path.join(data_folder,
                                           "variance_matrix.csv"), index=False)


if __name__ == '__main__':
    compute_and_save_var_bootstrap(sample_size_from=10,
                                   sample_size_to=110,
                                   sample_size_by=10,
                                   replication_count=10,
                                   mean=0,
                                   sigma=2,
                                   noise_type="gaussian")
