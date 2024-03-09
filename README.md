# Validate Excel with Pydantic then save data to DB

A small project to validate data from an Excel file using Pydantic, then the data is saved in PostgreSQL database.
The frontend is built using Streamlit and can be acessed in the link

### Installation

1. Clone the repository:
```bash
git clone https://github.com/robinsonlovatto/validate_excel_pydantic.git
cd validate_excel_pydantic
```
2. Configure the right version of Python with `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Install the project dependencies:
```bash
#create the virtual env
python -m venv .venv

# activate the virtual env (windows based)
source .venv/Scripts/Activate

# install the dependencies
pip install -r requirements.txt  
```

4. Commands to run the app and the tests:
```bash
# run the streamlit app
task run

# run the automated tests
task tests
```

