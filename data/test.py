import streamlit as st
from streamlit_gsheets import GSheetsConnection

url="https://docs.google.com/spreadsheets/d/1u7fX9Zf2K6AC7HbEzPO5ZfVzCCF8zQTXyXMUEt0Z3CI/edit?usp=sharing"

conn = st.connection("gsheets",type=GSheetsConnection, 
                    worksheet="544952461")
df = conn.read(spreadsheet=url)

st.write(df)