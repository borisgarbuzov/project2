import numpy as np


def triangular_kernel_nw(lag: int, sample_size: int) -> float:
    x = lag / sample_size * bandwidth(sample_size=sample_size)
    return (1 - abs(x)) if -1 <= x <= 1 else 0.


def bandwidth(sample_size: int) -> float:
    return sample_size / sample_size


def estimate_nw(cov_matrix: np.array) -> np.array:
    sample_size = len(cov_matrix[0])

    res_array = np.full(shape=sample_size, fill_value=0)

    for lag in range(len(cov_matrix)):
        K = triangular_kernel_nw(lag=lag, sample_size=sample_size)
        for t in range(sample_size):
            res_array[t] += cov_matrix[lag][t] * K

    return res_array


if __name__ == '__main__':
    matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]
    ]

    print(estimate_nw(cov_matrix=matrix))
