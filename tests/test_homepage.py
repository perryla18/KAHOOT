from src.pages.HomePage import HomePage
from src.utils.credentials import get_credentials


def test_navigate_to_login_page(driver):
    home = HomePage(driver)
    email, password = get_credentials()
    assert home.login_to_Kahoot(email, password)

def test_explore_family_night(driver):
    familynight = HomePage(driver)
    email, password = get_credentials()
    familynight.login_to_Kahoot(email, password)
    assert familynight.discover_channel()