from src.sd_cov_hat import sd_cov_hat
from src.zhou_treshold import zhou_treshold
from src.cov_column_t_free import cov_column_t_free
from src.threshold_max_lag import threshold_max_lag
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.plot_acf import plot_acf


def compute_and_save_acf(sample_size: int,
        mean: int,
        sigma: int,
        noise_type: str):
    par_list = {"sample_size": sample_size,
                "mean": mean,
                "sigma": sigma,
                "noise_type": noise_type}

    sample = diagonal_sample_tvma1(sample_size=sample_size,
                                   mean=mean,
                                   sigma=sigma,
                                   noise_type=noise_type)
    max_lag = threshold_max_lag(sample_size=sample_size)
    cov_hat = cov_column_t_free(sample=sample,
                                max_lag=max_lag)
    cloud = sd_cov_hat(sample_size=sample_size) * zhou_treshold(
        sample_size=sample_size)

    plot_acf(cov_hat=cov_hat,
             cloud=cloud,
             par_list=par_list)


if __name__ == '__main__':
    compute_and_save_acf(sample_size=1000,
                         mean=0,
                         sigma=2,
                         noise_type="gaussian")
