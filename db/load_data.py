import sqlite3

from typing import Any

from calculate_bmi import calculate_bmi


def load_transformed_data(pokemon_data: list[dict[str, Any]], db_file: str) -> None:
    """
    Loads the transformed Pokémon data into an SQLite database.

    :args
        pokemon_data (list[dict[str, Any]]): List of dictionaries containing Pokémon data.
        db_file (str): Path to the SQLite database file.

    :returns
        None

    :exceptions
        Exception
    """
    # Instantiate global connection object
    global connection
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Create the pokemon_data table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_data (
            id INTEGER PRIMARY KEY,
            name TEXT,
            height REAL,
            weight REAL,
            bmi REAL
        )
        """)

        # Insert each Pokémon's data into the database
        for pokemon in pokemon_data:
            bmi = calculate_bmi(pokemon["height"], pokemon["weight"])
            cursor.execute("""
            INSERT INTO pokemon_data (id, name, height, weight, bmi)
            VALUES (?, ?, ?, ?, ?)
            """, (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"], bmi))
        # Commit changes and close the connection
        connection.commit()
    except Exception as err:
        print(f'Err: {err}')
    finally:
        connection.close()
