from src.pages.Base_page import BasePage
from src.utils.credentials import get_credentials, get_invalid_credentials
from src.utils.contants import (
    LOGIN_BUTTON, LOGIN_PASSWORD_BOX, LOGIN_SUBMIT_BUTTON, LOGIN_USERNAME_BOX,
    BASE_URL, LOGO, LONG_TIMEOUT, LOGIN_ERROR
)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_loginpage(self):
        self.driver.get(BASE_URL)
        self.accept_cookie_if_present()
        self.click(LOGIN_BUTTON)
    
    def enter_user_password(self, email = None, password = None):
        if email is None or password is None:
            email, password = get_credentials()
        self.accept_cookie_if_present()
        self.send_keys(LOGIN_USERNAME_BOX, email)
        self.send_keys(LOGIN_PASSWORD_BOX, password)
        self.accept_cookie_if_present()
        self.click_js(LOGIN_SUBMIT_BUTTON)
        return self.is_element_visible(LOGO, timeout=LONG_TIMEOUT)
    
    def enter_invalid_user(self, email = None, password = None):
        if email is None or password is None:
            email, password = get_invalid_credentials()
        self.send_keys(LOGIN_USERNAME_BOX, email)
        self.send_keys(LOGIN_PASSWORD_BOX, password)
        self.accept_cookie_if_present()
        self.click(LOGIN_SUBMIT_BUTTON)
        return self.is_element_visible(LOGIN_ERROR)