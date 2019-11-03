import numpy as np


class Samples:

    def __init__(self, sample_size_from, sample_size_to, sample_size_step, replication_count):
        self.sample_size_from = sample_size_from
        self.sample_size_to = sample_size_to
        self.sample_size_step = sample_size_step
        self.replication_count = replication_count

        self.sample_size_array = range(self.sample_size_from, self.sample_size_to + 1, self.sample_size_step)
        self.replication_count_array = range(1, self.replication_count + 1)

        self.samples = list()

    def __getitem__(self, item):
        return self.samples[item]

    def __len__(self):
        return len(self.samples)

    def generate(self):
        for i in range(len(self.sample_size_array)):
            sample_size = self.sample_size_array[i]
            self.samples.append(list())
            for _ in self.replication_count_array:
                sample = list(np.random.normal(size=sample_size))
                self.samples[i].append(sample)
        return self.samples

    def print(self):
        for i in range(len(self.sample_size_array)):
            sample_size = self.sample_size_array[i]
            print(f'{sample_size} : ')
            for sample in self.samples[i]:
                print(f'\t{sample}')


if __name__ == '__main__':
    samples = Samples(sample_size_from=10, sample_size_to=100, sample_size_step=10, replication_count=5)
    samples.generate()
    samples.print()
