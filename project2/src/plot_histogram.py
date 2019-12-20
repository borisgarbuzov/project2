from os.path import dirname
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime


def plot_histogram(hat_array: np.array,
                   true_value: float,
                   title: str,
                   label: str,
                   par_list: dict):
    # create directory for output if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    output_folder = os.path.join(parent_dir, "output")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # create file name for plot
    now = datetime.datetime.now()
    file_name = os.path.join(output_folder, 'plot for ') + title + str(
        par_list).replace(': ', '=') + '_' + now.strftime("%H;%M;%S;%f") + \
                '.png'

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    plt.style.use('seaborn')

    plt.hist(hat_array, color='red', alpha=0.7, label=label)

    plt.axvline(true_value, color='blue', label="true lrv", linewidth=3)

    plt.xlabel("values" + '\n' + caption)
    plt.title(title)

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()