import matplotlib.pyplot as plt


def first_use_case_plot(sample_size_array, newey_west_array,
                        threshold_array, par_list):
    plt.plot(sample_size_array, newey_west_array, color = 'blue',
             label = 'Newey-West')
    plt.plot(sample_size_array, threshold_array, color = "red",
             label = "Threshold")
    plt.legend(framealpha = 1, frameon = True)
