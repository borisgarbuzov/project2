import numpy as np
from src.precision import mse_array_by_array_and_double_array, mean_array_by_double_array, variance_array_by_double_array, bias_array_by_array_and_double_array


def precision_of_t(true_array: np.array,
                    est_double_array: np.array):
    return_of_mse = mse_array_by_array_and_double_array(true_array=true_array,
                                                        est_double_array=est_double_array)
    return_of_mean = mean_array_by_double_array(est_double_array=est_double_array)
    return_of_variance = variance_array_by_double_array(est_double_array=est_double_array)
    return_of_bias = bias_array_by_array_and_double_array(true_array=true_array,
                                                          est_double_array=est_double_array)

    return np.array([return_of_mse, return_of_mean, return_of_variance, return_of_bias])
    