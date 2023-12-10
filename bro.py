import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import logging
from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor
import os

# Setup logging
logging.basicConfig(filename='data/data_processing.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s', 
                    level=logging.INFO)

# Define your preprocessor
categorical_cols = ['KY_CD', 'OFNS_DESC', 'PD_CD', 'PD_DESC', 
                    'CRM_ATPT_CPTD_CD', 'LAW_CAT_CD', 'BORO_NM', 
                    'ADDR_PCT_CD', 'LOC_OF_OCCUR_DESC', 'PREM_TYP_DESC', 
                    'PATROL_BORO']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ], remainder='drop')

def process_and_save_chunk(chunk, chunk_id):
    try:
        # Drop unnecessary columns
        columns_to_drop = ['RPT_DT', 'JURIS_DESC', 'PARKS_NM', 'HADEVELOPT', 
                           'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 
                           'TRANSIT_DISTRICT', 'Lat_Lon', 'STATION_NAME', 
                           'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX',
                           'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM']
        chunk.drop(columns=columns_to_drop, inplace=True)

        # Handle missing values
        chunk.dropna(inplace=True)

        # Apply preprocessing to the chunk
        processed_chunk = preprocessor.fit_transform(chunk)
        processed_chunk = pd.DataFrame(processed_chunk.toarray(), columns=preprocessor.get_feature_names_out())

        # Save the processed chunk to a CSV file
        processed_chunk.to_csv(f"data/preprocessed_complaints_part_{chunk_id}.csv", index=False)
        logging.info(f"Chunk {chunk_id} processed and saved successfully.")
    except Exception as e:
        logging.error(f"Error processing chunk {chunk_id}: {e}")

try:
    chunksize = 10**6  # Adjust chunksize based on your system's capability
    with ThreadPoolExecutor(max_workers=(os.cpu_count()-2)) as executor:
        for chunk_id, chunk in enumerate(tqdm(pd.read_csv("data/complaints.csv", chunksize=chunksize, low_memory=False), 
                                              desc="Processing chunks")):
            executor.submit(process_and_save_chunk, chunk, chunk_id)

    logging.info("All data chunks processed.")
except Exception as e:
    logging.error(f"An error occurred in the overall process: {e}")
