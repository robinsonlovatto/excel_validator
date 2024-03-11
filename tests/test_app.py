from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os

# this decorator run for each test
@pytest.fixture
def driver():
    # run streamlit in background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    options = Options()
    options.headless = True

    # define which driver is to use
    driver = webdriver.Firefox(options=options)

    # define a timeout
    driver.set_page_load_timeout(5) # 5s

    yield driver

    # close webdriver and streamlit after the test
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # check if page opens
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title_is(driver):
    # check if page opens
    driver.get("http://localhost:8501")
    sleep(5)
    # get page title
    page_title = driver.title

    # check if title is the expected one
    expected_title = "Excel schema Validator"
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
     # check if page opens
    driver.get("http://localhost:8501")
    sleep(5)

    # get the first h1
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # check if h1 element is the expected one
    expected_text = "Upload the Excel file to be validated"
    assert h1_element.text == expected_text

def test_check_user_can_upload_an_excel_and_receive_a_message(driver):
     # check if page opens
    driver.get("http://localhost:8501")
    sleep(5)

    # upload a file successfully
    success_file_path = os.path.abspath("data/valid_file.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    # wait for the success message
    sleep(5)

    assert "The Excel schema is correct!" in driver.page_source