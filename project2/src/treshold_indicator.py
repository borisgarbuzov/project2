import numpy as np
from src.sd_cov_hat import sd_cov_hat
from src.zhou_treshold import zhou_treshold

def treshold_indicator(sample_size, cov_hat, lag):
    indicator_value = 0
    ratio = abs(cov_hat) / sd_cov_hat(sample_size)
    is_ratio_smaller = (ratio < zhou_treshold(sample_size))
    indicator_value = int(is_ratio_smaller)
    return indicator_value