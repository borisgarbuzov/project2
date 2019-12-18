import numpy as np

def bias_t_free(true_value, est_double_array):
    mean = np.mean(est_double_array)
    return mean - true_value
