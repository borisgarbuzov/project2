import numpy as np


def threshold(sample: list) -> float:
    return float(np.mean(sample))


def newey_west(sample: list) -> float:
    return float(np.median(sample))


class Estimator:

    def __init__(self, estimator):
        self.estimator = estimator
        self.threshold_array = list()
        self.newey_west_array = list()

    def estimate_lrv_threshold(self, samples):
        for sample in samples:           # sample_size
            t = threshold(sample)
            self.threshold_array.append(t)

        return self.threshold_array

    def estimate_lrv_nw(self, samples):
        for sample in samples:           # sample_size
            t = newey_west(sample)
            self.newey_west_array.append(t)

        return self.newey_west_array
