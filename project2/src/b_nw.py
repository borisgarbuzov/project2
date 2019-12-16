def b_nw(sample_size: int) -> float:
    """
    We use it and should drop it even for t_free.
    But we can change it to max_lag or support bound = n*bn
    We do not need bandwidth separately.
    Indeed, we do not use bn separately from n*bn
    So potentially, it will likely be deprecated.
    May be chosen in some data driven methods?
    Zhou suggested to look at R packages for optimal bandwidth on NW.

    :param sample_size: size of sample
    :return: float number
    """
    b_nw_const = 1
    degree = -0.25
    return b_nw_const * sample_size ** degree
