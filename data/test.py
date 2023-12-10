import requests
import pandas as pd
import os

def load_crime_data(file_path, download_url):
    # Check if the file exists locally
    if not os.path.exists(file_path):
        # File doesn't exist, download it
        r = requests.get(download_url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        else:
            raise Exception("Failed to download the file")

    # Load the CSV into a DataFrame and return
    return pd.read_csv(file_path)

# Replace with your Google Drive download URL
google_drive_url = "https://drive.google.com/uc?export=download&id=1_3_cbNeVR4yulivO7ddVV75QlHxuy9mN"

# Use the function to load data
df = load_crime_data('data/2022_final_clean_complaints.csv', google_drive_url)
print(df)