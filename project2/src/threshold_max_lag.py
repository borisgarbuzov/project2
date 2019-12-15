# Threshold max lag. 
# Initially Zhou said, n/2 or sqrt(n).
# then degree 1/3?
# No restriction is imposed from the NW side. 
# The only concern for us is performance. 
# And performance we can measure only by multiple experiments
# recording the precision. 
def threshold_max_lag(sample_size: int) -> float:
	const = 1
	degree = 1/3
	bound = const * sample_size**degree
	return bound
