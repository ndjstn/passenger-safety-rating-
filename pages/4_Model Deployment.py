import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_gsheets import GSheetsConnection
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

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
        st.error("Please enter a valid time in HHMM format.")
    else:
        pickup_lat, pickup_lon = get_lat_lon(pickup_location)
        dropoff_lat, dropoff_lon = get_lat_lon(dropoff_location)

        if pickup_lat is not None and pickup_lon is not None:
            if dropoff_lat is not None and dropoff_lon is not None:
                # Update Google Sheet
                conn = st.connection("gsheets", type=GSheetsConnection)
                conn.write(
                    spreadsheet="your_spreadsheet_id",  # Replace with actual ID
                    worksheet="your_worksheet_name",    # Replace with actual worksheet name
                    data=[[pickup_location, dropoff_location, pickup_time, dropoff_time]]
                )

                # Generate and display map
                m = folium.Map(location=[pickup_lat, pickup_lon], zoom_start=13)
                folium.Marker(location=[pickup_lat, pickup_lon], popup='Pickup Location').add_to(m)
                folium.Marker(location=[dropoff_lat, dropoff_lon], popup='Drop-off Location').add_to(m)
                st.session_state.map = m
            else:
                st.error("Drop-off location not found.")
        else:
            st.error("Pickup location not found.")

# Display the map from session state
if 'map' in st.session_state:
    st_folium(st.session_state.map, width=-1, height=500)
