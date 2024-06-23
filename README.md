# Data Analysis Python

## Project Structure

Poniżej znajduje się struktura katalogów projektu oraz opis funkcji poszczególnych katalogów.

- **command/**: Są w nim umieszczone klasy komend (command), które odpowiadają za logike poszczególnych komend
- **command_types/**: Posiada klasy typów dla komend
- **handlers/**: W katalogu znajdują się klasy, których obsługują logike danych oraz wykresów
- **helpers/**: Klasy pomocnicze dla komend
- **resolvers/**: Obsługa pobierania odpowieniej klasy po typie

Cały kod został skonstruowany w taki sposób aby użytkownik mógł sam manipulować danymi:
- **filtracja**
- **grupowanie**
- **sortowanie**

Projekt generuje też kilka wykresów danych:

- **Rozkład wiekowy zawodników**
- **Wartośc rynkowa zawodników a ich wiek**
- **Rozkład pozycji na jakich grają piłkarze**
- **Top 10 klubów z największą ilością zawodników na euro**

W projekcie skorzystałem z wzorca projektowego "Metoda wytwórcza" tak aby tworzenie nowych komend było jak najbardziej uproszczone.