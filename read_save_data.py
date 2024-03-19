from typing import Any


def save_data(pokemon_data: list[dict[str, Any]], output_file: str) -> None:
    """
    Outputs the pokemon_data to a.csv file.

    :args
        pokemon_data (List[Dict[str, Any]]): A list of dictionaries containing Pokémon data.
        output_file (str): The name of the output text file.

    :returns: None

    :exceptions
        FileNotFoundError: If the output file cannot be found.
        IOError: If there is an error writing to the output file.
    """
    try:
        with open(output_file, 'w') as file:
            for pokemon in pokemon_data:
                file.write(f"{pokemon}\n")
    except FileNotFoundError as file_err:
        print(f'FileNotFoundError: {file_err}')
    except IOError as err:
        print(f'IOError: {err}')


def read_csv(output_file: str) -> list[str]:
    """
       Reads a CSV file and returns a list of strings.

       :args
           output_file (str): The name of the CSV file to be read.

       :returns
           list[str]: A list of strings, where each string is a line from the CSV file.

       :exceptions
           FileNotFoundError: If the file cannot be found.

       """
    try:
        with open(output_file) as csv_file:
            contents = csv_file.readlines()
            refactored_lines = [line.lstrip('{').rstrip('}') for line in contents]

            return refactored_lines
    except FileNotFoundError as file_err:
        print(f'FileNotFoundError: {file_err}')
