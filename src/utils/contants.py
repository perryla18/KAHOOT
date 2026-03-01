# URL CONTANT
BASE_URL = "https://kahoot.com/"
LOGIN_URL = "https://create.kahoot.it/auth/login"
SIGNUP_URL = "https://create.kahoot.it/auth/register"

# TIMEOUT CONTANTS
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 5
LONG_TIMEOUT = 30
IMPLICIT_WAIT = 10
EXPLICITAIT = 20

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
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"

# SIGNUP
# TEACHER
TEACHER_OPTION = "//span[normalize-space()='Teacher']"
SCHOOL_WORKSPACE = "//span[normalize-space()='School']"
HIGHER_EDUCATION = "//span[normalize-space()='Higher education']"
SCHOOL_ADMINISTRATION = "//span[normalize-space()='School administration']"
BUSINESS_WORKSPACE = "//span[normalize-space()='Business']"
OTHER_WORKSPACE = "//span[normalize-space()='Other']"
PROFESSIONAL_OPTION = "//span[normalize-space()='Professional']"
# STUDENT
STUDENT_OPTION = "//span[normalize-space()='Student']"
DAY = "//select[@id='day']"
MONTH = "//select[@id='month']"
YEAR = "//select[@id='year']"
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
CHECKMARK = "//div[@id='anchor-tc']"
SIGNUP_BUTTON = "//button[normalize-space()='Sign up']"

# LOGIN PAGE
LOGIN_BUTTON = "//a[@href='https://create.kahoot.it/']//span[@class='menu-item-text'][normalize-space()='Log in']"
LOGIN_USERNAME_OX = "//input[@id='username']"
LOGIN_PASSWORD_BOX = "//input[@id='password']"
LOGIN_SUBMIT_BUTTON = "//button[@id='login-submit-btn']"

# HOMEPAGE
LOGO = "//span[@title='Kahoot! logo']"
SETTING_ICON = "//a[@aria-label='Settings']//span[@class='icon__Icon-sc-xvsbpg-0 exxNNM']"
SIGNOUT_BUTTON = "//button[normalize-space()='Sign out']"
