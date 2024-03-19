import asyncio
import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions

from calculate_bmi import calculate_average_bmi, calculate_min_max_bmi
from db.load_data import load_transformed_data
from fetch_data import fetch_all_pokemon
from read_save_data import save_data


async def main():
    pokemon_data = await fetch_all_pokemon()
    load_transformed_data(pokemon_data, "pokemon.db")


if __name__ == "__main__":
    # Instantiate options object from PipelineOptions class
    options = PipelineOptions()
    # Beam context manager - pass PipelineOptions object and execute asynchronously
    with beam.Pipeline(options=PipelineOptions()) as pipeline:
        loop = asyncio.new_event_loop()
        # Fetch details for each Pokémon asynchronously
        pokemon_details = loop.run_until_complete(fetch_all_pokemon())
        # Calculate average_bmi
        average_bmi = calculate_average_bmi(pokemon_details)
        # Unpack max and min bmi values
        max_bmi_pokemon, min_bmi_pokemon = calculate_min_max_bmi(pokemon_details)
        # Print the extracted details
        print(f'First 50 Pokemon characters\' data: {pokemon_details}')
        print(f"Average BMI of all Pokémon characters: {average_bmi}")
        print(f"Maximum BMI value of all Pokémon characters: {max_bmi_pokemon}")
        print(f"Minimum BMI value of all Pokémon characters: {min_bmi_pokemon}")

        # Save the results into a file in .txt format
        output_file_name = "pokemon_data.csv"
        save_data(pokemon_details, output_file_name)

        # Create visualizations of extracted .csv Pokemon character data
        # create_visualizations(output_file_name)

        # Inject data into the SQL pokemon_data DB
        asyncio.run(main())

        # Init the pipeline, create Apache Beam API pipeline objects
        (
                pipeline
                | 'Create PCollections' >> beam.Create(pokemon_details)
                | 'Print First 50 Rows' >> beam.Map(print)
        )
