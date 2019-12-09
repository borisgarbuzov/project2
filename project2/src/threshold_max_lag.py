def threshold_max_lag(sample_size: int) -> float:
	const = 1
	degree = 1/3
	bound = const * sample_size**degree
	return bound
