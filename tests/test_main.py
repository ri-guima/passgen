from passgen.main import generate_password
import pyperclip


def test_password():
    password = generate_password(15)
    assert len(password) == 15
    assert password == pyperclip.paste()


def test_password_with_digits():
    password = generate_password(digits=True)
    assert any([n in password for n in '0123456789'])


def test_password_with_special_characters():
    password = generate_password(special=True)
    assert any([n in password for n in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'])
