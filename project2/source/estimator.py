import numpy as np


def threshold(sample: list) -> float:
    return float(np.mean(sample))


def newey_west(sample: list) -> float:
    return float(np.median(sample))


class Estimator():

    def __init__(self, estimator):
        self.estimator = estimator
        self.threshold_array = list()
        self.newey_west = list()

    def estimate_lrv_threshold(self, samples):
        for i in range(len(samples)):           # sample_size
            self.threshold_array.append(list())

            for sample in list(samples[i]):     # replication_count
                self.threshold_array[i].append(threshold(sample))

        return self.threshold_array

    def estimate_lrv_nw(self, samples):
        for i in range(len(samples)):  # sample_size
            self.newey_west.append(list())

            for sample in list(samples[i]):  # replication_count
                self.newey_west[i].append(newey_west(sample))

        return self.newey_west
