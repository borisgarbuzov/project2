from scipy.stats import norm


def custom_kernel(u, bandwidth=0.1, kernel_type='gaussian'):
    v = u / bandwidth
    if kernel_type == 'triangular':
        if abs(v) <= 1:
            kernel = 1 - abs(v)
        else:
            kernel = 0
    if kernel_type == 'boxcar':
        if abs(v) <= 1:
            kernel = 1 / 2
        else:
            kernel = 0
    if kernel_type == 'gaussian':
        kernel = norm.pdf(v)
    return kernel / bandwidth
