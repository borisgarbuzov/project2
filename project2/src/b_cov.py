# We need it for kernel, so only for t-dependent values. 
# If we do cov_hat_t_free, it does not use any bandwidth. 
# So far we took the formula from project 1. 
def b_cov(sample_size):
    b_cov = 1 * sample_size ** (-1 / 4)
    return b_cov
