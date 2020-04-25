# Author: Kyungho Lim
# Contact: kyungho.lim@gmail.com

import string
# import re

special_character = "!@#$%^&*()-_+="
def check_password():
    global special_character
    password = input("Enter your password: ")
    print(set(password))
    if len(password) == 0:
        print('Please enter your password.')
        password_again()
    elif len(password) < 8:
        print('Password must have at least eight characters.')
        password_again()
    elif not any(i in string.digits for i in password):
    # elif re.search('[0-9]', password) is None:
        print('Password must contain at least one number.')
        password_again()
    elif not any(i in string.ascii_letters for i in password):
        print('Password must contain at least one letter.')
        password_again()
    elif not any(i in string.ascii_lowercase for i in password):
    # elif re.search('[a-z]', password) is None:
        print('Password must contain at least one lowercase letter.')
        password_again()
    elif not any(i in string.ascii_uppercase for i in password):
    # elif re.search('[A-Z]', password) is None:
        print('Password must contain at least one uppercase letter.')
        password_again()
    elif not any(i in special_character for i in password):
        print('Password must contain at least one special character.')
        password_again()
    elif any(i in string.whitespace for i in password):
        print('Password do not allow any space among characters.')
        password_again()
    else:
        print('Your password is valid')

    # try:
    #     assert any(i in string.ascii_letters for i in password)
    #     assert any(i in string.ascii_lowercase for i in password)
    #     assert any(i in string.ascii_uppercase for i in password)
    #     assert any(i in string.digits for i in password)
    #     assert any(i in string.whitespace for i in password)
    # except AssertionError as e:
    #     raise Exception('Invalid password!')


def password_again():
    check_password()

check_password()