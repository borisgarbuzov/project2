import numpy as np
from sklearn.metrics import mean_squared_error


def mse_value_by_value_and_array(true_value: float, est_array: np.array) -> float:
    """
    Mean squared error by value and array

    :param true_value: true value
    :param est_array: array
    :return: mse value
    """
    true_array = np.full(shape=len(est_array), fill_value=true_value)
    return mean_squared_error(true_array, est_array)
    
    
def mse_value_by_array_and_array(true_array: np.array, est_array: np.array) -> float:
    """
    Mean squared error by array and array

    :param true_array: true value
    :param est_array: array of est values
    :return: mse value
    """
    return mean_squared_error(true_array, est_array)


def mse_array_by_array_and_double_array(true_array: np.array, est_double_array: np.array) -> np.array:
    """
    Find mean squared error (MSE) for every t

    :param true_array: array of true values for every t_par value
    :param est_double_array: columns correspond to t_par values, and each row is a replication
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

    
def mean_array_by_double_array(est_double_array: np.array) -> np.array:
    """
    mean for every t

    :param est_double_array: columns correspond to t_par values, and each row is a replication
    :return: array of mean's corresponding to each t_par value
    """
    t_par_count = len(est_double_array[0])
    mean_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        # take a matrix column
        t_array = np.array(est_double_array)[:, t]
        mean_array[t] = (np.mean(t_array))
    return mean_array


def variance_array_by_double_array(est_double_array: np.array) -> np.array:
    """
    variance for every t

    :param est_double_array: columns correspond to t_par values, and each row is a replication
    :return: array of variance's corresponding to each t_par value
    """
    t_par_count = len(est_double_array[0])
    variance_array = np.full(shape=t_par_count, fill_value=np.nan)
    for t in range(t_par_count):
        # take a matrix column
        t_array = np.array(est_double_array)[:, t]
        variance_array[t] = np.var(t_array)
    return variance_array

    
def bias_array_by_array_and_double_array(true_array: np.array, est_double_array: np.array) -> np.array:
    """
    bias for every t

    :param true_array: array of true values for every t_par value
    :param est_double_array: columns correspond to t_par values, and each row is a replication
    :return: array of bias's corresponding to each t_par value
    """
    t_par_count = len(true_array)
    bias_array = np.full(shape=t_par_count, fill_value=np.nan)
    mean_array = mean_array_by_double_array(est_double_array=est_double_array)
    for t in range(t_par_count):
        #bias_array[t] = bias_t_free(true_value=true_array[t], est_array=est_double_array[2]) 
        # The above is an attempt to use t_free for of_t, but it works wrong
        # The dimensions are wrong. If it is commented, deterministic tests are OK. 
        bias_array[t] = mean_array[t] - true_array[t]
    return bias_array
    
def precision_of_t(true_array: np.array,
                    est_double_array: np.array,
                    par_list: dict):
    """
    Calls 4 single precision functions. 
    Returns 4 one-dimensional arrays, wrapped up in a list
    Accepts 2 arguments: one-dimensional array of true values 
    and 2-dimensional array of estimates.
    """                        
    return_of_mse = mse_array_by_array_and_double_array(true_array=true_array,
                                                        est_double_array=est_double_array)
    return_of_mean = mean_array_by_double_array(est_double_array=est_double_array)
    return_of_variance = variance_array_by_double_array(est_double_array=est_double_array)
    return_of_bias = bias_array_by_array_and_double_array(true_array=true_array,
                                                          est_double_array=est_double_array)

    return {"mse": return_of_mse,
            "mean": return_of_mean,
            "variance": return_of_variance,
            "bias": return_of_bias
    }


if __name__ == '__main__':
    pass