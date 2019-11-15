import os
import matplotlib.pyplot as plt


def first_use_case_plot(sample_size_array, newey_west_array,
                        threshold_array, true_array, par_list):
    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # create file name for plot
    file_name = 'output/plot case one ' + str(par_list).replace(': ',
                                                                '=') + '.png'

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key]) + " "
        if i % 3 == 0:
            caption += "\n"

    plt.style.use('seaborn')

    plt.plot(sample_size_array, newey_west_array, color='blue',
             label='Newey-West')
    plt.plot(sample_size_array, threshold_array, color='red',
             label='Threshold')
    plt.plot(sample_size_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel('sample size\n' + caption)
    plt.ylabel('value')
    plt.title('Plot for first use case')

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
