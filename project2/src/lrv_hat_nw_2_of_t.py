from src.lrv_hat_nw_2_of_single_t import lrv_hat_nw_2_of_single_t
import numpy as np


def lrv_hat_nw_2_of_t(sample: np.array, t_par_array: np.array) -> np.array:
    '''
    This is the same as lrv_hat_of_single_t_nw, 
    but for all t_par_array. 
    So it calls that function in a cycle. 
    '''
    lrv_hat_of_t_nw_2_array = np.full(shape=len(t_par_array), fill_value=np.nan)
    for t_index, t_par in enumerate(t_par_array):
        lrv_hat_of_t_nw_2_array[t_index] = lrv_hat_nw_2_of_single_t(sample=sample,
                                                                    t_par=t_par)
        print("lrv_hat_of_t_nw_2 t_par left", len(t_par_array) - (t_index + 1))

    return lrv_hat_of_t_nw_2_array
