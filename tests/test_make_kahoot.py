from src.pages.Make_Kahoot import MakeKahoot
from src.utils.credentials import get_credentials

def test_make_kahoot(driver):
    kahoot = MakeKahoot(driver)
    email, pasword = get_credentials()
    kahoot.loginsuccess(email, pasword)
    assert kahoot.make_kahoot("Nothing")