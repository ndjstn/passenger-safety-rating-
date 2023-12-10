# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# import json
# import requests

# # Site configuration
# st.set_page_config(page_title="RUSAFE", 
#                     layout="wide", 
#                     page_icon=":shark:",
#                     initial_sidebar_state="expanded",
#                     )

# # Site Header
# st.header("Ride Share Safety")
# st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])# Message Center
# if 'header_text' not in st.session_state: # Init the session state
#     st.session_state.header_text = "Here are the results by borough."

# st.write(st.session_state.header_text)

# # Split the screen into two columns for map and other content
# col1, col2 = st.columns((2, 1))  # Adjust the ratio as needed

# # Use the first column to display the map
# with col1:

#     # URL to the GeoJSON data for NYC Borough Boundaries
#     geojson_url = 'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON'
    
#     # Make a request to get the GeoJSON data
#     r = requests.get(geojson_url)
#     nyc_boroughs_geojson = r.json()

#     nycmap = folium.Map(location=[40.7352763,-73.98990],  # Updated coordinates for better centering
#                         zoom_start=10,
#                         tiles="OpenStreetMap")           # Adjust zoom level as needed
    
#     # Function to return a style dictionary
#     def my_style_func(feature):
#         return {
#             'fillColor': 'none',    # adjust fill on the basis of danger rating?
#             'color': 'blue',        # borough border coloring
#             'weight': 1,            
#             'fillOpacity': 0.0              
#         }

#     # Function to return a tooltip for each feature (borough)
#     def my_tooltip_func(feature):
#         boro_name = feature['properties']['boro_name']
#         return f'{boro_name} - Borough'

#     # Add GeoJSON layer to the map with custom tooltips
#     geojson_layer = folium.GeoJson(
#         nyc_boroughs_geojson,
#         name='geojson',
#         style_function=my_style_func,
#         tooltip=folium.features.GeoJsonTooltip(
#             fields=['boro_name'],
#             aliases=[''],
#             style=('background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 4px;')
#         )
#     )

#     # Apply the custom tooltip function to each feature
#     for feature in geojson_layer.data['features']:
#         tooltip_text = my_tooltip_func(feature)
#         tooltip = folium.Tooltip(tooltip_text)
#         geojson_layer.add_child(tooltip)

#     geojson_layer.add_to(nycmap)

#     # Display map in Streamlit
#     st_folium(nycmap, width=-1)

#     # Save to html file
#     nycmap.save('nyc_boros.html')

# with col2:
#     st.write("Pick Up Location")
#     pickup_time = st.time_input("What time (24 HR Time)", key=1)
#     pickup_num = st.number_input("Street Address Number", step=1, format="%d", key=2)
#     pickup_street = st.text_input("Pick Up Street", key=3)
#     st.write("Drop Off Location")
#     dropoff_time = st.time_input("Estimated Drop Off Time (24 HR Time)", key=4)
#     dropoff_num = st.number_input("Street Address Number", step=1, format="%d", key=5)
#     dropoff_street = st.text_input("Drop Off Street", key=6)
#     if st.button("Submit Trip"):
#         st.session_state.header_text = f"""Pickup is at {pickup_time:%H:%M} hrs at:
#                                      {pickup_num} {pickup_street}. 
#                                      Dropoff at {dropoff_time:%H:%M} hrs at {dropoff_num} {dropoff_street}."""
#         st.experimental_rerun()


import streamlit as st
from pathlib import Path

# Read the About me to the site 
st.write(Path("./README.md").read_text())

