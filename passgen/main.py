import string
import random
import pyperclip


def generate_password(length=8, digits=False, special=False):
    characters = string.ascii_letters
    password_list = random.choices(characters, k=length)
    if digits:
        password_list = insert_in_password(password_list, string.digits)
    if special:
        password_list = insert_in_password(password_list, string.punctuation)
    pyperclip.copy(''.join(password_list))
    return pyperclip.paste()


def insert_in_password(password_list, characters):
    result = password_list.copy()
    for _ in range(random.randint(1, len(result))) :
        result[random.randint(0, len(result) - 1)] = random.choice(characters)
    return result
