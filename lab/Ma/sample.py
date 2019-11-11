import numpy as np


def generate(mean, sigma, sample_size):
    sample = np.random.normal(loc = mean, scale = sigma, size = sample_size)
    return sample
