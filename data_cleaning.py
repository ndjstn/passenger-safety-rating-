import pandas as pd


df = pd.read_csv("data/complaints.csv", low_memory=False)
print(f"The data frame is {df.size}")

# Combine date and time columns into single datetime columns
df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'] + ' ' + df['CMPLNT_FR_TM'], errors='coerce')
df['CMPLNT_TO_DT'] = pd.to_datetime(df['CMPLNT_TO_DT'] + ' ' + df['CMPLNT_TO_TM'], errors='coerce')

# Drop the original time columns
df.drop(['CMPLNT_FR_TM', 'CMPLNT_TO_TM'], axis=1, inplace=True)

# Filter the DataFrame to include only rows from the year 2022
df = df[df['CMPLNT_FR_DT'].dt.year == 2022]



print(f"The cleaned data frame size is {df.size}")
print(df.head)
df.to_csv("data/2022complaints.csv")