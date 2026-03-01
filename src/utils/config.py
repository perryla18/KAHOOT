import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.utils.contants import (
    HEADLESS,
    BROWSER,
    WINDOW_SIZE,
    IMPLICIT_WAIT,
)


def get_chromedriver_path():
    """
    Lấy đường dẫn đúng tới file thực thi chromedriver.
    Webdriver-manager đôi khi trả về file THIRD_PARTY_NOTICES.chromedriver (file text)
    thay vì file chromedriver (binary). Hàm này sửa lại đường dẫn cho đúng.
    """
    path = ChromeDriverManager().install()
    if not path:
        return path
    folder = os.path.dirname(path)
    name = os.path.basename(path)
    if name != "chromedriver":
        path = os.path.join(folder, "chromedriver")
    if os.path.exists(path):
        os.chmod(path, 0o755)
    return path


def get_edgedriver_path():
    """Lấy đường dẫn đúng tới file thực thi msedgedriver (tương tự Chrome)."""
    path = EdgeChromiumDriverManager().install()
    if not path:
        return path
    folder = os.path.dirname(path)
    name = os.path.basename(path)
    if name != "msedgedriver":
        path = os.path.join(folder, "msedgedriver")
    if os.path.exists(path):
        os.chmod(path, 0o755)
    return path


def get_browser_options():
    """
    Tạo và cấu hình browser options (cửa sổ, headless, ...) theo BROWSER và HEADLESS.
    Returns:
        options: ChromeOptions hoặc EdgeOptions đã cấu hình.
    """
    if BROWSER.lower() == "chrome":
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
        if WINDOW_SIZE:
            options.add_argument(f"--window-size={WINDOW_SIZE}")
        else:
            options.add_argument("--start-maximized")
        return options

    if BROWSER.lower() == "edge":
        options = EdgeOptions()
        if HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
        if WINDOW_SIZE:
            options.add_argument(f"--window-size={WINDOW_SIZE}")
        else:
            options.add_argument("--start-maximized")
        return options

    raise ValueError(f"Browser '{BROWSER}' chưa được hỗ trợ. Dùng 'chrome' hoặc 'edge'.")


def get_driver():
    """
    Tạo WebDriver theo cấu hình trong contants.py (BROWSER, HEADLESS, WINDOW_SIZE).
    Dùng trong test: fixture gọi get_driver() rồi yield driver, cuối test driver.quit().
    """
    options = get_browser_options()

    if BROWSER.lower() == "chrome":
        driver_path = get_chromedriver_path()
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
    elif BROWSER.lower() == "edge":
        driver_path = get_edgedriver_path()
        service = EdgeService(driver_path)
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Browser '{BROWSER}' chưa được hỗ trợ.")

    driver.implicitly_wait(IMPLICIT_WAIT)
    if not HEADLESS and not WINDOW_SIZE:
        driver.maximize_window()
    return driver
