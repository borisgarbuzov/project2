from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.lrv_hat_nw_t_free import lrv_hat_nw_t_free
from src.true_lrv_t_free import true_lrv_t_free
from src.plot_histogram import plot_histogram
from src.cov_column_t_free import cov_column_t_free
from src.true_lrv_t_free import true_lrv_t_free

import numpy as np


def compute_and_save_nw_t_free(sample_size: int,
                               replication_count: int,
                               mean: int,
                               sigma: int,
                               noise_type: str):
    par_list = {"sample_size": sample_size,
                "replication_count": replication_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    nw_t_free_array = np.full(shape=replication_count, fill_value=np.nan)

    true_lrv = true_lrv_t_free(sigma=sigma)

    for replication in range(replication_count):
        sample = diagonal_sample_tvma1(sample_size=sample_size,
                                       mean=mean,
                                       sigma=sigma,
                                       noise_type=noise_type)
        cov_column = cov_column_t_free(sample=sample)
        nw_t_free_array[replication] = lrv_hat_nw_t_free(cov_column=cov_column,
                                                         sample_size=sample_size)

    plot_histogram(hat_array=nw_t_free_array,
                   true_value = true_lrv,
                   title="Newey-West t free",
                   label="Newey-West t free",
                   par_list=par_list)


if __name__== '__main__':
    compute_and_save_nw_t_free(sample_size=1000,
                               replication_count=1000,
                               mean=0,
                               sigma=2,
                               noise_type="gaussian")
