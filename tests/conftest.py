import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options
import os
from dotenv import load_dotenv

# Load biến môi trường từ file.env
load_dotenv()
@pytest.fixture(scope='session')
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope='function')
def driver():
    "Fixture create WebDriver"
    chrome_options=options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=chrome_options)
    # Return driver for test
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def browser():
    "Fixture manage to url"
    driver.get(base_url)
    return driver


