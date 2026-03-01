from src.pages.SignUp import SignUp

def test_naviagte_to_SignUpPage(driver):
    SignUpPage = SignUp(driver)
    assert SignUpPage.navigate_to_SignUpPage()

def test_duplicated_email(driver):
    SignUpPage = SignUp(driver)
    SignUpPage.navigate_to_SignUpPage()
    assert SignUpPage.duplicated_valid_user_input()

def test_signup_with_teacher_and_school_workspace(driver):
    SignUpPage = SignUp(driver)
    SignUpPage.navigate_to_SignUpPage()
    SignUpPage.signup_with_teacher_account_and_school_workspace()
    assert SignUpPage.enter_email_and_password()