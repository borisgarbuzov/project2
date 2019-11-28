import numpy as np


def triangular_kernel(v):
    if abs(v) <= 1:
        kernel = 1 - abs(v)
    else:
        kernel = 0
    return kernel 


def boxcar_kernel(v):
    if abs(v) <= 1:
        kernel = 1 / 2
    else:
        kernel = 0            
    return kernel 


def gaussian_kernel(v):
    kernel = np.exp(-v**2/2)/np.sqrt(2*np.pi)
    return kernel
