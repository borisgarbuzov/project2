from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import numpy as np


def plot_arrays(x_array,
                arrays_dict,
                title,
                x_label,
                par_list="",
                true_array=np.array([]),
                true_label="True value",
                y_label='value'):

    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    for label, array in arrays_dict.items():
        plt.plot(x_array, array, label=label)

    if true_array.any():
        plt.plot(x_array, true_array, color="black", linewidth=2,
                 label=true_label)

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    # legend automatically choose best place
    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
