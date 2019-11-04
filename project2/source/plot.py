from matplotlib import pyplot as plt


class Plotter:

    @staticmethod
    def plot(to_plot):
        xs = len(to_plot)

        first = list()
        second = list()

        for item in to_plot:
            first.append(item[0])
            second.append(item[1])

        fig = plt.figure()
        plt.xkcd()
        plt.plot(xs, first, xs, first, 'ro', color='green')
        plt.plot(xs, second, xs, second, 'ro', color='red')
        plt.grid()
        fig.savefig('./project2/output/lol.png')
        plt.show()
