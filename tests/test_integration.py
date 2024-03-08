import pandas as pd
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

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM sales', con=DATABASE_URL)

    # check if dataframe has data
    assert not df.empty, "The dataframe is empty."

    # check the schema (columns and datatypes)
    expected_dtype = {
        'email': 'object', # object in Pandas is the same as string in SQL
        'date': 'datetime64[ns]',
        'price': 'float64',  
        'quantity': 'int64',
        'product': 'object',
        'category': 'object'
    }

    assert df.dtypes.to_dict() == expected_dtype, "The dataframe schema does not match with the expected schema."