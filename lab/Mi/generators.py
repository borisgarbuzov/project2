import numpy as np
import sample


def generate1(sample_size):
    new_sample = sample.Sample(np.random.normal(size=sample_size))
    return new_sample