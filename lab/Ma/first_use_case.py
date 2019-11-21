import numpy as np
from sample import *
from newey_west_estimator import *
from threshold_estimator import *
from plot_two_arrays import *


def first_use_case(sample_size_min, sample_size_max, sample_size_by,
                   mean, sigma):
    # create so called par_list for subtitle in plot
    par_list = {"sample_size_min": sample_size_min,
                "sample_size_max": sample_size_max,
                "sample_size_by": sample_size_by,
                "mean": mean,
                "sigma": sigma}

    # here we create so called sample_size_array that contains all sample sizes
    sample_size_array = np.arange(start=sample_size_min,
                                  stop=sample_size_max,
                                  step=sample_size_by)
    sample_size_array = np.append(sample_size_array, sample_size_array[-1] +
                                  sample_size_by)

    true_array = np.full(shape=len(sample_size_array), fill_value=mean)

    # create 2 empty arrays for our estimations
    newey_west_array = np.full(shape=len(sample_size_array),
                               fill_value=np.nan)
    threshold_array = np.full(shape=len(sample_size_array),
                              fill_value=np.nan)

    # main cycle
    for sample_size_index in range(0, sample_size_array.size):
        sample = generate(mean=mean, sigma=sigma,
                          sample_size=sample_size_array[sample_size_index])
        newey_west_array[sample_size_index] = newey_west_estimator(
            sample=sample)
        threshold_array[sample_size_index] = threshold_estimator(
            sample=sample)
        print("Sample sizes left", sample_size_array.size -
              (sample_size_index + 1))

    # plot two estimates against sample sizes
    first_use_case_plot(sample_size_array=sample_size_array,
                        newey_west_array=newey_west_array,
                        threshold_array=threshold_array,
                        true_array=true_array,
                        par_list=par_list)


if __name__ == '__main__':
    first_use_case(sample_size_min=1005,
                   sample_size_max=10000,
                   sample_size_by=1000,
                   mean=0,
                   sigma=2)
