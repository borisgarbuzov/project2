import numpy as np


def compute_precision(true_array, hat_double_array):
    """
    compute Mean, Bias, Variance, MSE

    :param true_array:
    :param hat_double_array:
    :return:list of precisions
    """
    t_par_count = len(true_array)
    mean_array = list()
    bias_array = list()
    variance_array = list()
    mse_array = list()

    for t in range(t_par_count):
        mean_array.append(np.mean(hat_double_array[t]))
        variance_array.append(np.var(hat_double_array[t]))
        bias_array.append(mean_array[t] - true_array[t])
        mse_array.append(np.mean((hat_double_array[t] - true_array[t])**2))

    return [mean_array, bias_array, variance_array, mse_array]
