from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_double_array_of_t import cov_double_array_of_t
from src.create_t_par_array import create_t_par_array
from src.true_lrv_of_t import true_lrv_ma1_of_t
from src.lrv_hat_nw_of_t import lrv_hat_nw_of_t
from src.plot_double_array import plot_double_array
from src.support_bound import support_bound
# import src.precision
import numpy as np
        
    
def compute_and_save_nw_single_n(sample_size: int, 
                                 t_par_count: int,
                                 mean: float,
                                 sigma: float,
                                 noise_type: str,
                                 replication_count: int) -> np.array:
    """
    
    :param cov_double_array: covariance double array
    :return: array of newey west
    """
    par_list = {
        "sample_size": sample_size,
        "t_par_count": t_par_count,
        "mean": mean,
        "sigma": sigma,
        "noise_type": noise_type,
        "replication_count": replication_count
    }
    
    t_par_array = create_t_par_array(t_par_count=t_par_count)
    true_lrv_ma1_array = true_lrv_ma1_of_t(sigma=sigma, t_par_array=t_par_array)
    
    nw_hat_double_array = np.full(shape=(t_par_count, replication_count),
                                         fill_value=np.nan)
    max_lag = int(support_bound(sample_size=sample_size)) + 1

    for r in range(replication_count):
        sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                   sigma=sigma, noise_type=noise_type)
        
        cov_double_array = cov_double_array_of_t(sample=sample,
                                                 t_par_count=11,
                                                 max_lag=max_lag)
        nw_hat_double_array[:, r] = lrv_hat_nw_of_t(cov_double_array=cov_double_array, sample_size=sample_size)

    plot_double_array(x_array=t_par_array,
                      hat_double_array=nw_hat_double_array,
                      true_array=true_lrv_ma1_array,
                      title=" Newey-West vs true lrv",
                      x_label="t par",
                      par_list=par_list)    
    
    return nw_hat_double_array


if __name__ == '__main__':
    compute_and_save_nw_single_n(sample_size=100,
                                 t_par_count=11,
                                 mean=0,
                                 sigma=2,
                                 noise_type="gaussian",
                                 replication_count=5)
