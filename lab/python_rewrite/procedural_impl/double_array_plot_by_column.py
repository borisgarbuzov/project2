import os
import matplotlib.pyplot as plt


def double_array_plot_by_column(t_par_array,
                                hat_double_array,
                                true_array,
                                title,
                                par_list):
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

    file_name = 'output/plot for ' + title + str(par_list).replace(': ',
                                                                   '=') + \
                '.png'

    for column in range(hat_double_array.shape[1]):
        plt.plot(t_par_array, hat_double_array[:, column])

    plt.plot(t_par_array, true_array, color="black", linewidth=2,
             label='True value')

    plt.xlabel('t par\n' + caption)
    plt.ylabel('value')
    plt.title('Autocovariance')

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
