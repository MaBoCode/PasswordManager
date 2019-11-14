from .utils.functions import *
from .utils.crypto import Crypto
from .utils.generator import Generator

def generate(website, email, length = 16, save = True):
    """
    check website, email
    generate a new password, encrypt it
    """

    website = sanitize_string(website)

    if not is_email_valid(email):
        return False

    g = Generator()
    password = g.generate(length)

    if not password:
        display_msg("Error", "Couldn't generate password.")
        return False
    
    c = Crypto()
    pair = c.encrypt(password)

    data = (website, email, password)

    if save:
        save_to_file(data)

    return True

def update(website):
    return

def delete(website):
    return

def save(website, email, password):
    return

def fetch(website):
    return

generate("hi", "hi")