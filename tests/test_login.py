import pytest
from src.pages.login import LoginPage
from src.utils.credentials import get_credentials, get_invalid_credentials

def test_login(driver):
    login = LoginPage(driver)
    login.navigate_to_loginpage()
    email, password = get_credentials()
    assert login.enter_user_password(email, password)

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.navigate_to_loginpage()
    email, password = get_invalid_credentials()
    assert login.enter_invalid_user(email, password)