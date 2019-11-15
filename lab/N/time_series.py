import numpy as np
from abc import ABC, abstractmethod


class TimeSeries(ABC):

    @abstractmethod
    def generate(self):
        pass


class MA1(TimeSeries):

    def __init__(self, sample_size, coef=1):
        self.sample_size = sample_size
        self.coef = coef
        self.sample = np.zeros(self.sample_size)
        self.generate()

    def generate(self):
        noise = np.random.normal(size=self.sample_size + 1)
        for i in range(self.sample_size):
            self.sample[i] = noise[i + 1] + self.coef * noise[i]
        return self
