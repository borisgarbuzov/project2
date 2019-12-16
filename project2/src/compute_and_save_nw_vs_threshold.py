from src.create_t_par_array import create_t_par_array
from src.cov_double_array_of_t import cov_double_array_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.true_lrv_of_t import true_lrv_ma1_of_t
from src.lrv_hat_nw_of_t import lrv_hat_nw_of_t
from src.lrv_hat_threshold_of_t import lrv_hat_threshold_of_t
from src.plot_two_arrays import plot_two_arrays


def compute_and_save_nw_vs_threshold(sample_size: int,
                                     t_par_count: int,
                                     mean: int,
                                     sigma: int,
                                     noise_type: str):
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    sample = diagonal_sample_tvma1(sample_size=sample_size, mean=mean,
                                   sigma=sigma, noise_type=noise_type)

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    cov_double_array = cov_double_array_of_t(sample=sample, t_par_count=11)

    nw_lrv_array = lrv_hat_nw_of_t(cov_double_array=cov_double_array,
                                   sample_size=sample_size)
    threshold_lrv_array = lrv_hat_threshold_of_t(
        cov_double_array=cov_double_array,
        sample_size=sample_size)
    true_lrv_array = true_lrv_ma1_of_t(sigma=sigma, t_par_array=t_par_array)

    plot_two_arrays(x_array=t_par_array,
                    first_array=nw_lrv_array,
                    first_label="Newey-West LRV",
                    second_array=threshold_lrv_array,
                    second_label="Threshold LRV",
                    title="Threshold vs Newey-West",
                    x_label="t par",
                    par_list=par_list,
                    true_array=true_lrv_array,
                    y_label="LRV")


if __name__ == '__main__':
    compute_and_save_nw_vs_threshold(sample_size=10000,
                                     t_par_count=11,
                                     mean=0,
                                     sigma=2,
                                     noise_type="gaussian")
