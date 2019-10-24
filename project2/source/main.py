import numpy as np
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt


def generate_sample():
    pass


def threshold(sample: list) -> float:
    return float(np.mean(sample))


def newey_west(sample: list) -> float:
    return float(np.median(sample))


def precision(sample1: list, sample2: list) -> float:
    return float(mean_squared_error(sample1, sample2))


def compute_and_save_lrv_hat(sample_size_from: int,
                             sample_size_to: int,
                             sample_size_step: int,
                             replication_count: int,
                             method1: str,
                             method2: str) -> dict:
    sample_size_array = range(sample_size_from, sample_size_to + 1, sample_size_step)
    replication_count_array = range(1, replication_count + 1)
    samples = dict()
    if method1 == 'threshold':
        threshold_array = dict()
    if method2 == 'newey west':
        newey_west_array = dict()

    # главная переменная, хранящая все precisions
    precision_dict = dict()

    for sample_size in sample_size_array:
        samples[sample_size] = list()
        threshold_array[sample_size] = list()
        newey_west_array[sample_size] = list()
        for i in replication_count_array:
            sample = list(np.random.normal(size=sample_size))
            samples[sample_size].append(sample)
            threshold_array[sample_size].append(threshold(sample=sample))
            newey_west_array[sample_size].append(newey_west(sample=sample))

        # идеальный массив чисел для использования в функции precision
        ideal_array = list(np.ones(replication_count))
        precision_dict[sample_size] = list()
        precision_dict[sample_size].append(precision(ideal_array, threshold_array[sample_size]))
        precision_dict[sample_size].append(precision(ideal_array, newey_west_array[sample_size]))

    return precision_dict


if __name__ == '__main__':
    out = compute_and_save_lrv_hat(sample_size_from=1000,
                                   sample_size_to=10000,
                                   sample_size_step=1000,
                                   replication_count=100,
                                   method1='threshold',
                                   method2='newey west')

    for key, value in out.items():
        print(key, '->', value)
