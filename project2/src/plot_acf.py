from src.plot_preparations import plot_preparations
import matplotlib.pyplot as plt
import numpy as np


def plot_acf(cov_hat,
             cloud,
             max_lag_array="auto",
             par_list="",
             title="ACF"):
    if max_lag_array == "auto":
        max_lag_array = [lag for lag in range(len(cov_hat))]

    file_name, caption = plot_preparations(title=title, par_list=par_list)

    plt.style.use('seaborn')

    plt.stem(max_lag_array, cov_hat, use_line_collection=True)
    plt.axhspan(cloud, np.negative(cloud), alpha=0.1, color='blue')

    plt.xlabel("lags" + '\n' + caption)
    plt.ylabel("correlation")
    plt.title(title)

    plt.tight_layout()

    plt.savefig(file_name, dpi=300, bbox_inches='tight')

    plt.close()
