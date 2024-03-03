import streamlit as st

class ExcelValidatorUI:
    def __init(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(page_title="Excel schema Validator")

    def display_header(self):
        st.title("Upload the Excel file to be validated") #h1

    def upload_file(self):
        return st.file_uploader("Upload your Excel file here", type=["xlsx"])

    def display_results(self, result, error):
        if error:
            st.error(f"Validation error: {error}")
        else:
            st.success("The Excel schema is correct!")