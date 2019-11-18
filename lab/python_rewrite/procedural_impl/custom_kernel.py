from scipy.stats import norm


def custom_kernel(u, bandwidth=0.1, kernel_type='gaussian'):
    v = u / bandwidth
    if kernel_type == 'gaussian':
        kernel = norm.pdf(v)
    return kernel / bandwidth
