from command.command import Command
from helpers.command_helper import CommandHelper


class FilterCommand(Command):
    def __init__(self, data_handler):
        self.name = "FilterCommand"
        self.data_handler = data_handler

    def execute(self):
        columns = self.data_handler.get_header()
        column_name = CommandHelper.get_valid_parameter(columns, {
            'title': 'Możesz użyć filter dla następujących kolumn: ',
            'select': 'Wybierz kolumne: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        column_values = self.data_handler.get_unique_column_values(column_name)
        column_value = CommandHelper.get_valid_parameter(column_values, {
            'title': 'Wartości po jakich możesz filtrować dla wybranej kolumny: ',
            'select': 'Wpisz wartość po jakiej chcesz filtrować: ',
            'invalid': 'Niepoprawna wartość kolumny!!'
        })

        self.data_handler.filter(column_name, column_value)
        self.data_handler.print_data()
