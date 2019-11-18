import numpy as np


def create_t_par_array(t_par_count):
    if t_par_count <= 1:
        raise ValueError(
            "t_par_count is 1 or smaller, whereas it should be 2 or greater")
    t_par_count_inner = t_par_count - 1
    t_par_array = np.arange(0, 1, 1 / t_par_count_inner)
    return np.append(t_par_array, 1)
