from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from src.utils.helpers import (
    wait_for_element,
    is_element_present,
    click_element,
    click_element_js,
    send_keys_to_element,
    take_screenshot,
)
from src.utils.contants import DEFAULT_TIMEOUT, ONETRUST_ACCEPT, SHORT_TIMEOUT, I_AM_HUMAN_IFRAME, I_AM_HUMAN


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=DEFAULT_TIMEOUT, by=By.XPATH):
        return wait_for_element(self.driver, locator, timeout, by)
    
    def click(self, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
        return click_element(self.driver, locator, timeout, by)

    def click_js(self, locator, timeout=DEFAULT_TIMEOUT, by=By.XPATH):
        return click_element_js(self.driver, locator, timeout, by)

    def send_keys(self, locator, text, timeout = DEFAULT_TIMEOUT, by=By.XPATH, clear_first=True):
        return send_keys_to_element(self.driver, locator, text, timeout, by, clear_first)
    
    def is_element_visible(self, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
        return is_element_present(self.driver, locator, timeout, by)

    def accept_cookie_if_present(self):
        try:
            self.click(ONETRUST_ACCEPT, timeout=SHORT_TIMEOUT)
        except TimeoutException:
            pass

    def click_i_am_human_if_present(self):
        try:
            iframe = wait_for_element(self.driver, I_AM_HUMAN_IFRAME, SHORT_TIMEOUT, By.XPATH)
            self.driver.switch_to.frame(iframe)
            try:
                wait_for_element(self.driver, I_AM_HUMAN, SHORT_TIMEOUT, By.XPATH).click()
            finally:
                self.driver.switch_to.default_content()
        except TimeoutException:
            pass

    def take_screenshot(self, filename=None):
        return take_screenshot(self.driver, filename)
