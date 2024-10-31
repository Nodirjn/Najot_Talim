from datetime import datetime
import hashlib
from typing import Union

from file_manager import users_manager


class Users:
    def __init__(self, full_name, phone_number, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.password = hash_password(password)
        self.is_active = False
        self.created_at = datetime.now()

    def get_object_as_list(self):
        return [self.full_name, self.phone_number, self.password, self.created_at, self.is_active]


def hash_password(password) -> str:
    """hash the given password with sha256 algorithm"""
    return hashlib.sha256(string=password.encode()).hexdigest()


def get_user_by_phone(phone_number: str) -> Union[str, bool]:
    """get user by phone number from users.csv file"""

    users = users_manager.read()
    for user in users[1:]:
        if user[1] == phone_number:
            return user
    return False


def get_active_user() -> Union[bool, list]:
    """get user by it is status that is active """
    users = users_manager.read()
    for user in users:
        if user[-1]:
            return user
    return False
