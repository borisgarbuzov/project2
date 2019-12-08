def batch_size(sample_size: int) -> int:
    batch_size = 1 * sample_size ** (1 / 3)
    return int(batch_size)
