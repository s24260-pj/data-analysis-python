from command.data_refresh_command import DataRefreshCommand
from command.filter_command import FilterCommand
from command.group_command import GroupCommand
from command.analise_command import AnaliseCommand
from command.sort_command import SortCommand


class CommandResolver:
    commands = {
        'filter': FilterCommand,
        'sort': SortCommand,
        'group': GroupCommand,
        'analise': AnaliseCommand,
        'data_refresh': DataRefreshCommand,
    }

    @classmethod
    def get_command(cls, command):
        return cls.commands.get(command, None)
