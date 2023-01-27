import os
import pyperclip


def test_password():
    os.system('python passgen/cli.py -l 15')
    assert len(pyperclip.paste()) == 15
    os.system('python passgen/cli.py -l 10')
    assert len(pyperclip.paste()) == 10


def test_password_with_digits():
    os.system('python passgen/cli.py -d')
    assert any([n in pyperclip.paste() for n in '0123456789'])


def test_password_with_special_characters():
    os.system('python passgen/cli.py -s')
    assert any([n in pyperclip.paste() for n in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'])
