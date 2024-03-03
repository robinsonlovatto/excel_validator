import pandas as pd
from contract import Sales

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # check for extra column in excel
        extra_cols = set(df.columns) - set(Sales.model_fields.keys())
        if extra_cols:
            return False, f"Extra columns detected in the Excel: {', '.join(extra_cols)}"

        # validate each line with the schema
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Error in line {index + 2}: {e}")
        
        return True, None
    
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"