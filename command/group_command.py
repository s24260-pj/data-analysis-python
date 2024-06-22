from command.command import Command
from command_types.group_types import GroupTypes
from helpers.command_helper import CommandHelper


class GroupCommand(Command):
    def __init__(self, data_handler):
        self.name = "GroupCommand"
        self.data_handler = data_handler

    def execute(self):
        columns = self.data_handler.get_header()

        key_columns = self.data_handler.get_string_columns(columns)
        first_column_name = CommandHelper.get_valid_parameter(key_columns, {
            'title': 'Możesz użyć akcji dla następujących kolumn ',
            'select': 'Wybierz kolumne dla jakiej chcesz wykonać grupowanie: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        valid_group_columns = self.data_handler.get_valid_columns_for_group(columns)
        second_column_name = CommandHelper.get_valid_parameter(valid_group_columns, {
            'title': 'Możesz użyć akcji dla następujących kolumn ',
            'select': 'Wybierz kolumne po jakiej chcesz wykonać akcje grupowania: ',
            'invalid': 'Niepoprawna nazwa kolumny!!'
        })

        group_type = CommandHelper.get_valid_parameter(GroupTypes.types, {
            'title': 'Wybierz typ grupowania ',
            'select': 'Wybierz kolumne: ',
            'invalid': 'Niepoprawny typ grupowania kolumny!!'
        })

        self.data_handler.group(first_column_name, second_column_name, group_type)
        self.data_handler.print_data()
