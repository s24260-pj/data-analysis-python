from resolvers.command_resolver import CommandResolver
from handlers.data_handler import DataHandler


def main():
    try:
        file_path = input("Provide the path to the CSV file: ")
        data_handler = DataHandler(file_path)
    except FileNotFoundError:
        print("No such file found, please try again!")
        main()

    while True:
        print("Command list: " + ", ".join(CommandResolver.commands))
        command_name = input("Type select command (or type 'exit' to exit): ")

        if command_name == "exit":
            break

        command_class_name = CommandResolver.get_command(command_name)

        if command_class_name is None:
            print("Invalid command!!!")
            continue

        command = command_class_name(data_handler)
        try:
            command.execute()
        except ValueError as error:
            print(str(error))
            break


if __name__ == "__main__":
    main()
