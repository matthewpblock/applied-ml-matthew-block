import pandas as pd
import os


# Get the directory where the script is located
# Since the CSV is in the same folder, we can just use its name.
file_path = 'coral_reef_sites.csv'
try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Print the first 5 rows of the DataFrame to verify it's loaded correctly
    print("Successfully loaded coral_reef_sites.csv into a DataFrame.")
    print("Here are the first 5 rows:")
    print(df.head())

except FileNotFoundError:
    print(f"Error: The file could not be found at the path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
