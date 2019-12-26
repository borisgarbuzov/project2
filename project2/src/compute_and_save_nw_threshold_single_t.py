from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
from src.plot_double_array import plot_double_array
from src.cov_column_t_free import cov_column_t_free
from src.cov_column_of_t import cov_column_of_t
from src.threshold_max_lag import threshold_max_lag
from src.support_bound import support_bound
from src.true_lrv_t_free import true_lrv_t_free
from src.true_lrv_of_single_t import true_lrv_ma1_of_single_t
import numpy as np
import numbers


def compute_and_save_nw_threshold_single_t(sample_size_from: int,
                                           sample_size_to: int,
                                           sample_size_by: int,
                                           replication_count: int,
                                           mean: int,
                                           sigma: int,
                                           noise_type: str,
                                           t_par="free"):
    par_list = {
        "sample_size_from": sample_size_from,
        "sample_size_to": sample_size_to,
        "sample_size_by": sample_size_by,
        "replication_count": replication_count,
        "mean": mean,
        "sigma": sigma,
        "noise_type": noise_type,
        "t_par": t_par
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
        true_LRV_array = np.repeat(true_lrv_ma1_of_single_t(sigma=sigma,
                                                            t_par=t_par),
                                   len(sample_size_array))
    elif t_par == 'free':
        true_LRV_array = np.repeat(true_lrv_t_free(sigma=sigma),
                                   len(sample_size_array))
    else:
        raise ValueError(
            't_par parameter should be "t_free" or float number not' + t_par)

    for col_index, sample_size in enumerate(sample_size_array):
        max_lag = max_lag_array[col_index]
        threshold_max_lag_value = threshold_max_lag_array[col_index]
        nw_max_lag_value = support_bound_array[col_index]
        for replication in range(replication_count):
            sample = diagonal_sample_tvma1(sample_size=sample_size,
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
            else:
                raise ValueError('t_par parameter should be "t_free" or float number not' + t_par)
            threshold_double_array[replication, col_index] = \
                lrv_hat_threshold_t_free(
                    cov_hat_column=cov_hat_column[:threshold_max_lag_value],
                    sample_size=sample_size)
            nw_double_array[replication, col_index] = lrv_hat_nw_t_free(
                cov_column=cov_hat_column[:nw_max_lag_value],
                sample_size=sample_size)

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


if __name__ == '__main__':
    compute_and_save_nw_threshold_single_t(sample_size_from=1000,
                                           sample_size_to=10001,
                                           sample_size_by=1000,
                                           replication_count=5,
                                           mean=0,
                                           sigma=2,
                                           noise_type="gaussian",
                                           t_par="free")
