import numpy as np
from sklearn.metrics import mean_squared_error


def mse_value_by_value_and_array(true_value: float, est_array: np.array) -> float:
    """
    Mean squared error by value and array

    :param true: true value OR array of true values
    :param est_array: array
    :return: float
    """
    true_array = np.full(shape=len(est_array), fill_value=true_value)
    return mean_squared_error(true_array, est_array)
    
    
def mse_value_by_array_and_array(true_array: np.array, est_array: np.array) -> float:
    """
    Mean squared error by array and array

    :param true: true value OR array of true values
    :param est_array: array
    :return: float
    """
    return mean_squared_error(true_array, est_array)


def mse_array_by_array_and_double_array(true_array: np.array, est_double_array: np.array) -> np.array:
    """
    Find mse for every t

    :param true_array: array of true values for every t_par value
    :param matrix: columns correspond to t_par values, and each row is a replication
    :return: array of mse's corresponding to each t_par value
    """
    length = len(est_double_array[0])
    mse_array = np.full(shape=length, fill_value=np.nan)
    for t in range(length):
        # take a matrix column
        t_array = np.array(est_double_array)[:, t]

        mse_number = mse_value_by_value_and_array(true_array[t], t_array)
        mse_array[t] = mse_number
    return mse_array

    
def mean_array_by_double_array(double_array: np.array) -> np.array:
    """
    mean for every t
    """
    t_par_count = len(double_array[0])
    mean_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        # берём столбец из матрицы
        t_array = np.array(double_array)[:, t]
        mean_array[t] = (np.mean(t_array))
    return mean_array


def variance_array_by_double_array(double_array: np.array) -> np.array:
    """
    variance for every t
    """
    t_par_count = len(double_array[0])
    variance_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        # берём столбец из матрицы
        t_array = np.array(double_array)[:, t]
        variance_array[t] = np.var(t_array)
    return variance_array
    

def bias_array_by_array(true_array: np.array, est_array: np.array) -> np.array:
    """
    bias
    """
    t_par_count = len(true_array)
    bias_array = np.full(shape=t_par_count, fill_value=np.nan)
    
    mean_value = np.mean(est_array)
    
    for t in range(t_par_count):
        bias_array[t] = mean_value - true_array[t]
    return bias_array    

    
def bias_array_by_double_array(true_array: np.array, double_array: np.array) -> np.array:
    """
    bias for every t
    """
    t_par_count = len(true_array)
    bias_array = np.full(shape=t_par_count, fill_value=np.nan)
    mean_array = mean_array_by_double_array(double_array=double_array)
    for t in range(t_par_count):
        bias_array[t] = mean_array[t] - true_array[t]
    return bias_array


if __name__ == '__main__':
    print(mse_value_by_value_and_array(true_value=3, est_array=[1,2,3,4,5]))
    
    print(mse_value_by_array_and_array(true_array=[1,2,3,4,5], est_array=[6,7,8,9,10]))
    
    print(mse_array_by_array_and_double_array(true_array=[1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]]))
    
    print(mean_array_by_double_array(double_array=[[1,2,3],[4,5,6],[7,8,9]]))
    
    print(variance_array_by_double_array(double_array=[[1,2,3],[4,5,6],[7,8,9]]))
    
    print(bias_array_by_array(true_array=[1,2,3], est_array=[4,5,6]))
    
    print(bias_array_by_double_array(true_array=[1,2,3], double_array=[[1,2,3],[4,5,6],[7,8,9]]))