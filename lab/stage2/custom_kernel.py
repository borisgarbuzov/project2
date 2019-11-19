from scipy.stats import norm


def custom_kernel(u: int, bandwidth=0.1, kernel_type='gaussian') -> float:
    """
    compute "triangular" or "boxcar" or "gaussian"  kernel.

    :param u: lag
    :param bandwidth: bandwidth
    :param kernel_type: type
    :return: kernel float
    """
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
