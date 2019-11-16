import os
import matplotlib.pyplot as plt


def second_use_case_plot(sample_size_array, hat_double_array, true_array,
                         est_type, par_list):
    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    plt.style.use('seaborn')

    # Newey-West
    file_name = 'output/plot for ' + est_type + str(par_list).replace(': ',
                                                                      '=') + \
                '.png'

    for row in range(len(hat_double_array)):
        plt.plot(sample_size_array, hat_double_array[row, :])

    plt.plot(sample_size_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel('sample size\n' + caption)
    plt.ylabel('value')
    plt.title('Plot for ' + est_type)

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
