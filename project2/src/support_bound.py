def support_bound(sample_size: int) -> float:
	const = 1
	degree = 1/5
	bound = const * sample_size**degree
	return bound
