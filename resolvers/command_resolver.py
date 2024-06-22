from command.filter_command import FilterCommand
from command.group_command import GroupCommand
from command.plot_command import PlotCommand
from command.sort_command import SortCommand


class CommandResolver:
    commands = {
        'filter': FilterCommand,
        'sort': SortCommand,
        'group': GroupCommand,
        'plot': PlotCommand,
    }

    @classmethod
    def get_command(cls, command):
        return cls.commands.get(command, None)
