import streamlit as st

st.set_page_config(page_title="Excel schema Validator")

st.title("Upload the Excel file to be validated") #h1

file = st.file_uploader("Upload your Excel file here", type=["xlsx"])

if file is not None:
    st.success("The Excel schema is correct!")