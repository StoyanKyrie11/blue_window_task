import pandas as pd
import pygsheets
import os


def create_visualizations(csv_file_path: str) -> None:
    """
    Function creates visualizations of a CSV file using the Google Sheets API.

    :args
        csv_file_path (str): The path to the CSV file.

    :returns
        None

    :exceptions
        pygsheets.exceptions.IncorrectCellLabel
        pygsheets.exceptions.CellNotFound
        pygsheets.exceptions.SpreadsheetNotFound
        pygsheets.exceptions.RangeNotFound

    """
    try:
        gc = pygsheets.authorize(service_file=os.getcwd() + '/client_secret.json')

        # Open the Google Sheet file
        sh = gc.create("Pokemon Data Visualization")

        # Open the first worksheet (tab) in the Google Sheet
        wks = sh[0]

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Write the DataFrame to the Google Sheet
        wks.set_dataframe(df, (1, 1))

        # Add a scatter plot showing the relationship between height and weight
        scatter_chart = wks.add_chart("scatter", (10, 1), anchor_cell="A10")
        scatter_chart.set_y_axis({"name": "Weight"})
        scatter_chart.set_x_axis({"name": "Height"})
        scatter_chart.add_series({"values": (wks, (2, 4), (len(df) + 1, 4)),
                                  "categories": (wks, (2, 3), (len(df) + 1, 3))})
        scatter_chart.title = "Height vs. Weight"

        # Add a histogram of BMI values
        hist_chart = wks.add_chart("histogram", (10, 5), anchor_cell="A10")
        hist_chart.set_y_axis({"name": "Frequency"})
        hist_chart.set_x_axis({"name": "BMI"})
        hist_chart.add_series({"values": (wks, (2, 5), (len(df) + 1, 5))})
        hist_chart.title = "BMI Distribution"

        # Save changes to the Google Sheet
        sh.save()
        # Close the Google Sheet
        sh.close()
    except pygsheets.exceptions.IncorrectCellLabel as inc_label_exc:
        print(f"Incorrect cell label: {inc_label_exc}")
    except pygsheets.exceptions.CellNotFound as cell_exc:
        print(f"Cell not found: {cell_exc}")
    except pygsheets.exceptions.SpreadsheetNotFound as spr_exc:
        print(f"Spreadsheet not found: {spr_exc}")
    except pygsheets.exceptions.RangeNotFound as range_exc:
        print(f"Range not found: {range_exc}")
