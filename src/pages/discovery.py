import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from src.pages.Base_page import BasePage
from src.pages.HomePage import HomePage
from src.pages.login import LoginPage
from src.utils.contants import (
    DISCOVERY_BUTTON,
    FOUNDATION_MESSAGE,
    LOGO_FOUNDATION,
    LOGO_FOUNDATION_FALLBACK,
    LOGO_FOUNDATION_FALLBACK2,
    LOGO_FOUNDATION_FALLBACK3,
    LONG_TIMEOUT,
    PARTNER_COLLECTIONS_PAGE,
    SHORT_TIMEOUT,
    VIEW_ALL_LOCATORS,
)
from src.utils.credentials import get_credentials
from src.utils.helpers import switch_to_new_tab


class Discovery(BasePage):
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

    def _click_view_all(self):
        """Mở Partner collections: thử xpath; nếu không có link (lazy / locale), mở thẳng URL."""
        for xpath in VIEW_ALL_LOCATORS:
            try:
                el = self.find_element(xpath, timeout=LONG_TIMEOUT)
                self.scroll_to_element(el)
                self.click_js(xpath, timeout=LONG_TIMEOUT)
                return
            except TimeoutException:
                continue
        self.driver.get(PARTNER_COLLECTIONS_PAGE)
        time.sleep(2)

    def _find_foundation_card(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        for xpath, timeout in (
            (LOGO_FOUNDATION, SHORT_TIMEOUT),
            (LOGO_FOUNDATION_FALLBACK, LONG_TIMEOUT),
            (LOGO_FOUNDATION_FALLBACK2, SHORT_TIMEOUT),
            (LOGO_FOUNDATION_FALLBACK3, SHORT_TIMEOUT),
        ):
            try:
                return self.find_element(xpath, timeout=timeout)
            except TimeoutException:
                continue
        try:
            els = self.driver.find_elements(By.CSS_SELECTOR, "a[data-testid*='image-card']")
            if els:
                return els[0]
        except Exception:
            pass
        raise TimeoutException(
            "Không thấy thẻ partner — kiểm tra đăng nhập create.kahoot.it và DOM mới."
        )

    def navigate_to_discovery(self):
        self.click(DISCOVERY_BUTTON, timeout=LONG_TIMEOUT)
        time.sleep(2)
        if len(self.driver.window_handles) > 1:
            switch_to_new_tab(self.driver)
            time.sleep(1.5)
        self._click_view_all()
        self.driver.execute_script("window.scrollTo(0, Math.max(document.body.scrollHeight, 800) / 2);")
        time.sleep(1)
        foundation = self._find_foundation_card()
        self.scroll_to_element(foundation)
        self.driver.execute_script("arguments[0].click();", foundation)
        return self.is_element_visible(FOUNDATION_MESSAGE, timeout=LONG_TIMEOUT)
