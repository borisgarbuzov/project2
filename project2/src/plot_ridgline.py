from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import joypy


def plot_ridgline(hat_double_array,
                  title,
                  x_label,
                  par_list,
                  bins=10):
    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    joypy.joyplot(hat_double_array, hist=True, bins=bins, overlap=0, grid=True,
                  legend=False)

    plt.xlabel(x_label + '\n' + caption)
    plt.title(title)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
