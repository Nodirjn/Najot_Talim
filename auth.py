from typing import Union

from utils import validate_password, validate_phone_number
from users import Users, hash_password, get_user_by_phone
from file_manager import users_manager


def update_is_active(employees, employee) -> bool:
    """update given user status to True"""
    index = 1
    while index < len(employees):
        if employees[index][1] == employee[1]:
            employees[index][-1] = True
            break
        index += 1
    users_manager.write(data=employees)
    return True


def check_user(phone, password) -> Union[str, bool]:
    """check user from database and update status, else return False"""

    users = users_manager.read()
    for user in users:
        hashed_password = hash_password(password)
        if user[1] == phone and user[2] == hashed_password:
            if update_is_active(users, user):
                return user
            return False
    return False


def login() -> Union[str, bool]:
    """search user from database and return user type"""

    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")

    result = check_user(phone, password)
    if result:
        return result
    return False


def logout():
    employees = users_manager.read()
    index = 1
    while index < len(employees):
        employees[index][-1] = False
        index += 1
    users_manager.write(data=employees)


def get_active_user():
    users = users_manager.read()
    for user in users[1:]:
        if user[-1]:
            return user
    return False


def register() -> Union[bool]:
    """register user with full_name, password and phone number"""

    try:
        full_name: str = input("Enter your full name: ")
        phone: str = input("Enter your phone number: ").strip()
        if not validate_phone_number(phone_number=phone):
            print("Invalid phone number")
            return register()

        if get_user_by_phone(phone_number=phone):
            print("User with this phone number is already exists")
            return register()

        password: str = input("Enter your password: ")
        confirm_password: str = input("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match")
            return register()

        if not validate_password(password):
            return register()

        user = Users(full_name=full_name, phone_number=phone, password=password)
        users_manager.append(row=user.get_object_as_list())
        return True
    except Exception as e:
        print(e)
        return False
