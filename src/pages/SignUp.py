from src.pages.Base_page import BasePage
from src.utils.credentials import get_username, get_password, get_dulpicated_user
from src.utils.contants import (
    SIGNUP_URL, SIGNUP_BUTTON, EMAIL_SIGNUP_BOX, TEACHER_OPTION, SCHOOL_WORKSPACE,
    CONTINUE_BUTTON, CONFIRM_SIGNUP_OPTION, PASSWORD_SIGNUP_BOX, LOGO,
    PROFESSIONAL_OPTION, DUPLICATED_EMAIL_ERROR
)

class SignUp(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_SignUpPage(self):
        self.driver.get(SIGNUP_URL)
        self.accept_cookie_if_present()
        return self.is_element_visible("//div[@class='card__AuthCard-sc-1rk0phi-1 igttXZ']")

    def duplicated_valid_user_input(self):
        self.click(PROFESSIONAL_OPTION)
        self.send_keys(EMAIL_SIGNUP_BOX, get_dulpicated_user())
        self.click(CONFIRM_SIGNUP_OPTION)
        self.click(CONTINUE_BUTTON)
        return self.is_element_visible(DUPLICATED_EMAIL_ERROR)

# Teacher option
    def signup_with_teacher_account_and_school_workspace(self):
        self.click(TEACHER_OPTION)
        self.click(SCHOOL_WORKSPACE)

    def enter_email_and_password(self):
        self.send_keys(EMAIL_SIGNUP_BOX, 'abc23@gmail.com')
        self.click(CONFIRM_SIGNUP_OPTION)
        self.click(CONTINUE_BUTTON)
        self.send_keys(PASSWORD_SIGNUP_BOX, get_password())
        self.click_i_am_human_if_present()
        self.accept_cookie_if_present()
        self.click(SIGNUP_BUTTON)
        return self.is_element_visible(LOGO)


    



