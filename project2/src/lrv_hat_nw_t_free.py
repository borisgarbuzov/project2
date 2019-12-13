import numpy as np
import src.custom_kernel
from src.b_nw import b_nw
    

def lrv_hat_nw_t_free(cov_column: np.array, sample_size: int) -> float:
    '''
    In place of deprecated 
    lrv_hat_nw_of_single_t
    sample_size used to be computed as a length of cov_column
    Since now we do not have the full set of lags, we accept it as an argument. 
    '''
    b_nw_value = b_nw(sample_size=sample_size)
    out_value = 0.0
    
    for lag in range(len(cov_column)):
        if lag == 0:
            rep = 1
        else:
            rep = 2
        K = src.custom_kernel.triangular_kernel(v=lag / (sample_size * b_nw_value)) * rep
        out_value += cov_column[lag] * K
    return out_value
