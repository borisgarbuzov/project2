import numpy as np

def zhou_treshold(sample_size):
    treshold_value = 1.96 * np.sqrt(np.log(sample_size))
    return treshold_value