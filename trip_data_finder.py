import pandas as pd
import requests
import io
from tqdm import tqdm

# Different Taxi Types
TAXI_TYPES = ['yellow', 'green', 'fhv']
# Year Selection
YEAR = 2022

# Iter over all of the taxi types
for taxi_type in TAXI_TYPES:

    # User Update statement
    print(f"Processing {taxi_type} taxis.") 
    df_list = []

    # Iter over all of the months
    for month in tqdm(range(1,13)):

        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{YEAR}-{month:02d}.parquet"
        
        # Get the parquet data from New York State
        try:
            response = requests.get(url)
        except Exception as e:
            print(f"There was an error getting the data stream {e}")
        try:    
            df = pd.read_parquet(io.BytesIO(response.content))
            df_list.append(df)
        except Exception as e:
            print(f"There was an error reading the parquet file: {e}")
    # Concatonate all of the data frames together
    full_df = pd.concat(df_list, ignore_index=True)

    try:
        # Save the data in the .data folder so I don't get kicked off Github
        # https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
        csv_path = f"./data/{taxi_type}_tripdata_{YEAR}.csv"
        # User Update statement
        print(f"Saving to {csv_path}")
    except Exception as e:
        print(f"There was an error saving the dataframe to csv: {e}")

    # Save the concatonated dataframe
    try:
        full_df.to_csv(csv_path, index=False)
        # User Update statement
        print("Dataframe saved")
    except Exception as e:
        print(f"There was an error saving the dataframe: {e}")
    # Next taxi type please!

print("All done!!")