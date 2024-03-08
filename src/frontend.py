import streamlit as st

class ExcelValidatorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(page_title="Excel schema Validator")

    def display_header(self):
        st.title("Upload the Excel file to be validated") #h1

    def upload_file(self):
        return st.file_uploader("Upload your Excel file here", type=["xlsx"])

    def display_results(self, result, errors):
        if errors:
            for error in errors:
                st.error(f"Validation error: {error}")
        else:
            st.success("The Excel schema is correct!")

    def display_save_button(self):
        return st.button("Save to DB")
    
    def display_wrong_message(self):
        return st.error("You need to fix the spreadsheet")
    
    def display_success_message(self):
        return st.success("Data succesfully save to DB!")