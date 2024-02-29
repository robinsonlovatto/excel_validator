from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

# define which driver is to use
driver = webdriver.Firefox()

# define a timeout
driver.set_page_load_timeout(5) # 5s

# try except to access the page
try: 
    driver.get("http://localhost:8501")
    sleep(5)
    print("Accessed the page succesfully")
except TimeoutException:
    print("Timeout")
finally:
    driver.quit()