from src.pages.Make_Kahoot import MakeKahoot
from src.utils.credentials import get_credentials

def test_make_kahoot(driver):
    kahoot = MakeKahoot(driver)
    email, pasword = get_credentials()
    kahoot.loginsuccess(email, pasword)
    assert kahoot.make_kahoot("Nothingg")

def test_kahoot_activity(driver):
    library = MakeKahoot(driver)
    email, password = get_credentials()
    library.loginsuccess(email, password)
    assert library.visit_your_kahoot()