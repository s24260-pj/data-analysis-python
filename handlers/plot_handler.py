from matplotlib import pyplot as plt

from command_types.plot_types import PlotTypes


class PlotHandler:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def generate_by_type(self, plot_type, columns):
        if plot_type == PlotTypes.types['line']:
            plt.plot(self.data[columns['x_column']], self.data[columns['y_column']])
        elif plot_type == PlotTypes.types['bar']:
            plt.bar(self.data[columns['x_column']], self.data[columns['y_column']])
        elif plot_type == PlotTypes.types['scatter']:
            plt.scatter(self.data[columns['x_column']], self.data[columns['y_column']])
        elif plot_type == PlotTypes.types['hist']:
            plt.hist(self.data[columns['y_column']])
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")

        plt.xlabel(columns['x_column'])
        plt.ylabel(columns['y_column'])

        plt.xticks(rotation='vertical')

        plt.show()
