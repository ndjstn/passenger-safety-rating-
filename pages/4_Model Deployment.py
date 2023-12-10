# import streamlit as st
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut
# from shapely.geometry import shape, Point
# import requests

# # Function to validate time format (HHMM)
# def is_valid_time(time_str):
#     if len(time_str) != 4 or not time_str.isdigit():
#         return False
#     hours, minutes = int(time_str[:2]), int(time_str[2:])
#     return 0 <= hours < 24 and 0 <= minutes < 60

# # Function to get latitude and longitude
# def get_lat_lon(address):
#     geolocator = Nominatim(user_agent="streamlit_app")
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except GeocoderTimedOut:
#         return None, None

# # Function to check if a point is in NYC using GeoJSON data
# def is_point_in_nyc(lat, lon, nyc_shapes):
#     point = Point(lon, lat)
#     return any(shape(poly['geometry']).contains(point) for poly in nyc_shapes['features'])

# # Fetch and parse NYC GeoJSON
# geojson_url = 'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON'
# response = requests.get(geojson_url)
# nyc_shapes = response.json()

# # Create a form for the pickup and drop-off information
# with st.form(key='my_form'):
#     st.title("Trip Information")

#     # Input fields for locations
#     pickup_location = st.text_input("Pickup Location")
#     dropoff_location = st.text_input("Drop-off Location")

#     # Text input fields for times
#     pickup_time = st.text_input("Pickup Time (HHMM format)")
#     dropoff_time = st.text_input("Drop-off Time (HHMM format)")

#     # Submit button for the form
#     submit_button = st.form_submit_button(label='Submit')

# # Handling the form submission
# if submit_button:
#     # Validate the time format
#     if not is_valid_time(pickup_time) or not is_valid_time(dropoff_time):
#         st.error("Please enter a valid time in HHMM format (e.g., 0730 for 7:30 AM).")
#     else:
#         # Get latitude and longitude for the addresses
#         pickup_lat, pickup_lon = get_lat_lon(pickup_location)
#         dropoff_lat, dropoff_lon = get_lat_lon(dropoff_location)

#         # Check if the points are within NYC
#         if pickup_lat is not None and pickup_lon is not None:
#             if is_point_in_nyc(pickup_lat, pickup_lon, nyc_shapes):
#                 st.write(f"Pickup Location: {pickup_location} (Latitude: {pickup_lat}, Longitude: {pickup_lon})")
#             else:
#                 st.write("Pickup Location not in NYC.")
#         else:
#             st.write("Pickup Location not found.")

#         if dropoff_lat is not None and dropoff_lon is not None:
#             if is_point_in_nyc(dropoff_lat, dropoff_lon, nyc_shapes):
#                 st.write(f"Drop-off Location: {dropoff_location} (Latitude: {dropoff_lat}, Longitude: {dropoff_lon})")
#             else:
#                 st.write("Drop-off Location not in NYC.")
#         else:
#             st.write("Drop-off Location not found.")

#         st.write("Pickup Time:", pickup_time[:2] + ":" + pickup_time[2:])
#         st.write("Drop-off Time:", dropoff_time[:2] + ":" + dropoff_time[2:])
import streamlit as st
import folium
from streamlit_folium import st_folium

# Function to validate time format (HHMM)
def is_valid_time(time_str):
    if len(time_str) != 4 or not time_str.isdigit():
        return False
    hours, minutes = int(time_str[:2]), int(time_str[2:])
    return 0 <= hours < 24 and 0 <= minutes < 60

# Function to get latitude and longitude
def get_lat_lon(address):
    geolocator = Nominatim(user_agent="streamlit_app")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Function to get the route
def get_route(pickup_coords, dropoff_coords, client):
    routes = client.directions(coordinates=[pickup_coords, dropoff_coords],
                               profile='driving-car',
                               format='geojson')
    return routes



# Streamlit form for input
with st.form(key='my_form'):
    st.title("Trip Information")

    pickup_location = st.text_input("Pickup Location")
    dropoff_location = st.text_input("Drop-off Location")
    pickup_time = st.text_input("Pickup Time (HHMM format)")
    dropoff_time = st.text_input("Drop-off Time (HHMM format)")

    submit_button = st.form_submit_button(label='Submit')

# Handling form submission
if submit_button:
    if not is_valid_time(pickup_time) or not is_valid_time(dropoff_time):
        st.error("Please enter a valid time in HHMM format (e.g., 0730 for 7:30 AM).")
    else:
        pickup_lat, pickup_lon = get_lat_lon(pickup_location)
        dropoff_lat, dropoff_lon = get_lat_lon(dropoff_location)

        if pickup_lat is not None and pickup_lon is not None and is_point_in_nyc(pickup_lat, pickup_lon, nyc_shapes):
            if dropoff_lat is not None and dropoff_lon is not None and is_point_in_nyc(dropoff_lat, dropoff_lon, nyc_shapes):
                # Only generate the map if it's not already in the session state
                if not st.session_state.map:
                    route = get_route((pickup_lon, pickup_lat), (dropoff_lon, dropoff_lat), ors_client)
                    m = folium.Map(location=[pickup_lat, pickup_lon], zoom_start=13)
                    folium.GeoJson(route, name='route').add_to(m)
                    folium.Marker(location=[pickup_lat, pickup_lon], popup='Pickup Location').add_to(m)
                    folium.Marker(location=[dropoff_lat, dropoff_lon], popup='Drop-off Location').add_to(m)
                    st.session_state.map = m
            else:
                st.error("Drop-off location not found or not in NYC.")
        else:
            st.error("Pickup location not found or not in NYC.")

# Display the map from session state
if st.session_state.map:
    st_folium(st.session_state.map, width=-1, height=500)