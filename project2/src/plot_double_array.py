from os.path import dirname
import matplotlib.pyplot as plt
import os


def plot_double_array(x_array,
                      hat_double_array,
                      true_array,
                      title,
                      x_label,
                      par_list,
                      axis='column',
                      y_label='value'):
    # create directory for output if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    output_folder = os.path.join(parent_dir, "output")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    if axis == 'row':
        hat_double_array = hat_double_array.T

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    plt.style.use('seaborn')

    file_name = os.path.join(output_folder, 'plot for') + title + str(
        par_list).replace(': ', '=') + '.png'

    for ax_value in range(hat_double_array.shape[1]):
        plt.plot(x_array, hat_double_array[:, ax_value])

    plt.plot(x_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
