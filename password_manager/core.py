from utils.functions import *
from utils.crypto import Crypto
from utils.generator import Generator
from tabulate import tabulate

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

    data = (website, email, pair)

    if not save:
        print("Your new password for '%s' is: %s" % (website, password))
        return True

    return save_to_file(data)

def update(website):
    return

def delete(website):
    return

def save(website, email, password):

    website = sanitize_string(website)

    if not is_email_valid(email):
        return False

    c = Crypto()
    pair = c.encrypt(password)

    data = (website, email, pair)

    return save_to_file(data)

def fetch(website):
    filename = "data.txt"
    c = Crypto()

    website = sanitize_string(website)

    result = []

    with open(filename, 'r') as f:
        for line in f:
            l = line.split()

            if l[0] == website:
                result.append(l)
        
    f.close()

    return result

#print(save("orange", "matthias.brown@gmail.com", "123456789"))
#print(fetch("microsoft"))
#generate("microsoft", "matthias.brown@gmail.com", 64)