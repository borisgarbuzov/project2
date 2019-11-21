def b_nw(sample_size: int) -> float:
    """
    Compute bandwidth for newey west.

    :param t_par_count: count of t
    :return: float number
    """
    b_nw_const = 1
    degree = -0.25
    return b_nw_const * sample_size ** degree
