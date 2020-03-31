import matplotlib.pyplot as plt
from os.path import dirname
import os


def plot_hist(array, name, title, show):
    # create directory for output if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    output_folder = os.path.join(parent_dir, "output")
    plt.hist(array)
    plt.title(title)
    name = os.path.join(output_folder, name + '.png')
    plt.savefig(name)
    plt.show()
