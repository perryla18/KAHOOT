import os
import pytest
from dotenv import load_dotenv

from src.utils.config import get_driver
from src.utils.contants import BASE_URL

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """URL gốc cho test; ưu tiên lấy từ .env nếu có."""
    return os.getenv("BASE_URL") or BASE_URL


@pytest.fixture(scope="function")
def driver():
    """Tạo WebDriver một lần cho mỗi test; đóng driver khi test xong."""
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def browser(driver, base_url):
    """Driver đã mở sẵn trang base_url (tiện cho test navigation)."""
    driver.get(base_url)
    return driver
