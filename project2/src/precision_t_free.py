import numpy as np
from sklearn.metrics import mean_squared_error
from src.bias_t_free import bias_t_free

def mean_t_free(est_array: np.array):
    return np.mean(est_array)

def bias_t_free(true_value: float, est_array: np.array):
    return bias_t_free(est_array, true_value)

def variance_r_free(est_array: np.array):
    return np.var(est_array)
    
def mse_t_free(true_value: float, est_array: np.array):
    return mean_squared_error(true_array, est_array)
    