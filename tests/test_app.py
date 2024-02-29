from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
import subprocess

# this decorator run for each test
@pytest.fixture
def driver():
    # run streamlit in background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # define which driver is to use
    driver = webdriver.Firefox()

    # define a timeout
    driver.set_page_load_timeout(5) # 5s

    yield driver

    # close webdriver and streamlit after the test
    driver.quit()
    process.kill()

def test_app_open(driver):
    # check if page open
    driver.get("http://localhost:8501")
    sleep(5)
