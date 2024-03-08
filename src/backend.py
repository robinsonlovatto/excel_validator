import pandas as pd
from contract import Sales
import os
from dotenv import load_dotenv

load_dotenv(".env")

# reading env variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# create the db connection url
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []
        # check for extra column in excel
        extra_cols = set(df.columns) - set(Sales.model_fields.keys())
        if extra_cols:
            return False, f"Extra columns detected in the Excel: {', '.join(extra_cols)}"

        # validate each line with the schema
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                errors.append(f"Error in line {index + 2}: {e}")
        
        # return validation result, errors and the dataframe
        return df, True, errors
    
    except ValueError as ve:
        return df, False, str(ve)
    # when error returns an empty dataframe and an error
    except Exception as e:
        return pd.DataFrame(), f"Unexpected error: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('sales', con=DATABASE_URL, if_exists='replace', index=False)    