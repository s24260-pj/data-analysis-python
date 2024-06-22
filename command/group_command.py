from command.command import Command
from command_types.group_types import GroupTypes
from helpers.command_helper import CommandHelper


class GroupCommand(Command):
    def __init__(self, data_handler):
        self.name = "GroupCommand"
        self.data_handler = data_handler

    def execute(self):
        columns = self.data_handler.get_header()

        string_columns = self.data_handler.get_string_columns(columns)
        first_column_name = CommandHelper.get_valid_parameter(string_columns, {
            'title': 'You can use actions for the following columns ',
            'select': 'Select the column for which you want to group: ',
            'invalid': 'Invalid column name!!'
        })

        numeric_columns = self.data_handler.get_numeric_columns(columns)
        second_column_name = CommandHelper.get_valid_parameter(numeric_columns, {
            'title': 'You can use actions for the following columns ',
            'select': 'Select the column on which you want to perform grouping actions: ',
            'invalid': 'Invalid column name!!'
        })

        group_type = CommandHelper.get_valid_parameter(GroupTypes.types, {
            'title': 'Select group type ',
            'select': 'Select column: ',
            'invalid': 'Invalid group column type!!'
        })

        self.data_handler.group(first_column_name, second_column_name, group_type)
        self.data_handler.print_data()
