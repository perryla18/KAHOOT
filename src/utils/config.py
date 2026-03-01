from src.utils.contants import (HEADLESS, BROWSER, DEFAULT_TIMEOUT, WINDOW_SIZE, IMPLICIT_WAIT)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import os

def get_browser_options():
    """
    Tạo và cấu hình browser options dựa trên BROWSER và HEADLESS constants
    
    Returns:
        options: Browser options object (ChromeOptions hoặc EdgeOptions)
    """
    if BROWSER.lower() == 'chrome':
        options = ChromeOptions()
        # headless mode
        if HEADLESS:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
        
        # window size
        if WINDOW_SIZE:
            options.add_argument(f'--window-size={WINDOW_SIZE}')
        else:
            options.add_argument('--start-maximized')
        
        return options
        
    elif BROWSER.lower() == 'edge':
        options = EdgeOptions()
        if HEADLESS:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
        
        # window size
        if WINDOW_SIZE:
            options.add_argument(f'--window-size={WINDOW_SIZE}')
        else:
            options.add_argument('--start-maximized')
        return options
    else:
        raise ValueError(f'browser {BROWSER} is not supported.')

def get_driver():
    options = get_browser_options()

    if BROWSER.lower() == 'chrome':
        driver_path = ChromeDriverManager().install()
        if 'THIRD_PARTY_NOTICES' in driver_path:
            driver_dir = os.path.dirname(driver_path)
            driver_path = os.path.join(driver_dir, 'chromedriver')
        # Cấp quyền thực thi nếu cần
        if os.path.exists(driver_path):
            os.chmod(driver_path, 0o755)
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=ChromeOptions)
    
    elif BROWSER.lower() == 'edge':
        service = EdgeService(driver_path)
        driver = webdriver.Edge(service=service, options=EdgeOptions)
    
    else:
        raise ValueError(f'Browser {BROWSER} is not supported')
    
    driver.implicitly_wait(IMPLICIT_WAIT)
    if not HEADLESS and not WINDOW_SIZE:
        driver.maximize_window()
    return driver

