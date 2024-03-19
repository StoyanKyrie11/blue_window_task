from typing import Any


def calculate_bmi(height: int | float, weight: int | float) -> int | float:
    """
        Calculates the body mass index (BMI) of a person.

        :args
            height (int | float): The person's height in meters.
            weight (int | float): The person's weight in kilograms.

        :returns
            int | float: The person's BMI.

        :exceptions
            ValueError: If the input data is not of a numeric type.
        """
    try:
        bmi = round(weight / (height ** 2), 2)
        return bmi
    except ValueError as error:
        raise ValueError(f"Value error: {error}")


def calculate_average_bmi(pokemon_data: list[dict[str, Any]]) -> float:
    """
       Calculates the average body mass index (BMI) of a list of Pokemon characters.

       :args
           pokemon_data (List[Dict[str, Any]]): A list of dictionaries containing the height and weight of each Pokemon.

       :returns
           float: The average BMI of the Pokemon characters in the list.

       :exceptions
           ValueError: If the input data is not a list of dictionaries.
       """
    try:
        total_bmi = sum(calculate_bmi(pokemon["height"], pokemon["weight"]) for pokemon in pokemon_data)
        average_bmi = round(total_bmi / len(pokemon_data), 2)
        return average_bmi
    except ValueError as error:
        raise ValueError(f"Value error: {error}")


def calculate_min_max_bmi(pokemon_data: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    """
        Function estimates the minimum and maximum body mass index value (BMI) of a list of Pokemon characters.

        :args
            pokemon_data (List[Dict[str, Any]]): A list of dictionaries containing the height and weight of each Pokemon.

        :returns
            tuple[dict[str, Any], dict[str, Any]]: A tuple containing the minimum and maximum BMI Pokémon data.

        :exceptions
            ValueError: If the input data is not a list of dictionaries.
        """
    try:
        max_bmi_pokemon_data = max(pokemon_data,
                                   key=lambda pokemon: calculate_bmi(pokemon["height"], pokemon["weight"]))
        min_bmi_pokemon_data = min(pokemon_data,
                                   key=lambda pokemon: calculate_bmi(pokemon["height"], pokemon["weight"]))
        return max_bmi_pokemon_data, min_bmi_pokemon_data
    except ValueError as val_error:
        raise ValueError(f"Value error: {val_error}")
