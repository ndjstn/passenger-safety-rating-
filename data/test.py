import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import requests
import os



def load_crime_data(download_url):
    r = requests.get(download_url, stream=True)
    if r.status_code == 200:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:  # filter out keep-alive new chunks
                print(chunk)
                

dropbox_url = "https://www.dropbox.com/scl/fi/gjaxaw6bz5c20kzgdurao/2022_final_clean_complaints.csv?rlkey=1sjg3g5pp19suolykdrwlcakz&dl=1"

# Local path and Dropbox URL
df = load_crime_data(dropbox_url)
print(df)