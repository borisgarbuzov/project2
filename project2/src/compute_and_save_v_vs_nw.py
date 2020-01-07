from src.cov_double_array_of_t import cov_double_array_of_t
from src.lrv_hat_nw_2_of_t import lrv_hat_nw_2_of_t
from src.lrv_hat_nw_of_t import lrv_hat_nw_of_t
from src.true_lrv_of_t import true_lrv_ma1_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.create_t_par_array import create_t_par_array
from src.plot_arrays import plot_arrays
from src.support_bound import support_bound


def compute_and_save_v_vs_nw(sample_size, t_par_count, mean, sigma,
                             noise_type):
    """
    This function is for visual comparison of v double summation formula with regular NW.
    It saves a single image with two curves that must coincide. And they currently do coincide.
    """
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                   sigma=sigma, noise_type=noise_type)

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    max_lag = int(support_bound(sample_size=sample_size)) + 1

    cov_double_array = cov_double_array_of_t(sample=sample,
                                             t_par_count=t_par_count,
                                             max_lag=max_lag)
    original_nw_array = lrv_hat_nw_of_t(cov_double_array=cov_double_array,
                                        sample_size=sample_size)

    true_lrv_ma1_array = true_lrv_ma1_of_t(sigma=sigma, t_par_array=t_par_array)
    double_sum_nw_array = lrv_hat_nw_2_of_t(sample=sample,
                                            t_par_array=t_par_array)

    arrays_dict = {"Double sum Newey-West": double_sum_nw_array,
                   "Original Newey-West": original_nw_array}

    plot_arrays(x_array=t_par_array,
                arrays_dict=arrays_dict,
                true_array=true_lrv_ma1_array,
                title='Double sum vs original Newey-West',
                x_label='t par',
                par_list=par_list)


if __name__ == '__main__':
    compute_and_save_v_vs_nw(sample_size=1000, t_par_count=11, mean=0,
                             sigma=2, noise_type='gaussian')
