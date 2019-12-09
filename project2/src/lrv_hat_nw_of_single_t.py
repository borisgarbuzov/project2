import numpy as np
import src.custom_kernel
from src.b_nw import b_nw
    

def lrv_hat_nw_of_single_t(t_column: np.array) -> float:
    sample_size = len(t_column)
    b_nw_value = b_nw(sample_size=sample_size)
    out_value = 0.0
    
    for lag in range(sample_size):
        if lag == 0:
            rep = 1
        else:
            rep = 2
        K = src.custom_kernel.triangular_kernel(v=lag / (sample_size * b_nw_value)) * rep
        out_value += t_column[lag] * K
    return out_value
