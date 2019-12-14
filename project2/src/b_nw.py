# We use it and should drop it even for t_free.
# But we can change it to max_lag or support bound = n*bn
# We do not need bandwidth separately. 
# Indeed, we do not use bn separately from n*bn
# So potentially, it will likely be deprecated. 
def b_nw(sample_size: int) -> float:
    """
    Compute bandwidth for newey west.

    :param t_par_count: count of t
    :return: float number
    """
    b_nw_const = 1
    degree = -0.25
    return b_nw_const * sample_size ** degree
