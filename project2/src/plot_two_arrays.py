import os
import matplotlib.pyplot as plt


def plot_two_arrays(x_array, first_array, first_label, second_array,
                    second_label, true_array, title,
                    x_label, par_list, y_label='value'):
    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # create file name for plot
    file_name = 'output/plot for ' + title + str(par_list).replace(': ',
                                                                   '=') + '.png'

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    plt.style.use('seaborn')

    plt.plot(x_array, first_array, color='blue', label=first_label)
    plt.plot(x_array, second_array, color='red', label=second_label)
    plt.plot(x_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
