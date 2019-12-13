from src.b_nw import b_nw

def support_bound(sample_size: int) -> float:
	#const = 1
	#degree = 1/5
	#bound = const * sample_size**degree
	bound = sample_size * b_nw(sample_size=sample_size)
	return bound
