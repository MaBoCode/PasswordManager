from tabulate import tabulate
import re, string

def generate(website, email, length, save = True):
    """
    check website, email
    generate a new password, encrypt it
    """

    website = sanitize_string(website)
    print(website)

    if not is_email_valid(email):
        return False

    return True

generate("fzef", "zef", 15)

def update(website):
    return

def delete(website):
    return

def save(website, email, password):
    return

def fetch(website):
    return

def sanitize_string(s):
    unwanted_chars = string.punctuation
    s.strip()
    for c in unwanted_chars:
        s = s.replace(c, '')
    return s

def is_email_valid(email):
    email_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    return re.fullmatch(email_regex, email)