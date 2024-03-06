import pandas as pd
from contract import Sales

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
        return True, errors
    
    #except ValueError as ve:
    #    return False, str(ve)
    # when error returns an empty dataframe and an error
    except Exception as e:
        return pd.DataFrame(), f"Unexpected error: {str(e)}"