"""
User gives for example,
model=MA1
sample_size_min = 100
sample_size_max = 100
sample_size_by = 100
coefficient of MA1 = (n^2)
sigma=2
r=3
methods = {NW, T}

"""

import numpy as np
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt


def threshold(sample: np.array) -> float:
    return float(np.mean(sample))


def newey_west(sample: np.array) -> float:
    return float(np.median(sample))


def generate_MA1(sample_size: int, coef=1):
    noise = np.random.normal(size=sample_size)
    ma1 = np.zeros(sample_size)

    for i in range(sample_size):
        ma1[i - 1] = noise[i] + coef * noise[i - 1]

    return ma1


def compute_MSE(sample1: np.array, sample2: np.array) -> float:
    return float(mean_squared_error(sample1, sample2))


def plot_third_use_case(sample_size_array, threshold_MSE_array, newey_west_MSE_array):
    xs = sample_size_array
    fig = plt.figure()
    plt.xkcd()
    plt.plot(xs, threshold_MSE_array, xs, threshold_MSE_array, 'ro',  color='green')
    plt.plot(xs, newey_west_MSE_array, xs, newey_west_MSE_array, 'ro', color='red')
    plt.grid()
    fig.savefig('lol.png')
    plt.show()


def third_use_case(sample_size_min, sample_size_max, sample_size_by, replications, sigma, model, coef):

    par_list = {"sample_size_min": sample_size_min,
                "sample_size_max": sample_size_max,
                "sample_size_by": sample_size_by,
                "replications": replications,
                "sigma": sigma,
                "model": model,
                "coef": coef}

    sample_size_array = np.arange(start=sample_size_min, stop=sample_size_max, step=sample_size_by)

    # идеальный массив чисел для использования в функции precision
    ideal_array = list(np.ones(replications))

    newey_west_MSE_array = np.full(shape=len(sample_size_array), fill_value=np.nan)
    threshold_MSE_array = np.full(shape=len(sample_size_array), fill_value=np.nan)

    j = 0
    for sample_size in sample_size_array:

        newey_west_array = np.full(shape=replications, fill_value=np.nan)
        threshold_array = np.full(shape=replications, fill_value=np.nan)

        for i in range(replications):
            sample = generate_MA1(sample_size, coef=coef)

            threshold_array[i] = threshold(sample=sample)
            newey_west_array[i] = newey_west(sample=sample)

        threshold_MSE_array[j] = compute_MSE(ideal_array, threshold_array)
        newey_west_MSE_array[j] = compute_MSE(ideal_array, newey_west_array)
        j += 1

    print(threshold_MSE_array)
    print(newey_west_MSE_array)
    plot_third_use_case(sample_size_array, threshold_MSE_array, newey_west_MSE_array)


if __name__ == '__main__':
    third_use_case(sample_size_min=100, sample_size_max=1000, sample_size_by=100, replications=3, sigma=2, model='MA1',
                   coef=1)
