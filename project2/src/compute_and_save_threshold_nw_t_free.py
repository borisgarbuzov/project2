from src.cov_column_t_free import cov_column_t_free
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
from src.true_lrv_t_free import true_lrv_t_free
from src.support_bound import support_bound
from src.plot_histogram import plot_histogram
import numpy as np


def compute_and_save_threshold_nw_t_free(sample_size: int,
                                         replication_count: int,
                                         mean: int,
                                         sigma: int,
                                         noise_type: str,
                                         lrv_type: str):
    par_list = {"sample_size": sample_size,
                "replication_count": replication_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    threshold_t_free_array = np.full(shape=replication_count, fill_value=np.nan)
    nw_t_free_array = np.full(shape=replication_count, fill_value=np.nan)

    true_lrv = true_lrv_t_free(sigma=sigma)

    max_lag = int(support_bound(sample_size=sample_size)) + 1

    for replication in range(replication_count):
        sample = diagonal_sample_tvma1(sample_size=sample_size,
                                       mean=mean,
                                       sigma=sigma,
                                       noise_type=noise_type)
        cov_column = cov_column_t_free(sample=sample,
                                       is_threshold=True)
        if lrv_type == "threshold" or lrv_type == "both":
            threshold_t_free_array[replication] = lrv_hat_threshold_t_free(
                cov_hat_column=cov_column,
                sample_size=sample_size)
        if lrv_type == "nw" or lrv_type == "both":
            nw_t_free_array[replication] = lrv_hat_nw_t_free(
                cov_column=cov_column[:max_lag],
                sample_size=sample_size)
        print("compute_and_save_threshold_nw_t_free", replication_count -
              (replication + 1), "left")

    arrays_dict = {"Newey-West": nw_t_free_array,
                   "Threshold": threshold_t_free_array}

    plot_histogram(arrays_dict=arrays_dict,
                   true_value=true_lrv,
                   title="{} t free lrv".format(lrv_type),
                   par_list=par_list)


if __name__ == '__main__':
    compute_and_save_threshold_nw_t_free(sample_size=10000,
                                         replication_count=1000,
                                         mean=0,
                                         sigma=2,
                                         noise_type="gaussian",
                                         lrv_type="both")
