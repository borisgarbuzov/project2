from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.diagonal_sample_tvma3 import diagonal_sample_tvma3
from src.diagonal_sample_tvar1 import diagonal_sample_tvar1
from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
from src.plot_double_array import plot_double_array
from src.cov_column_t_free import cov_column_t_free
from src.cov_column_of_t import cov_column_of_t
from src.threshold_max_lag import threshold_max_lag
from src.support_bound import support_bound
from src.true_lrv_t_free import true_lrv_ma1_t_free, true_lrv_ma3_t_free, true_lrv_ar1_t_free
from src.true_lrv_of_single_t import true_lrv_ma1_of_single_t, true_lrv_ma3_of_single_t, true_lrv_ar1_of_single_t
from src.compute_and_save_multi_precision_of_t import compute_and_save_multi_precision_of_t
from src.plot_ridgline import plot_ridgline
import numpy as np
import pandas as pd
import numbers
import os
from os.path import dirname
import datetime
from src.calculate_time import calculate_time
from timeit import default_timer as timer


def compute_and_save_nw_threshold_single_t(sample_size_from: int,
                                           sample_size_to: int,
                                           sample_size_by: int,
                                           replication_count: int,
                                           mean: int,
                                           sigma: int,
                                           noise_type: str,
                                           sd_type: str,
                                           is_data: bool = False,
                                           t_par="free",
                                           sample_type="ma1"):
    """
    For a series of sample sizes,
    this function generates r samples for each sample size,
    Illustrated in
    412 LRV3a / computing 2 / project 2 / vs_sample_size / M: NW and T vs sample size
    Saves 6 image files.
    For each of the two estimates, it computes and depicts the base estimates,
    and then all 4 precision indicators.
    It may be either for a given t or for t-free.
    """

    # create directory for data if it doesn't exist
    now = datetime.datetime.now()
    parent_dir = dirname(dirname(__file__))
    if is_data:
        data_folder = os.path.join(parent_dir, "data")
    if not is_data:
        data_folder = os.path.join(parent_dir, "output")
        date = '_{}'.format(now.strftime("%H;%M;%S;%f"))
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    par_list = {
        "replication_count": replication_count,
        "mean": mean,
        "sigma": sigma,
        "noise_type": noise_type,
        "sd_type": sd_type,
        "t_par": t_par,
        "sample_type": sample_type
    }

    sample_size_array = np.arange(start=sample_size_from, stop=sample_size_to,
                                  step=sample_size_by)

    # compute max lags for threshold and Newey-West
    support_bound_array = [int(support_bound(sample_size=sample_size)) + 1
                           for sample_size in sample_size_array]
    threshold_max_lag_array = [threshold_max_lag(sample_size=sample_size)
                               for sample_size in sample_size_array]
    max_lag_array = max(threshold_max_lag_array, support_bound_array)

    # empty double arrays for estimates
    threshold_double_array = np.full(shape=(replication_count,
                                            len(sample_size_array)),
                                     fill_value=np.nan)
    nw_double_array = np.full(shape=(replication_count,
                                     len(sample_size_array)),
                              fill_value=np.nan)

    # compute one of two true values
    if isinstance(t_par, numbers.Number):
        if sample_type == "ma1":
            true_LRV_array = np.repeat(true_lrv_ma1_of_single_t(sigma=sigma,
                                                                t_par=t_par),
                                       len(sample_size_array))
        elif sample_type == "ma3":
            true_LRV_array = np.repeat(true_lrv_ma3_of_single_t(sigma=sigma,
                                                                t_par=t_par),
                                       len(sample_size_array))
        elif sample_type == "ar1":
            true_LRV_array = np.repeat(true_lrv_ar1_of_single_t(sigma=sigma,
                                                                t_par=t_par),
                                       len(sample_size_array))

    elif t_par == 'free':
        if sample_type == "ma1":
            true_LRV_array = np.repeat(true_lrv_ma1_t_free(sigma=sigma),
                                       len(sample_size_array))
        elif sample_type == "ma3":
            true_LRV_array = np.repeat(true_lrv_ma3_t_free(sigma=sigma),
                                       len(sample_size_array))
        elif sample_type == "ar1":
            true_LRV_array = np.repeat(true_lrv_ar1_t_free(sigma=sigma),
                                       len(sample_size_array))
    else:
        raise ValueError(
            't_par parameter should be "free" or float number not' + t_par)

    for col_index, sample_size in enumerate(sample_size_array):
        max_lag = max_lag_array[col_index]
        threshold_max_lag_value = threshold_max_lag_array[col_index]
        nw_max_lag_value = support_bound_array[col_index]
        for replication in range(replication_count):
            if sample_type == "ma1":
                sample = diagonal_sample_tvma1(sample_size=sample_size,
                                               mean=mean,
                                               sigma=sigma,
                                               noise_type=noise_type)
            elif sample_type == "ma3":
                sample = diagonal_sample_tvma3(sample_size=sample_size,
                                               mean=mean,
                                               sigma=sigma,
                                               noise_type=noise_type)
            elif sample_type == "ar1":
                sample = diagonal_sample_tvar1(sample_size=sample_size,
                                               mean=mean,
                                               sigma=sigma,
                                               noise_type=noise_type)

            if isinstance(t_par, numbers.Number):
                cov_hat_column = cov_column_of_t(sample=sample,
                                                 t_par=t_par,
                                                 max_lag=max_lag)
            elif t_par == 'free':
                cov_hat_column = cov_column_t_free(sample=sample,
                                                   max_lag=max_lag)
            threshold_double_array[replication, col_index] = \
                lrv_hat_threshold_t_free(
                    cov_hat_column=cov_hat_column[:threshold_max_lag_value],
                    sample_size=sample_size,
                    noise_type=noise_type,
                    sd_type=sd_type,
                    sample_type=sample_type)
            nw_double_array[replication, col_index] = lrv_hat_nw_t_free(
                cov_column=cov_hat_column[:nw_max_lag_value],
                sample_size=sample_size)

    col_names = ["sample size " + str(sample_size) for sample_size
                 in sample_size_array]
    threshold_double_array_df = pd.DataFrame(threshold_double_array, columns=col_names)
    nw_double_array_df = pd.DataFrame(nw_double_array, columns=col_names)

    plot_ridgline(hat_double_array=threshold_double_array_df,
                  title="Threshold ridgline",
                  x_label="value",
                  par_list=par_list)

    plot_ridgline(hat_double_array=nw_double_array_df,
                  title="Newey-West ridgline",
                  x_label="value",
                  par_list=par_list)

    plot_double_array(x_array=sample_size_array,
                      hat_double_array=threshold_double_array,
                      true_array=true_LRV_array,
                      title="Threshold LRV t = {0}".format(t_par),
                      x_label="sample size",
                      par_list=par_list,
                      axis='row',
                      true_label='True lrv',
                      y_label='LRV')

    plot_double_array(x_array=sample_size_array,
                      hat_double_array=nw_double_array,
                      true_array=true_LRV_array,
                      title="Newey-West LRV t = {0}".format(t_par),
                      x_label="sample size",
                      par_list=par_list,
                      axis='row',
                      true_label='True lrv',
                      y_label='LRV')

    arrays_dict = {"Newey-West": nw_double_array,
                   "Threshold": threshold_double_array}
    # plot
    precision_dict = compute_and_save_multi_precision_of_t(true_array=true_LRV_array,
                                                           est_dict=arrays_dict,
                                                           par_list=par_list,
                                                           x_label="sample size",
                                                           x_array=sample_size_array)
    df_bias = pd.DataFrame(precision_dict['bias'])
    print(df_bias)
    df_bias.to_csv(os.path.join(data_folder, "bias_rep{}.csv".format(replication_count)))
    df_mean = pd.DataFrame(precision_dict['mean']).to_csv(os.path.join(data_folder, "mean_rep{}.csv".format(replication_count)))
    df_mse = pd.DataFrame(precision_dict['mse']).to_csv(os.path.join(data_folder, "mse_rep{}.csv".format(replication_count)))
    df_variance = pd.DataFrame(precision_dict['variance']).to_csv(os.path.join(data_folder, "variance_rep{}.csv".format(replication_count)))

    # to CSV
    # for DataFrame
    column_names = ["ss " + str(sample_size) for sample_size in sample_size_array]
    index_names = ["rc " + str(replication_count) for replication_count in range(replication_count)]

    # convert to Pandas DataFrame
    df_nw = pd.DataFrame(nw_double_array,
                         index=index_names,
                         columns=column_names)

    df_threshold = pd.DataFrame(threshold_double_array,
                                index=index_names,
                                columns=column_names)

    df_nw.to_csv(os.path.join(data_folder, "Newey-West_single_t.csv"))
    df_threshold.to_csv(os.path.join(data_folder, "Threshold_single_t.csv"))


if __name__ == '__main__':
    
    start_time = timer()
    compute_and_save_nw_threshold_single_t(sample_size_from=1000,
                                           sample_size_to=100001,
                                           sample_size_by=1000,
                                           replication_count=100,
                                           mean=0,
                                           sigma=2,
                                           noise_type="gaussian",
                                           sd_type="native_sim",
                                           is_data=True,
                                           t_par="free",
                                           sample_type="ar1")

    duration = timer() - start_time

    calculate_time(name='compute_and_save_nw_threshold_single_t', 
                   duration=duration,
                   parameters="""sample_size_from=1000,
                               sample_size_to=100001,
                               sample_size_by=1000,
                               replication_count=100,
                               mean=0,
                               sigma=2,
                               noise_type="gaussian",
                               sd_type="native_sim",
                               is_data=True,
                               t_par="free",
                               sample_type="ar1"'""")