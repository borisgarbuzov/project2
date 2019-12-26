from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt


def plot_double_array(x_array,
                      hat_double_array,
                      true_array,
                      title,
                      x_label,
                      par_list,
                      axis='column',
                      true_label='True value',
                      y_label='value'):
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    if axis == 'row':
        hat_double_array = hat_double_array.T

    plt.style.use('seaborn')

    for ax_value in range(hat_double_array.shape[1]):
        plt.plot(x_array, hat_double_array[:, ax_value])

    plt.plot(x_array, true_array, color="black", linewidth=2,
             label=true_label)

    plt.xlabel(x_label + '\n' + caption)
    plt.ylabel(y_label)
    plt.title(title)

    plt.legend(framealpha=1, frameon=False)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
