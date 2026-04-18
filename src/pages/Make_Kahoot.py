import time

from src.pages.Base_page import BasePage
from src.pages.HomePage import HomePage
from src.pages.login import LoginPage
from src.utils.contants import (
    ANSWER_1,
    ANSWER_2,
    ANSWER_3,
    ANSWER_4,
    CLOSE_BUTTON,
    CONTINUE_KAHOOT_BUTTON,
    DONE_BUTTON,
    KAHOOT_CARD_BY_TITLE,
    KAHOOT_REMARKS,
    KAHOOT_TITLE,
    LONG_TIMEOUT,
    MAKE_ICON,
    MY_LIBRARY_KAHOOTS_ALL,
    QUESTION_TYPING,
    SAVE_BUTTON,
    SHORT_TIMEOUT,
    UPLOAD_FILE,
    KAHOOT_ACTIVIT_BUTTON,
    RECENT_TAP,
    DRAFT_TAP,
    DRAFT_LIST,
)
from src.utils.credentials import get_credentials
from src.utils.helpers import xpath_string_literal


class MakeKahoot(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def loginsuccess(self, email=None, password=None):
        login = LoginPage(self.driver)
        login.navigate_to_loginpage()
        if email is None or password is None:
            email, password = get_credentials()
        login.enter_user_password(email, password)
        time.sleep(1)
        HomePage(self.driver).dismiss_post_login_modal_if_present()

    def verify_kahoot_in_library(self, title: str, timeout=LONG_TIMEOUT) -> bool:
        """Kiểm tra kahoot vừa tạo có trong lưới thư viện (theo @title trên thẻ overlay)."""
        xpath = KAHOOT_CARD_BY_TITLE.format(xpath_title=xpath_string_literal(title))
        if self.is_element_visible(xpath, timeout=SHORT_TIMEOUT):
            return True
        self.driver.get(MY_LIBRARY_KAHOOTS_ALL)
        return self.is_element_visible(xpath, timeout=timeout)

    def make_kahoot(self, kahoot_title="Just a question"):
        """
        Tạo kahoot; title dùng cho assert — giữ một biến title, đừng lấy return từ send_keys (là None).
        """
        self.click(MAKE_ICON)
        self.click(CLOSE_BUTTON)
        self.click(UPLOAD_FILE)
        self.select_random_image()
        self.send_keys(QUESTION_TYPING, "What's this?")
        self.send_keys(ANSWER_1, "Option 1")
        self.send_keys(ANSWER_2, "Option 2")
        self.send_keys(ANSWER_3, "Option 3")
        self.send_keys(ANSWER_4, "Option 4")
        self.choose_the_correct_answer()
        self.click(SAVE_BUTTON)
        self.send_keys(KAHOOT_TITLE, kahoot_title)
        self.send_keys(
            KAHOOT_REMARKS,
            "Your mind is stronger than anything in the world, so please beleive in your self. Because in someday in the future, you'll realize that you'll always correct! Be your self, my sweetie <33 ",
        )
        self.click(CONTINUE_KAHOOT_BUTTON)
        self.click(DONE_BUTTON)
        return self.verify_kahoot_in_library(kahoot_title)
    
    def visit_your_kahoot(self):
        self.click(KAHOOT_ACTIVIT_BUTTON)
        self.click(RECENT_TAP)
        self.click(DRAFT_TAP)
        return self.is_element_visible(DRAFT_LIST)

