import numpy as np


def mse(true_array: np.array, hat_double_array: np.array) -> np.array:
    """
    Mean squared error

    :param true_array: array of true values
    :param hat_double_array: array
    :return:
    """
    t_par_count = len(true_array)
    mse_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        mse_array[t] = (np.mean((hat_double_array[t] - true_array[t]) ** 2))
    return mse_array


def mean(true_array: np.array, hat_double_array: np.array) -> np.array:
    t_par_count = len(true_array)
    mean_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        mean_array[t] = (np.mean(hat_double_array[t]))
    return mean_array


def bias(true_array: np.array, hat_double_array: np.array) -> np.array:
    t_par_count = len(true_array)
    bias_array = np.full(shape=t_par_count, fill_value=np.nan)
    mean_array = mean(true_array=true_array, hat_double_array=hat_double_array)
    for t in range(t_par_count):
        bias_array[t] = mean_array[t] - true_array[t]
    return bias_array


def variance(true_array: np.array, hat_double_array: np.array) -> np.array:
    t_par_count = len(true_array)
    variance_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        variance_array[t] = np.var(hat_double_array[t])
    return variance_array