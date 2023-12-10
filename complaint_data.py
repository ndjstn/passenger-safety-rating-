import requests 
from tqdm import tqdm # Progress bar
import logging

# API URL endpoint  
URL = "https://data.cityofnewyork.us/api/views/qgea-i56i/rows.csv?date=20231203"  

# Parameters for pagination
params = {"$limit": 100_000, "$offset": 0}  

# Local file path to save data
file_path = "./data/complaints.csv"

try:
    # Stream response to avoid reading to memory 
    print("Attempting connection.")
    with requests.get(URL, params=params, stream=True) as r:  
        
        # Raise error if 4XX/5XX response
        r.raise_for_status()
        
        # User Update
        print(f"Connect to the server: {r.status_code}")

        # Init progress bar 
        progress = tqdm(desc="Downloading", total=100_000, unit=" rows")
        
        # Open/save file chunks
        print("Opening and saving file chunks.")
        with open(file_path, 'wb') as f:
        
            for chunk in r.iter_content(chunk_size=8192): 
            
                # Write chunk to file
                f.write(chunk) 
                
                # Update progress bar +1 
                progress.update(1)
                
    # Output success message 
    print(f"Data has been written to {file_path}")

except requests.RequestException as e:
    print(f"Request failed: {e}")

print("Script Complete!")