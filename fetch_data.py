import aiohttp
import asyncio

from typing import Any


async def fetch_pokemon(session, pokemon_url) -> dict[str, Any] | None:
    """
        Fetches information for a single Pokémon from the PokéAPI.

        :args
            session (aiohttp.ClientSession): The HTTP client session to use for making requests.
            pokemon_url (str): The URL of the Pokémon resource to retrieve.

        :returns
            dict: A dictionary containing the information for the requested Pokémon, or None if the request failed.

        :exceptions
            aiohttp.ClientResponseError: If the request failed for any reason.
        """
    try:
        async with session.get(pokemon_url) as response:
            if response.status == 200:
                pokemon_data = await response.json()
                return {
                    "id": pokemon_data["id"],
                    "name": pokemon_data["name"],
                    "height": pokemon_data["height"],
                    "weight": pokemon_data["weight"],
                    "bmi": round((pokemon_data["weight"] / pokemon_data["height"] ** 2), 2),
                }
            else:
                print(f"Failed to fetch data for {pokemon_url}")
                return None
    except aiohttp.ClientResponseError as error:
        print(f'Client Error: {error}')


async def fetch_all_pokemon(base_url="https://pokeapi.co/api/v2/pokemon/") -> tuple[Any]:
    """
       Fetches information of the first 50 rows of the transformed Pokémon data.

        :args
            base_url (str): The URL of the Pokémon resource to retrieve.

        :returns
           A list of dictionaries containing the information for each Pokémon, or an empty list if no Pokémon
           could be retrieved.

        :exceptions
            aiohttp.ClientResponseError
       """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url, params={"limit": 50}) as response:
                if response.status == 200:
                    data = await response.json()
                    pokemon_urls = [pokemon["url"] for pokemon in data["results"]]
                    tasks = [fetch_pokemon(session, pokemon_url) for pokemon_url in pokemon_urls]
                    return await asyncio.gather(*tasks)
                else:
                    print("Failed to fetch Pokémon data")
                    return tuple()
    except aiohttp.ClientResponseError as error:
        print(f'Client Error: {error}')
