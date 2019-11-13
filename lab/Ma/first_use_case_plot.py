import os
import re
import matplotlib.pyplot as plt


def first_use_case_plot(sample_size_array, newey_west_array,
                        threshold_array, true_array, par_list):

    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # create file name for plot
    file_name = 'output/plot case one ' + str(par_list).replace(': ', '=') + '.png'

    # prepare par_list for subtitle
    symbols = re.compile(r'[{\'\'}]', flags = re.UNICODE)
    caption_text = symbols.sub("", str(par_list)).replace(':', ' =')

    plt.style.use('seaborn')

    plt.plot(sample_size_array, newey_west_array, color = 'blue',
             label = 'Newey-West')
    plt.plot(sample_size_array, threshold_array, color = 'red',
             label = 'Threshold')
    plt.plot(sample_size_array, true_array, color = "black", linewidth = 2,
             label = 'True value')

    plt.xlabel('sample size')
    plt.ylabel('value')
    plt.title('Plot for first use case')

    # legend automatically choose best place
    plt.legend(framealpha = 1, frameon = False)

    plt.tight_layout()

    # add subtitle on our plot
    #plt.text(x = 5000, y = -0.2, s = caption_text, ha='center', va='center')

    plt.savefig(file_name, dpi = 300, bbox_inches = 'tight')
