import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.pages.Base_page import BasePage
from src.pages.login import LoginPage
from src.utils.credentials import get_credentials
from src.utils.contants import (
    LOGO, FAMILY_NIGHT_GAMES, FAMILY_NIGHT_DETAILS, FAMILY_NIGHT, EXIT_DETAIL,
    VIEW_OTHER_CHANNEL, GOOD_NEWS_CHANNEL, NEXT_OTHER_CHANNEL, PREVIOUS_BUTTON,
    NEXT_OTHER_CHANNEL_FALLBACK, PREVIOUS_BUTTON_FALLBACK,
    BACK_ICON, READ_MORE_OPTION, IPM_POPUP_CLOSE, POST_LOGIN_MODAL_CLOSE_CANDIDATES, LONG_TIMEOUT, SHORT_TIMEOUT, DEFAULT_TIMEOUT,
)

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_to_Kahoot(self, email=None, password=None):
        login = LoginPage(self.driver)
        login.navigate_to_loginpage()
        if email is None or password is None:
            email, password = get_credentials()
        return login.enter_user_password(email, password)

    def dismiss_post_login_modal_if_present(self):
        """Đóng mọi overlay/modal chặn màn hình sau khi đăng nhập (thường là IPM Kahoot!+).

        Flow (đọc từ trên xuống — mỗi bước *bổ sung*, không thay thế hẳn bước trước):

        1. **Chờ ngắn** rồi **JavaScript** click nhanh: thử `a[ipm-action="closeDialog"]` (popup marketing),
           nếu không có thì `#dialog__close-button` (nút X chuẩn của dialog Kahoot).

        2. **Vòng for**: lần lượt thử **nhiều xpath** (IPM chính + danh sách fallback trong constants).
           Mỗi cái được bọc `try/except`: *không có element* → bỏ qua, thử cái tiếp.
           Mục đích: Kahoot đổi DOM nhẹ; cùng một nút đóng có thể match xpath này nhưng không match xpath kia.

        3. **`EXIT_DETAIL`**: vẫn là nút đóng dialog (`#dialog__close-button`), nhưng xpath trỏ vào
           **icon bên trong** nút. Đôi khi overlay chỉ “ăn” click vào span con — nên thêm một
           cú click dự phòng *sau* vòng for (không trùng ý nghĩa với IPM vs EXIT — cả hai đều
           hướng tới “đóng thứ đang che màn hình”).

        4. **Escape × 2**: phím Escape đóng thêm một số layer/modal nếu còn sót.

        Tóm lại: không phải “chọn một trong hai giữa IPM và EXIT_DETAIL”, mà là **xếp chồng nhiều
        cách đóng** cho đến khi màn hình sạch overlay.
        """
        time.sleep(1.5)
        self.driver.execute_script(
            """
            var a = document.querySelector('a[ipm-action="closeDialog"]');
            if (a) { a.click(); return; }
            var b = document.querySelector('#dialog__close-button');
            if (b) { b.click(); }
            """
        )
        time.sleep(0.5)
        for xpath in (IPM_POPUP_CLOSE,) + POST_LOGIN_MODAL_CLOSE_CANDIDATES:
            try:
                self.click_js(xpath, timeout=SHORT_TIMEOUT)
                time.sleep(0.4)
            except TimeoutException:
                pass
        # Thử click icon X trong nút đóng dialog (đôi khi chỉ span mới nhận click).
        # Nếu vẫn còn modal: gửi Escape 2 lần (một số lớp chỉ đóng bằng phím).
        try:
            self.click_js(EXIT_DETAIL, timeout=SHORT_TIMEOUT)
            time.sleep(0.3)
        except TimeoutException:
            pass
        # Gửi phím Escape qua <body> (trang nhận phím tắt để đóng modal còn sót).
        # Lặp 2 lần: range(2). Biến _ = không dùng số đếm, chỉ cần thao tác lặp lại.
        body = self.driver.find_element(By.TAG_NAME, "body")
        """
        for _ in range(2): and for i in range(2): (or for banana in range(2):) 
            are the same behavior; only the name of the loop variable differs.
        range(2) gives two iterations (0 and 1 internally).
        Each time, the variable (_, i, …) would be 0 then 1, 
        but your code never uses that value — it only runs body.send_keys(Keys.ESCAPE) each time.
        """
        for _ in range(2):
            body.send_keys(Keys.ESCAPE)
            time.sleep(0.3)

    def discover_channel(self):
        self.dismiss_post_login_modal_if_present()
        if self.is_element_visible(FAMILY_NIGHT_GAMES):
            self.click(FAMILY_NIGHT_GAMES)
        self.is_element_visible(FAMILY_NIGHT)
        self.click(READ_MORE_OPTION)
        self.is_element_visible(FAMILY_NIGHT_DETAILS)
        self.click(EXIT_DETAIL)
        self.click(VIEW_OTHER_CHANNEL)
        self.is_element_visible(GOOD_NEWS_CHANNEL)
        last_err = None
        for xpath in (NEXT_OTHER_CHANNEL, NEXT_OTHER_CHANNEL_FALLBACK):
            try:
                self.click_js(xpath, timeout=DEFAULT_TIMEOUT)
                break
            except TimeoutException as e:
                last_err = e
        else:
            if last_err:
                raise last_err
        last_err = None
        for xpath in (PREVIOUS_BUTTON, PREVIOUS_BUTTON_FALLBACK):
            try:
                self.click_js(xpath, timeout=DEFAULT_TIMEOUT)
                break
            except TimeoutException as e:
                last_err = e
        else:
            if last_err:
                raise last_err
        self.click(VIEW_OTHER_CHANNEL)
        self.click(BACK_ICON)
        return self.is_element_visible(LOGO, timeout=LONG_TIMEOUT)
