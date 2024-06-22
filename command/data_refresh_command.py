from command.command import Command


class DataRefreshCommand(Command):

    def __init__(self, data_handler):
        self.name = "DataRefreshCommand"
        self.data_handler = data_handler

    def execute(self):
        self.data_handler.refresh_data()
        print("Data has been refreshed!!")
