import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_gsheets import GSheetsConnection

# Function to validate time format (HHMM)
def is_valid_time(time_str):
    if len(time_str) != 4 or not time_str.isdigit():
        return False
    hours, minutes = int(time_str[:2]), int(time_str[2:])
    return 0 <= hours < 24 and 0 <= minutes < 60

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
        # Update Google Sheet
        conn = st.connection("gsheets", type=GSheetsConnection)
        conn.write(
            spreadsheet="your_spreadsheet_id",  # Replace with actual ID
            worksheet="your_worksheet_name",    # Replace with actual worksheet name
            data=[[pickup_location, dropoff_location, pickup_time, dropoff_time]]
        )
        st.success("Data successfully submitted.")
