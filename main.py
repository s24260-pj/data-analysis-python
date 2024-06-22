from resolvers.command_resolver import CommandResolver
from handlers.data_handler import DataHandler


def main():
    try:
        file_path = input("Podaj ścieżkę do pliku CSV: ")
        data_handler = DataHandler(file_path)
    except FileNotFoundError:
        print("Nie znaleziono takiego pliku spróbuj jeszcze raz!")
        main()

    while True:
        print("Lista poleceń: " + ", ".join(CommandResolver.commands))
        command_name = input("Wpisz wybierz polecenie (lub wpisz 'exit' aby wyjść): ")

        if command_name == "exit":
            break

        command_class_name = CommandResolver.get_command(command_name)

        if command_class_name is None:
            print("Niepoprawna komenda!!!")
            continue

        command = command_class_name(data_handler)
        command.execute()


if __name__ == "__main__":
    main()
