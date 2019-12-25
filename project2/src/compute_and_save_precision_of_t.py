from src.precision_of_t import precision_of_t, plot_precision_of_t
import numpy as np

def compute_and_save_precision_of_t(true_array: np.array,
                                    est_double_array: np.array,
                                    par_list: dict):
    precision_arrays = precision_of_t(true_array, est_double_array, par_list)
    print('Precision arrays:\n', precision_arrays)
    plot_precision_of_t(precision_arrays)

if __name__ == '__main__':
    compute_and_save_precision_of_t(true_array=np.array([1,2,3]),
                                    est_double_array=np.array([[1,2,3], [4,5,6], [7,8,9]]),
                                    par_list="")
