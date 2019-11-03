from sample import Samples
from estimator import Estimator


if __name__ == '__main__':
    samples = Samples(sample_size_from=1, sample_size_to=10, sample_size_step=1, replication_count=5)
    samples.generate()
    samples.print()

    est = Estimator('')
    t = est.estimate_lrv_threshold(samples)
    nw = est.estimate_lrv_nw(samples)

    print()

    for x in t:
        print(x)

    print()

    for x in nw:
        print(x)

