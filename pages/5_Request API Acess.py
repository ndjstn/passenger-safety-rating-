import streamlit as st
import requests  # Import requests to make an API call

st.title("API Access Request Form")

with st.form(key='api_request_form'):
    name = st.text_input(label='Enter your name')
    email = st.text_input(label='Enter your email')
    purpose = st.text_area(label='Describe the purpose for API access')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Here you would send the data to your backend service
    # Example: POST request to your API
    response = requests.post('https://your-backend-service.com/api/submit', json={
        'name': name,
        'email': email,
        'purpose': purpose
    })

    if response.status_code == 200:
        st.success("Your request has been successfully submitted!")
    else:
        st.error("There was an error submitting your request. Please try again.")
