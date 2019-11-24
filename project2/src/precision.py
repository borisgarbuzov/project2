import numpy as np


def mse(true_array: np.array, array: np.array) -> np.array:
    """
    Mean squared error

    :param true_array: array of true values
    :param array: array
    :return:
    """
    t_par_count = len(true_array)
    mse_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        mse_array[t] = (array[t] - true_array[t]) ** 2
    return np.mean(mse_array)


def mse2(true: np.array, sample2: np.array) -> float:
    from sklearn.metrics import mean_squared_error
    return mean_squared_error(sample1, sample2)


def mse_value_by_value_and_array(true_value, est_array):
    pass
       
       
def mse_value_by_two_arrays(true_array, est_array):
    from sklearn.metrics import mean_squared_error
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

    # Переворачиваем матрицу
    """
    Before: [
        [1, 2, 3],
        [4, 5, 6]
    ] 
    
    After: [
        [4, 1],
        [5, 2],
        [6, 3]
    ]
    """
    new = list(zip(*est_double_array[::-1]))

    for t in range(len(new)):
        new_true_array = np.full(shape=len(new[t]), fill_value=true_array[t])

        # Переворачиваем массив для нашего удобства
        """
        Before: [
            [4, 1],
            [5, 2],
            [6, 3]
        ]

        After: [
            [1, 4],
            [2, 5],
            [3, 6]
        ]
        """
        t_array = np.array(list(reversed(new[t])))

        mse_number = mse(new_true_array, t_array)
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
