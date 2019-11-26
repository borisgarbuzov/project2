"""
true value AND est array:  2.0
true array AND est array:  25.0
new_arr:  [1 4 7]
new_arr:  [2 5 8]
new_arr:  [3 6 9]
true value AND est double array:  [ 7. 10. 15.]
new_arr:  [1 4 7]
new_arr:  [2 5 8]
new_arr:  [3 6 9]
true array AND est double array:  [15. 15. 15.]
[1 4 7]

"""

import numpy as np
from sklearn.metrics import mean_squared_error


def mse_value(true, est_array: np.array) -> float:
    """
    Mean squared error

    :param true: true value OR array of true values
    :param est_array: array
    :return: float
    """
    if type(true) == float or type(true) == int:
        true_array = np.full(shape=len(est_array), fill_value=true)
    else:
        true_array = true
    return mean_squared_error(true_array, est_array)


def mse_array_by_array_and_double_array(true_array: np.array, est_double_array: np.array) -> np.array:
    """
    Find mse for every t

    :param true_array:
    :param matrix:
    :return:
    """
    length = len(est_double_array[0])

    mse_array = np.full(shape=length, fill_value=np.nan)

    for t in range(len(est_double_array)):
        
        # берём столбец из матрицы
        t_array = np.array(est_double_array)[:, t]

        mse_number = mse_value(true_array[t], t_array)
        mse_array[t] = mse_number
    return mse_array


def mse(true, est):
    # если est массив
    if len(np.array(est).shape) == 1:  # array
        if type(true) == float or type(true) == int:
            true_array = np.full(shape=len(est), fill_value=true)
        else:
            true_array = true
        return mean_squared_error(true_array, est)
    # если est двойной массив
    elif len(np.array(est).shape) == 2:  # double array
        # выходной массив
        mse_array = np.full(shape=len(est[0]), fill_value=np.nan)

        # подготовка true_array
        if type(true) == float or type(true) == int:
            big_true_array = np.full(shape=len(est[0]), fill_value=true)
        else:
            big_true_array = true

        for t in range(len(est)):
            # берём столбец из матрицы
            t_array = np.array(est)[:, t]
            # строим массив true значений
            true_array = np.full(shape=len(t_array), fill_value=big_true_array[t])

            mse_number = mean_squared_error(true_array, t_array)
            mse_array[t] = mse_number
        return mse_array


def mean(true_array: np.array, array: np.array) -> np.array:
    t_par_count = len(true_array)
    mean_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        mean_array[t] = (np.mean(array[t]))
    return mean_array


def bias(true_array: np.array, array: np.array) -> np.array:
    t_par_count = len(true_array)
    bias_array = np.full(shape=t_par_count, fill_value=np.nan)
    mean_array = mean(true_array=true_array, array=array)
    for t in range(t_par_count):
        bias_array[t] = mean_array[t] - true_array[t]
    return bias_array


def variance(true_array: np.array, array: np.array) -> np.array:
    t_par_count = len(true_array)
    variance_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        variance_array[t] = np.var(array[t])
    return variance_array


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    print('true value AND est array: ', mse(3, l1))
    print('true array AND est array: ', mse(l1, l2))

    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    l3 = [1, 2, 3]

    print('true value AND est double array: ', mse(3, m))
    print('true array AND est double array: ', mse(l3, m))