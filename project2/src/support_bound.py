from src.b_nw import b_nw


def support_bound(sample_size: int) -> int:
	bound = sample_size * b_nw(sample_size=sample_size)
	return int(bound) + 1
