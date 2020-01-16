from src.sd_cov_hat import sd_cov_hat
from src.zhou_treshold import zhou_treshold

def threshold_indicator(sample_size,
                        cov_hat,
                        lag,
                        noise_type,
                        sd_type,
                        sample_type="ma1"):
    ratio = abs(cov_hat) / sd_cov_hat(sample_size=sample_size,
                                      lag=lag,
                                      noise_type=noise_type,
                                      sd_type=sd_type,
                                      sample_type=sample_type)
    is_ratio_bigger = (ratio > zhou_treshold(sample_size))
    indicator_value = int(is_ratio_bigger)
    return indicator_value
