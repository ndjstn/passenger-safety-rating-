import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import requests
import os

# Site configuration
st.set_page_config(page_title="RUSAFE", layout="wide", initial_sidebar_state="expanded")

# loading of the geojson data
def load_geojson(url):
    r = requests.get(url)
    return r.json()

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

# Function to create and return a MarkerCluster
def create_marker_cluster(dataframe):
    locations = [[row['Latitude'], 
                row['Longitude']] for index, 
                row in dataframe.iterrows() if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude'])]
    return MarkerCluster(locations=locations)

# Add radio buttons for marker display options
marker_display_option = st.sidebar.radio("Choose Marker Display Option", 
                                        ('2022 Crime Data Clustered', 
                                        'Applicable Crime Clustered'))

# Page Header
st.header("Crime in NYC 2022")
# Page Information
st.write(f"""
            Please be patient with the load times as there are a lot of datapoints being addressed here. 
            So you may see a lag in the map rendering. There are {len(df)} entries being marked and 
            clustered on this map. It is interesting to note there is nothing reported for Staten Island.
            This prompted me to go back to my cleaning step and research why. The Crime rate is also far
            higher in the Bronx, but this is where Riker's Island is and crimes committed there are included
            in the Bronx.
            """)

# URL to the GeoJSON data for NYC Borough Boundaries
geojson_url = 'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON'

# load geojson for city borders
nyc_boroughs_geojson = load_geojson(geojson_url)

# Function to show/hide crimes
def show_hide_crimes():
    # Initialize a new map object
    nycmap = folium.Map(location=[40.7352763, -73.98990], 
                                zoom_start=10, 
                                tiles="OpenStreetMap")

    # Define a color mapping for boroughs
    borough_colors = {
    'Manhattan': '#FF5733',
    'Brooklyn': '#33FF57',
    'Queens': '#3357FF',
    'Bronx': '#FF33FF',
    'Staten Island': '#FFFF33'
    }

    # Function to assign color based on borough
    def style_function(feature):
        borough_name = feature['properties']['boro_name']
        return {
            'fillColor': borough_colors.get(borough_name, '#FFFFFF'), # Default color if not found
            'color': 'black', # Border color
            'weight': 1,
            'fillOpacity': 0.5
        }

    # Add GeoJSON layer with borough labels
    folium.GeoJson(
        nyc_boroughs_geojson,
        name='geojson',
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=['boro_name'])
    ).add_to(nycmap)

    if marker_display_option == '2022 Crime Data Clustered':
        clusters = create_marker_cluster(df)
        for index, row in df.iterrows():
            print(row['Lat_Lon'])
            if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
                # Define the tooltip content for each marker
                tooltip_content = f"Crime: {row['OFNS_DESC']}<br>Coordinates: {row['Latitude']}, {row['Longitude']}"
                folium.Marker(
                    location=[row['Latitude'], 
                            row['Longitude']],
                    popup=folium.Popup(tooltip_content),
                    tooltip=tooltip_content
                ).add_to(clusters)
        clusters.add_to(nycmap)
    st_folium(nycmap, width=-1)


# Call the function initially and also when the radio button selection changes
show_hide_crimes()
