from command.command import Command
from command_types.plot_types import PlotTypes
from handlers.plot_handler import PlotHandler
from helpers.command_helper import CommandHelper


class PlotCommand(Command):
    def __init__(self, data_handler):
        self.name = "PlotCommand"
        self.data_handler = data_handler
        self.plot_handler = PlotHandler()

    def execute(self):
        self.plot_handler.set_data(self.data_handler.data)

        columns = self.data_handler.get_header()
        x_column = CommandHelper.get_valid_parameter(columns, {
            'title': 'Możesz użyć akcji dla następujących kolumn ',
            'select': 'Wybierz kolumnę dla osi X: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        y_column = CommandHelper.get_valid_parameter(columns, {
            'title': 'Możesz użyć akcji dla następujących kolumn ',
            'select': 'Wybierz kolumnę dla osi Y: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        plot_type = CommandHelper.get_valid_parameter(PlotTypes.types, {
            'title': 'Wybierz typ wykresu ',
            'select': 'Wybierz typ wykresu: ',
            'invalid': 'Niepoprawny typ wykresu!!'
        })

        self.plot_handler.generate_by_type(plot_type, {
            'x_column': x_column,
            'y_column': y_column
        })
