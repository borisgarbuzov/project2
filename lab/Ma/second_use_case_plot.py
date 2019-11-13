import os
import re
import matplotlib.pyplot as plt
from itertools import cycle


def second_use_case_plot(sample_size_array, newey_west_array,
                         threshold_array, true_array, par_list):
    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # prepare par_list for subtitle
    symbols = re.compile(r'[{\'\'}]', flags = re.UNICODE)
    caption_text = symbols.sub("", str(par_list)).replace(':', ' =')

    lines = ["-", "--", "-.", ":", "."]
    linecycler = cycle(lines)

    plt.style.use('seaborn')

    # Newey-West
    file_name_newey_west = 'output/second case plot NW ' + str(par_list).replace(': ', '=') + '.png'

    for row in range(len(newey_west_array)):
        plt.plot(sample_size_array, newey_west_array[row, :], color = "blue")

    plt.plot(sample_size_array, true_array, color = "black", linewidth = 2,
             label = 'True value')

    plt.xlabel('sample size')
    plt.ylabel('value')
    plt.title('Plot for second use case Newey-West')

    plt.legend(framealpha = 1, frameon = False)

    plt.tight_layout()

    # add subtitle on our plot
    #plt.text(x = 5000, y = -0.2, s = caption_text, ha='center', va='center')

    plt.savefig(file_name_newey_west, dpi = 300, bbox_inches = 'tight')

    plt.close()

    # Threshold
    file_name_threshold = 'output/second case plot Threshold ' + str(par_list).replace(': ', '=') + '.png'

    for row in range(len(threshold_array)):
        plt.plot(sample_size_array, threshold_array[row, :], color = 'blue',
                 linestyle = next(linecycler))

    plt.plot(sample_size_array, true_array, color = "black", linewidth = 2,
             label = 'True value')

    plt.xlabel('sample size')
    plt.ylabel('value')
    plt.title('Plot for second use case Threshold')

    plt.legend(framealpha = 1, frameon = False)

    plt.tight_layout()

    # add subtitle on our plot
    #plt.text(x = 5000, y = -0.2, s = caption_text, ha='center', va='center')

    plt.savefig(file_name_threshold, dpi = 300, bbox_inches = 'tight')
