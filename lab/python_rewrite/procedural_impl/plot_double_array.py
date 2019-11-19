import os
import matplotlib.pyplot as plt


def plot_double_array(t_par_array,
                      hat_double_array,
                      true_array,
                      title,
                      axis,
                      ylabel,
                      par_list):
    # create directory for output if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    if axis == 'column':
        ax = 0
    elif axis == 'row':
        ax = 1
    else:
        raise ValueError('axis parameter should be \'column\' or \'row\' not '
                         + axis)

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    plt.style.use('seaborn')

    file_name = 'output/plot for ' + title + str(par_list).replace(': ',
                                                                   '=') + \
                '.png'

    for ax_value in range(hat_double_array.shape[ax]):
        plt.plot(t_par_array, hat_double_array[:, ax_value])

    plt.plot(t_par_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel(ylabel + '\n' + caption)
    plt.ylabel('value')
    plt.title(title)

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
