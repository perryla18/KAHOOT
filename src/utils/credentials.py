import os
from dotenv import load_dotenv
from src.utils.contants import VALID_PASSWORD, VALID_USERNAME, INVALID_PASSWORD, INVALID_USERNAME, DUPLICATED_VALID_USER, USERNAME

load_dotenv()

def get_username():
    return os.getenv('USERNAME', USERNAME)

def get_email():
    return os.getenv('VALID_USERNAME', VALID_USERNAME)

def get_password():
    return os.getenv('VALID_PASSWORD', VALID_PASSWORD)

def get_dulpicated_user():
    return os.getenv('DUPLICATED_VALID_USERNAME', DUPLICATED_VALID_USER)

def get_credentials():
    return (get_email(), get_password())

def get_invalid_username():
    return os.getenv('INVALID_USERNAME', INVALID_USERNAME)

def get_invalid_password():
    return os.getenv('INVALID_PASSWORD', INVALID_PASSWORD)

def get_invalid_credentials():
    return (get_invalid_username(), get_invalid_password())

