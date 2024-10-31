def validate_password(password: str) -> bool:
    is_valid = True
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        is_valid = False
    if password == password.lower():
        print("Password must contain at least one upper case")
        is_valid = False
    return is_valid


def validate_phone_number(phone_number: str) -> bool:
    if len(phone_number) != 13:
        return False
    elif not phone_number.startswith("+998"):
        return False
    elif phone_number[4:6] not in ["90", "91", "50", "55", "95", "99", "93","94"]:
        return False
    elif not phone_number[6:].isdigit():
        return False
    return True
