import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Site configuration
st.set_page_config(page_title="API Access Request Form", layout="wide", initial_sidebar_state="expanded")

st.title("API Access Request Form")

with st.form(key='api_request_form'):
    name = st.text_input(label='Enter your name')
    email = st.text_input(label='Enter your email')
    purpose = st.text_area(label='Describe the purpose for API access')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Establish a connection to the Google Sheet
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Write the data to the Google Sheet
    conn.write(
        spreadsheet=st.secrets["connections"]["gsheets"]["spreadsheet"],
        worksheet="Your_Worksheet_Name",
        data=[[name, email, purpose]]
    )
    st.success("Your request has been successfully submitted!")
