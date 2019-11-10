import numpy as np


def threshold(sample):
    return float(np.mean(sample.get_sample()))


def newey_west(sample):
    return float(np.median(sample.get_sample()))
