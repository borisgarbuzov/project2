from sample import Samples
from estimator import Estimator
from plot import Plotter


if __name__ == '__main__':
    samples = Samples(sample_size=5, replication_count=5)
    samples.generate()
    samples.print()

    est = Estimator('')
    t = est.estimate_lrv_threshold(samples.samples)
    nw = est.estimate_lrv_nw(samples.samples)

    print()
    out = zip(t, nw)
    for x in out:
        print(x)

    pl = Plotter.plot(list(out))

