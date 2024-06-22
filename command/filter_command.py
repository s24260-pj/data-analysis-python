from command.command import Command
from helpers.command_helper import CommandHelper


class FilterCommand(Command):
    def __init__(self, data_handler):
        self.name = "FilterCommand"
        self.data_handler = data_handler

    def execute(self):
        columns = self.data_handler.get_header()
        column_name = CommandHelper.get_valid_parameter(columns, {
            'title': 'You can use filter for the following columns:',
            'select': 'Select column: ',
            'invalid': 'Invalid column name!!'
        })

        column_values = self.data_handler.get_unique_column_values(column_name)
        column_value = CommandHelper.get_valid_parameter(column_values, {
            'title': 'Values by which you can filter for the selected column: ',
            'select': 'Enter the value you want to filter by: ',
            'invalid': 'Invalid column name!!'
        })

        self.data_handler.filter(column_name, column_value)
        self.data_handler.print_data()
