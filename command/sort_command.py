from command.command import Command
from command_types.sort_types import SortTypes
from helpers.command_helper import CommandHelper


class SortCommand(Command):
    def __init__(self, data_handler):
        self.name = "SortCommand"
        self.data_handler = data_handler

    def execute(self):
        columns = self.data_handler.get_header()
        column_name = CommandHelper.get_valid_parameter(columns, {
            'title': 'Możesz użyć sortowania dla następujących kolumn ',
            'select': 'Wybierz kolumne: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        sort_type = CommandHelper.get_valid_parameter(SortTypes.types, {
            'title': 'Wybierz typ grupowania ',
            'select': 'Wybierz kolumne: ',
            'invalid': 'Niepoprawny typ grupowania kolumny!!'
        })

        self.data_handler.sort_by_column(column_name, sort_type)
        self.data_handler.print_data()
