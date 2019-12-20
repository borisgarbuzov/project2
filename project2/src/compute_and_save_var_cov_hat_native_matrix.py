from src.support_bound import support_bound
# from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.horizontal_sample_tvma1 import horizontal_sample_tvma1
from src.cov_hat_t_free import cov_hat_t_free
from timeit import default_timer as timer
from os.path import dirname
import numpy as np
import pandas as pd
import datetime
import os


def compute_and_save_var_cov_hat_native_matrix(replication_count: int, sample_size_array: np.array, mean: float,
                                               sigma: float, noise_type: str, is_data: bool) -> np.array:
    max_lag_array = [int(support_bound(sample_size)) for sample_size in
                     sample_size_array]

    # result matrix
    var_cov_hat_native_matrix = np.full(shape=(max_lag_array[-1] + 1,
                                               len(sample_size_array)),
                                        fill_value=np.nan)
    
    for i, sample_size in enumerate(sample_size_array):
        # max lag for current sample_size
        max_lag = max_lag_array[i]
        
        print('sample size:', sample_size)
        for lag in range(3): #max_lag + 1):
            cov_array = np.full(shape=replication_count, fill_value=np.nan)

            for r in range(replication_count):
                sample = horizontal_sample_tvma1(sample_size=sample_size,
                                                 t_par_count=11, 
                                                 mean=mean,
                                                 sigma=sigma,
                                                 noise_type=noise_type)[5, :]
                cov_array[r] = cov_hat_t_free(sample, lag)

            var_cov_hat_native_matrix[lag, i] = np.var(cov_array)
            print('lags left:', max_lag - lag)
            
    # convert to Pandas DataFrame
    column_names = ["sample size " + str(sample_size) for sample_size in sample_size_array]
    
    index_names = ["lag " + str(lag) for lag in range(max(max_lag_array) + 1)]
    df_var_cov_hat_native_matrix = pd.DataFrame(var_cov_hat_native_matrix,
                                                index=index_names,
                                                columns=column_names)
    df_var_cov_hat_native_matrix.index.name = 'lag' 
    
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
    df_var_cov_hat_native_matrix.to_csv(os.path.join(data_folder,
                                                     "var_cov_hat_native_matrix{}.csv".format(date)))
            
    return var_cov_hat_native_matrix
    
    
if __name__ == '__main__':
    sample_size_array = np.arange(1000, 20001, 1000)
    start_time = timer()
    res = compute_and_save_var_cov_hat_native_matrix(replication_count=1000,
                                                     sample_size_array=sample_size_array,
                                                     mean=0,
                                                     sigma=2,
                                                     noise_type='gaussian',
                                                     is_data=True)
    duration = timer() - start_time
    print(np.around(res, decimals=4))
    print('=========================================')
    print('Matrix duration:\t', duration, 'secs')
    print('=========================================\n')
    