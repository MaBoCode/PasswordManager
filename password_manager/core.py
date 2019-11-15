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

def update(website, email = None, password = None):
    change_password, change_email = False, False

    if not website:
        return False

    website = sanitize_string(website)
    results = fetch(website)

    if len(results) > 0:

        if email and not is_email_valid(email):
            display_msg("Error", "Invalid email.")
            return False

        if password and len(password) < 16:
            display_msg("Error", "Password too short (> 15).")
            return False

        display_data(results, ["N°", "Website", "Email", "Key", "Password"])

        entry_num = int(handle_user_input("Which entry you want to change? [enter n°]: "))

        num_list = []
        for row in results:
            num_list.append(row[0])
        
        if entry_num not in num_list:
            display_msg("Error", "Entry not in list.")
            return False

        if not password:
            res = handle_user_input("Generate a new password ? [y/n]: ")

            if res.lower() == 'y':
                length = handle_user_input("Password length (> 15): ")
                
                g = Generator()
                password = g.generate() if not length else g.generate(int(length))
    
        w_res = handle_user_input("Change website ? [y/n]: ")

        if w_res.lower() == 'y':
            website = handle_user_input("Website: ")

        #print(str(website) + " " + str(email or '') + " " + str(password or ''))

        #TODO: open file, go the line n and overwrite old values with new values


    else:
        print("No entry for website '%s'." % website)
        return False


def delete(website):
    delete_line_in_file(7, "data.txt")
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
        i = 0
        for line in f:
            l = line.split()

            if l[0] == website:
                l.insert(0, i+1)
                result.append(l)
            i += 1

    return result

delete("test")
#update(website="orange")
#print(save("orange", "matthias.brown@gmail.com", "123456789"))
#print(fetch("microsoft"))
#generate("microsoft", "matthias.brown@gmail.com", 64)