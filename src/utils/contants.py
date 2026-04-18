# URL CONTANT
BASE_URL = "https://kahoot.com/"
LOGIN_URL = "https://create.kahoot.it/auth/login"
SIGNUP_URL = "https://create.kahoot.it/auth/register"

# TIMEOUT CONTANTS
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 5
LONG_TIMEOUT = 30
IMPLICIT_WAIT = 10

# BROWSER CONTANTS
HEADLESS = False
BROWSER = 'chrome'
WINDOW_SIZE = "1920,1080"
SCREENSHOT_PATH = 'screenshots/'

# FILE PATHS
REPORTS_DIR = "reports/"
SCREENSHOTS_DIR = "screenshots/"
TEST_DATA_DIR = "src/fixtures/"

# TEST DATA CONTANTS
# Note: Real credentials should be in .env file
# These are fallback values only - use credentials.py for real values
VALID_USERNAME = "test_user"        # ✅ TEST value (mẫu)
VALID_PASSWORD = "test_password"    # ✅ TEST value (mẫu)
DUPLICATED_VALID_USER = "test_duplicated"
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"
USERNAME = 'username'

# SIGNUP
# TEACHER
TEACHER_OPTION = "//span[normalize-space()='Teacher']"
SCHOOL_WORKSPACE = "//span[normalize-space()='School']"
HIGHER_EDUCATION = "//span[normalize-space()='Higher education']"
SCHOOL_ADMINISTRATION = "//span[normalize-space()='School administration']"
BUSINESS_WORKSPACE = "//span[normalize-space()='Business']"
OTHER_WORKSPACE = "//span[normalize-space()='Other']"
#Professional
PROFESSIONAL_OPTION = "//span[normalize-space()='Professional']"
# STUDENT
STUDENT_OPTION = "//span[normalize-space()='Student']"
USERNAME_BOX = "//input[@id='username']"
DAY = "//select[@id='day']"
MONTH = "//select[@id='month']"
YEAR = "//select[@id='year']"
AGE_TEXT = "//form/p[1]" 
CONTINUE_BUTTON = "//button[@type='submit']"
# FAMILY AND FRIENDS
FAMILY_FRIEND_OPTIONS = "//span[normalize-space()='Family and friends']"
YOUR_FRIENDS_AND_FAMILY = "//span[normalize-space()='Your friends and family']"
YOUR_CHILDRENS = "//span[normalize-space()='Your children']"
YOUR_COLLEAGUES_OR_CLIENTS = "//span[normalize-space()='Your colleagues or clients']"
YOUR_STUDENTS = "//span[normalize-space()='Your students']"
OTHER = "//span[normalize-space()='Other']"
# EMAIL
EMAIL_SIGNUP_BOX = "//input[@id='email']"
CONFIRM_SIGNUP_OPTION = "//button[@id='marketingconsent']"
SUBMIT_SIGNUP = "//button[normalize-space()='Continue']"
DUPLICATED_EMAIL_ERROR = "//span[@id='email_error']"
PASSWORD_SIGNUP_BOX = "//input[@id='password']"
I_AM_HUMAN_IFRAME = "//form//iframe"
I_AM_HUMAN = "//*[@id='checkbox']"
SIGNUP_BUTTON = "//button[normalize-space()='Sign up']"
ONETRUST_ACCEPT = "//button[@id='onetrust-accept-btn-handler']"

# LOGIN PAGE
LOGIN_BUTTON = "//a[@href='https://create.kahoot.it/after/login']//span[@class='menu-item-text'][normalize-space()='Log in']"
LOGIN_USERNAME_BOX = "//input[@id='username']"
LOGIN_PASSWORD_BOX = "//input[@id='password']"
LOGIN_SUBMIT_BUTTON = "//button[@id='login-submit-btn']"
LOGIN_ERROR = "//span[@role='alert']"

# HOMEPAGE — popup Kahoot!+ (IPM): nút × đóng
IPM_POPUP_CLOSE = "//a[@ipm-action='closeDialog' and contains(@class,'close-button')]"
# Các selector khác (fallback)
POST_LOGIN_MODAL_CLOSE_CANDIDATES = (
    "//a[@ipm-action='closeDialog']",
    "//button[@id='dialog__close-button']",
    "//button[@id='dialog__close-button']//span[contains(@class,'icon')]",
    "//div[@role='dialog']//button[@id='dialog__close-button']",
    "//button[contains(@data-functional-selector,'close')]",
    "//button[contains(normalize-space(),'Skip') or contains(normalize-space(),'Not now')]",
)
LOGO = "//span[@title='Kahoot! logo']"
SETTING_ICON = "//a[@aria-label='Settings']//span[@class='icon__Icon-sc-xvsbpg-0 exxNNM']"
SIGNOUT_BUTTON = "//button[normalize-space()='Sign out']"

