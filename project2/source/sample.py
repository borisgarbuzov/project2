import numpy as np


class Samples:

    def __init__(self, sample_size, replication_count):
        self.sample_size = sample_size
        self.replication_count = replication_count
        self.samples = list()

    def generate(self):
        for i in range(1, self.replication_count + 1):
            sample = list(np.random.normal(size=self.sample_size))
            self.samples.append(sample)

    def print(self):
        for sample in self.samples:
            print(f'\t{sample}')


if __name__ == '__main__':
    samples = Samples(sample_size=3, replication_count=5)
    samples.generate()
    samples.print()
