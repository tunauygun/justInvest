import os
import csv
import base64

from cryptography.exceptions import InvalidSignature, InvalidKey
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from helpers import *
from role import Role
from user_type import UserType
from user import User


# Password File Format:
# username,roles,hash,salt

def register_and_login():
    selected_option = get_input_from_options(["Login", "Register", "Exit"])
    if selected_option == 3:
        print(("\n" * 40) + "EXITING...")
        exit(0)
    elif selected_option == 2:
        return _registration_menu()
    else:
        return _login_menu()


def _registration_menu():
    _register_new_user()
    input("Registration Successful. Press enter to go to login page...")
    clear_page()
    return _login_menu()


def _login_menu():
    return _login_user()


def _login_user():
    while True:
        print()
        username_input = input("Username: ").strip()
        if username_input == "":
            print("Username cannot be empty")
            continue

        password = input("Password: ")
        username, roles, hash, salt = _get_user_from_password_file(username_input)
        if username is None:
            print("Incorrect username or password!")
        else:
            is_password_correct = _is_password_correct(password, hash, salt)
            if not is_password_correct:
                print("Incorrect username or password!")
            else:
                return User(username, [Role.get_enum_from_name(role_name) for role_name in roles])


def _register_new_user():
    username, password = _get_username_password()
    user_type = _get_user_type()
    roles = '-'.join([r.get_name() for r in user_type.get_roles()])
    _add_user_to_password_file(username, roles, password)


def _is_password_correct(password, hash, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
    )
    try:
        kdf.verify(password.encode('utf-8'), hash)
        return True
    except InvalidKey:
        return False


def _get_user_from_password_file(target_username):
    with open('passwd.txt', mode='r') as password_file:
        file_reader = csv.reader(password_file, delimiter=',')
        for user in file_reader:
            if len(user) == 0:
                continue
            username = user[0]
            if username == target_username:
                roles = user[1].split('-')
                hash = user[2]
                salt = user[3]
                return username, roles, base64.b64decode(hash), base64.b64decode(salt)
        return None, None, None, None


def _add_user_to_password_file(username, roles, password):
    hash, salt = _hash_with_salt(password)
    with open('passwd.txt', mode='a', newline="") as password_file:
        if _check_for_existing_user(username):
            return False
        file_writer = csv.writer(password_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([username, roles, base64.b64encode(hash).decode(), base64.b64encode(salt).decode()])
        return True


def _hash_with_salt(password):
    salt = os.urandom(16)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
    )
    hash = kdf.derive(password.encode('utf-8'))
    return hash, salt


def _check_for_existing_user(target_username):
    with open('passwd.txt', mode='r') as password_file:
        file_reader = csv.reader(password_file, delimiter=',')
        for user in file_reader:
            if len(user) == 0:
                continue
            username = user[0]
            if username == target_username:
                return True
        return False


def _is_valid_password(username, password):
    if username == password:
        return False, "Your password cannot be same as your username!"

    if _is_weak_password(password):
        return False, "Your password is too weak!"

    password_length = len(password)
    if password_length < 8 or password_length > 12:
        return False, "Your password must be 8-12 characters long!"

    if not any(c.islower() for c in password):
        return False, "Your password must contain at least one lowercase letter!"

    if not any(c.isupper() for c in password):
        return False, "Your password must contain at least one uppercase letter!"

    if not any(c.isdigit() for c in password):
        return False, "Your password must contain at least one number!"

    special_characters = ['!', '@', '#', '$', '%', '*', '&']
    if not any(c in special_characters for c in password):
        return False, "Your password must contain at least one of [!, @, #, $, %, *, &]"

    return True, None


def _is_weak_password(password):
    with open('weak_passwords.txt', mode='r', encoding='utf-8') as weak_password_file:
        for weak_password in weak_password_file:
            if weak_password.strip() == password:
                return True
        return False


def _get_username_password():
    user_already_exists = True
    while user_already_exists:
        print()
        username = input("Username: ").strip()
        if username == "":
            print("Username cannot be empty")
        else:
            user_already_exists = _check_for_existing_user(username)
            if user_already_exists:
                print("Username already exists! Select a different username.")
    while True:
        password = input("Password: ").strip()
        is_valid_password, error_message = _is_valid_password(username, password)
        if not is_valid_password:
            print(error_message)
        else:
            return username, password


def _get_user_type():
    return get_enum_selection(UserType, "Select a user type: ")