FAMILY_NIGHT_GAMES = "//div[@aria-label='Family night games']"
FAMILY_NIGHT = "//span[normalize-space()='Family Night!']"
READ_MORE_OPTION = "//button[normalize-space()='Read more']"
FAMILY_NIGHT_DETAILS = "//body"
EXIT_DETAIL = "//button[@id='dialog__close-button']//span[@class='icon__Icon-sc-xvsbpg-0 exxNNM']"
VIEW_OTHER_CHANNEL = "//span[normalize-space()='View other channels']"
GOOD_NEWS_CHANNEL = "//a[@aria-label='Good News of the Week by Kahoot! by KahootStudio']"
# Carousel next/prev — ưu tiên flickity (ổn định hơn class hash cũ)
NEXT_OTHER_CHANNEL = "//button[contains(@class,'flickity-prev-next-button') and contains(@class,'next')]"
PREVIOUS_BUTTON = "//button[contains(@class,'flickity-prev-next-button') and contains(@class,'previous')]"
NEXT_OTHER_CHANNEL_FALLBACK = "//div[contains(@class,'styles__Header')]//li[2]//button[1]"
PREVIOUS_BUTTON_FALLBACK = "//div[contains(@class,'styles__Header')]//li[1]//button[1]//span[2]"
BACK_ICON = "//button[@aria-label='Back']//span[@class='icon__Icon-sc-xvsbpg-0 exxNNM']"

"""
MAKE KAHOOT
"""
MAKE_ICON = "//a[@href='/creator']//h3[text()='Make']/ancestor::a"
CLOSE_BUTTON = "//button[normalize-space()='Close']"
UPLOAD_FILE = "//div[@aria-label='Add image or youtube video to the current question.']"
ALL_LIST_IMAGES = "//button[@data-functional-selector='media-library-dialog__image-grid__image']"
QUESTION_TYPING= "//p[@data-placeholder='Start typing your question']"
ANSWER_1 = "//div[@id='question-choice-0']"
ANSWER_2 = "//div[@id='question-choice-1']"
ANSWER_3 = "//div[@id='question-choice-2']"
ANSWER_4 = "//div[@id='question-choice-3']"
SAVE_BUTTON = "//button[normalize-space()='Save']"
CORRECT_BUTTON = "//button[@data-functional-selector='question-answer__toggle-button']"
KAHOOT_TITLE = "//input[@id='kahoot-title']"
KAHOOT_REMARKS = "//textarea[@id='description']"
CONTINUE_KAHOOT_BUTTON = "//button[normalize-space()='Continue']"
DONE_BUTTON = "//button[normalize-space()='Done']"
# Thư viện kahoot — sau khi tạo xong có thể cần mở /my-library/kahoots/all
MY_LIBRARY_KAHOOTS_ALL = "https://create.kahoot.it/my-library/kahoots/all"
# {xpath_title} = helpers.xpath_string_literal(title) — khớp overlay link theo @title
KAHOOT_CARD_BY_TITLE = (
    "//div[contains(@class,'kahoots-list__Content')]"
    "//a[contains(@data-testid,'clickable-overlay') and @title={xpath_title}]"
)
KAHOOT_ACTIVIT_BUTTON = "//a[@aria-label='View all your kahoots']"
RECENT_TAP = "//button[@id='recent-tab']"
DRAFT_TAP = "//button[@id='drafts-tab']"
DRAFT_LIST = "/html/body/div[1]/div/div/div/div[2]/main/div[2]/div/div[3]/div[3]"

FAVORITE_TAP = "//button[@id='favorites-tab']"
SHARED_WITH_YOU_TAB = "//button[@id='shared-tab']"

DISCOVERY_BUTTON = "//a[contains(@href,'/discover')]//h3[normalize-space()='Discover']/ancestor::a"
# “View all” tới partner collections — thử lần lượt (locale / DOM khác nhau). Không bắt span "View all" (có thể đổi ngôn ngữ).
PARTNER_COLLECTIONS_PAGE = "https://create.kahoot.it/page/en/partner-collections-social"
VIEW_ALL_LOCATORS = (
    "//a[contains(@href,'partner-collections')]",
    "//a[contains(@aria-label,'Partner collections')]",
    "//a[contains(@aria-label,'View all content')]",
)
VIEW_ALL = VIEW_ALL_LOCATORS[0]
# Partner card — không bọc trong <li> trên layout mới; thử Lego trước rồi card đầu tiên
_AL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_al = "abcdefghijklmnopqrstuvwxyz"
LOGO_FOUNDATION = (
    f"//a[contains(@data-testid,'image-card-overlay')]"
    f"[contains(translate(@aria-label, '{_AL}', '{_al}'), 'lego') "
    f"or contains(translate(@title, '{_AL}', '{_al}'), 'lego')]"
)
LOGO_FOUNDATION_FALLBACK = "//a[contains(@data-testid,'image-card-overlay')]"
# DOM đổi: thẻ overlay / link partner không còn testid cũ
LOGO_FOUNDATION_FALLBACK2 = "//a[contains(@class,'ClickableOverlay')]"
LOGO_FOUNDATION_FALLBACK3 = "//a[contains(@href,'lego') or contains(@href,'LEGO')]"
FOUNDATION_MESSAGE = "//h2[contains(.,'Lego') or contains(.,'LEGO')]"