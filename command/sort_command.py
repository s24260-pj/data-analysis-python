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
            'title': 'You can use sorting for the following columns ',
            'select': 'Select column: ',
            'invalid': 'Invalid column name!!'
        })

        sort_type = CommandHelper.get_valid_parameter(SortTypes.types, {
            'title': 'Select sort type',
            'select': 'Select type: ',
            'invalid': 'Invalid sort type!!'
        })

        self.data_handler.sort_by_column(column_name, sort_type)
        self.data_handler.print_data()
