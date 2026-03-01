import os
import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.contants import DEFAULT_TIMEOUT, SHORT_TIMEOUT, LONG_TIMEOUT,SCREENSHOTS_DIR

# ============================================
# WAIT HELPERS
# ============================================

def wait_for_element(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, locator)))

def wait_for_element_clickable(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by,locator)))

def wait_for_element_visible(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, locator)))

def is_element_present(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    try:
        wait_for_element(driver, locator, timeout, by)
        return True
    except TimeoutException:
        return False
    
# ============================================
# ELEMENT INTERACTION HELPERS
# ============================================

def click_element(driver, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
    element = wait_for_element_clickable(driver, locator, timeout, by)
    element.click()


def click_element_js(driver, locator, timeout=DEFAULT_TIMEOUT, by=By.XPATH):
    element = wait_for_element(driver, locator, timeout, by)
    scroll_to_element(driver, element)
    driver.execute_script("arguments[0].click();", element)

def send_keys_to_element(driver, locator, text, timeout = DEFAULT_TIMEOUT, by= By.XPATH, clear_first = True):
    element = wait_for_element_visible(driver, locator, timeout, by)
    if clear_first:
        element.clear()
    element.send_keys(text)

def get_element_text(driver, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
    element = wait_for_element_visible(driver,locator, timeout, by)
    return element.text

# ============================================
# SCREENSHOT HELPERS
# ============================================

def take_screenshot(driver, filename = None):
    # Create screenshots folder if not exist
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    # Create files if not exist
    if filename is None:
        filestamp = datetime.now().strftime("d/m/Y, H:MS")
        filename = f'screenshot_{filestamp}.png'

    # Make sure that extension.png exist
    if not filename.endswith('.png'):
        filename += '.png'
    
    # Full path
    filepath = os.path.join(SCREENSHOTS_DIR, filename)

    # Take screenshot
    driver.save_screenshot(filepath)
    return filepath

def take_screenshot_on_failure(driver, test_name):
    timestamp = datetime.now().strftime("d/m/Y, H:MS")
    filename = f'{test_name}_failure_{timestamp}.png'
    return take_screenshot(driver, filename)

# ============================================
# BROWSER HELPERS
# ============================================

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

def scroll_to_top(driver):
    driver.execute_script("window.scrollTo(0, 0);")

def switch_to_new_tab(driver):
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to.window(windows[-1])
    
def close_current_tab(driver):
    driver.close()
    windows = driver.window_handles
    if windows:
        driver.switch_to.window(windows[0])