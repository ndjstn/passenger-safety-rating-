import streamlit as st
from pathlib import Path
import pandas as pd




# st.header("Data Cleaning Process Of the Crime Complaints")
# df = pd.read_csv('./data/complaints.csv', nrows=10000)
# st.write(df[df['BORO_NM'] == 'STATEN ISLAND'].shape)
# # Filter for Staten Island complaints
# staten_island_complaints = df[df['BORO_NM'] == 'STATEN ISLAND']

# # Extract the year from the complaint date
# staten_island_complaints['Year'] = staten_island_complaints['CMPLNT_FR_DT']

# # Get unique years
# unique_years = staten_island_complaints['Year'].unique()

# # Display the unique years using Streamlit
# st.write("Years with complaints in Staten Island:", unique_years)

# st.write(f"The data frame is {len(df)}")
# # Get data from target year:
# # Combine the date and time columns into a single datetime column
# df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'] + ' ' + df['CMPLNT_FR_TM'], errors='coerce')
# df['CMPLNT_TO_DT'] = pd.to_datetime(df['CMPLNT_TO_DT'] + ' ' + df['CMPLNT_TO_TM'], errors='coerce')
# # Drop the time column as it's no longer needed
# df.drop('CMPLNT_FR_TM', axis=1, inplace=True)
# df.drop('CMPLNT_TO_TM', axis=1, inplace=True)
# # Filter the DataFrame to include only rows from the year 2022
# df = df[df['CMPLNT_FR_DT'].dt.year == 2022]
# st.write(df)
# st.write(f"The data frame is {len(df)}")
