import numpy as np


def threshold_estimator(sample):
    threshold = np.var(sample)
    return threshold
