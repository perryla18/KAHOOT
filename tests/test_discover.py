from src.pages.discovery import Discovery
from src.utils.credentials import get_credentials

def test_discovery(driver):
    discover = Discovery(driver)
    email, pasword = get_credentials()
    discover.loginsuccess(email, pasword)
    assert discover.navigate_to_discovery()