from timeit import default_timer as timer
from os.path import dirname
import numpy as np
import pandas as pd
import datetime
import os


def compute_and_save_var_cov_hat_theoretical_matrix(sample_size_array: np.array, lags_array: np.array, noise_type='gaussian', is_data=False):
    
    var_cov_hat_theoretical_matrix = np.full(shape=(lags_array[-1] + 1, len(sample_size_array)), fill_value=np.nan)
    
    for i, sample_size in enumerate(sample_size_array):
        for lag in lags_array:
            if (lag == 0 and noise_type == 'gaussian'):
                var_cov_hat_theoretical_matrix[lag, i] = 482 / sample_size - 144 / (sample_size ** 2)
            elif lag == 1 and noise_type == 'gaussian':
                var_cov_hat_theoretical_matrix[lag, i] = 482 / sample_size - 626 / (sample_size ** 2)
    
     # convert to Pandas DataFrame
    column_names = ["sample size " + str(sample_size) for sample_size in sample_size_array]
    
    index_names = ["lag " + str(lag) for lag in range(max(lags_array) + 1)]
    df_var_cov_hat_theoretical_matrix = pd.DataFrame(var_cov_hat_theoretical_matrix, index=index_names, columns=column_names)
    df_var_cov_hat_theoretical_matrix.index.name = 'lag' 
    
    # save DataFrame to .csv
    now = datetime.datetime.now()
    # create directory for data if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    if is_data:
        data_folder = os.path.join(parent_dir, "data")
        date = '_{}'.format(noise_type)
    if not is_data:
        data_folder = os.path.join(parent_dir, "output")
        date = '_{}_{}'.format(noise_type, now.strftime("%H;%M;%S;%f"))
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    df_var_cov_hat_theoretical_matrix.to_csv(os.path.join(data_folder,
                                                     "var_cov_hat_theoretical_matrix{}.csv".format(date)))
            
    return var_cov_hat_theoretical_matrix


if __name__ == '__main__':
    sample_size_array = np.arange(1000, 20001, 1000)
    lags_array = np.arange(0, 2)
    start_time = timer()
    res = compute_and_save_var_cov_hat_theoretical_matrix(sample_size_array=sample_size_array,
                                                          lags_array=lags_array,
                                                          noise_type='gaussian',
                                                          is_data=False)
    duration = timer() - start_time
    print(np.around(res, decimals=4))
    print('=========================================')
    print('Theoretical matrix duration:\t', duration, 'secs')
    print('=========================================\n')