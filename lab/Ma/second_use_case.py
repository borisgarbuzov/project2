import numpy as np
from sample import *
from newey_west_estimator import *
from threshold_estimator import *
from second_use_case_plot import *


def second_use_case(sample_size_min, sample_size_max, sample_size_by,
                    replications, mean, sigma):
    par_list = {"sample_size_min": sample_size_min,
                "sample_size_max": sample_size_max,
                "sample_size_by": sample_size_by,
                "replications": replications,
                "mean": mean,
                "sigma": sigma}

    sample_size_array = np.arange(start=sample_size_min,
                                  stop=sample_size_max,
                                  step=sample_size_by)
    sample_size_array = np.append(sample_size_array, sample_size_array[-1] +
                                  sample_size_by)

    true_array = np.full(shape=len(sample_size_array), fill_value=mean)

    newey_west_double_array = np.full(shape=(replications,
                                             len(sample_size_array)),
                                      fill_value=np.nan)
    threshold_double_array = np.full(shape=(replications,
                                            len(sample_size_array)),
                                     fill_value=np.nan)

    for sample_size_index in range(0, sample_size_array.size):
        for replication in range(replications):
            sample = generate(mean=mean, sigma=sigma,
                              sample_size=sample_size_array[sample_size_index])
            newey_west_double_array[
                replication, sample_size_index] = newey_west_estimator(
                sample=sample)
            threshold_double_array[
                replication, sample_size_index] = threshold_estimator(
                sample=sample)

    # plot Newey-West
    second_use_case_plot(sample_size_array=sample_size_array,
                         hat_double_array=newey_west_double_array,
                         true_array=true_array,
                         est_type="Newey-West",
                         par_list=par_list)

    # plot Threshold
    second_use_case_plot(sample_size_array=sample_size_array,
                         hat_double_array=threshold_double_array,
                         true_array=true_array,
                         est_type="Threshold",
                         par_list=par_list)


if __name__ == '__main__':
    second_use_case(sample_size_min=1000, sample_size_max=10000,
                    sample_size_by=1000, replications=5, mean=0,
                    sigma=2)
