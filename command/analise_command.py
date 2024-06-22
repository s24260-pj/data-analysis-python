from command.command import Command
from command_types.chart_types import ChartTypes
from handlers.plot_handler import PlotHandler
from helpers.command_helper import CommandHelper


class AnaliseCommand(Command):
    def __init__(self, data_handler):
        self.name = "PlotCommand"
        self.data_handler = data_handler
        self.plot_handler = PlotHandler()

    def execute(self):
        self.plot_handler.set_data(self.data_handler.data_backup)

        type = CommandHelper.get_valid_parameter(["1", "2", "3", "4"], {
            'title': 'Select the type of chart you want to generate [\n'
                     '1: Age Distribution of Players, \n'
                     '2: Market Value vs Age of Players, \n'
                     '3: Positional Distribution of Players, \n'
                     '4: Top 10 Clubs by Number of Players \n'
                     '] ',
            'select': 'Select number: ',
            'invalid': 'Invalid number!!'
        })

        self.plot_handler.generate_by_type(ChartTypes.types[type])
