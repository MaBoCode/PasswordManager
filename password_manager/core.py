from password_manager.utils.functions import *
from password_manager.utils.crypto import Crypto
from password_manager.utils.generator import Generator
from tabulate import tabulate
from definitions import *

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

    print("Your new password for '%s' is: %s" % (website, password))

    return save_to_file(data, DATA_FILE_PATH)


"""
Save website, email, password to file

1. Sanitize all strings
2. Encrypt password
3. Send all data to save_to_file function

"""
def save(website, email, password):

    website = sanitize_string(website)

    if not is_email_valid(email):
        display_msg('Error', "Invalid email.")
        return False

    if len(password) < 15:
        display_msg('Error', "Password is too short.(>= 15)")
        return False

    c = Crypto()
    pair = c.encrypt(password)

    data = (website, email, pair)

    return save_to_file(data, DATA_FILE_PATH)


"""
Update one row from file

website     str
email       str
password    str

"""
def update(website, email = None, password = None):

    # Website must be set in order to fetch rows
    if not website:
        return False

    website = sanitize_string(website)
    results = fetch_in_file(website, DATA_FILE_PATH)

    # Check if any results
    if len(results) > 0:

        # Check email
        if email and not is_email_valid(email):
            display_msg("Error", "Invalid email.")
            return False

        #Check password
        if password and len(password) < 16:
            display_msg("Error", "Password too short (> 15).")
            return False
        
        results_display = []
        c = Crypto()

        for row in results:
            l = row[:-2]
            l.append(c.decrypt((row[-2], row[-1])))
            results_display.append(l)

        display_data(results_display, ["N°", "Website", "Email", "Password"])

        entry_num = handle_user_input("Which entry you want to change? [enter n° or type 'c' to cancel]: ")

        if entry_num == 'c':
            return False

        entry_num = int(entry_num)
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
                print("Your new password is: %s" % password)
                pair = c.encrypt(password)
            else:
                pair = (None, None)
        else:
            pair = c.encrypt(password)
    
        w_res = handle_user_input("Change website ? [y/n]: ")

        if w_res.lower() == 'y':
            website = handle_user_input("Website: ")

        data = (website, email, pair)

        return update_line_in_file(entry_num, data, DATA_FILE_PATH)
    else:
        print("No entry for website '%s'" % (website))
        return False

def delete(website):
    # Website must be set in order to fetch rows
    if not website:
        return False

    website = sanitize_string(website)
    results = fetch_in_file(website, DATA_FILE_PATH)

    if(len(results) > 0):
        results_display = []
        c = Crypto()

        for row in results:
            l = row[:-2]
            l.append(c.decrypt((row[-2], row[-1])))
            results_display.append(l)

        display_data(results_display, ["N°", "Website", "Email", "Password"])

        entry_num = int(handle_user_input("Which entry you want to delete? [enter n°]: "))

        num_list = []
        for row in results:
            num_list.append(row[0])
        
        if entry_num not in num_list:
            display_msg("Error", "Entry not in list.")
            return False
        
        conf_res = handle_user_input("Are you sure you want to delete this entry ? [y/n]: ")

        if conf_res.lower() == 'y':
            return delete_line_in_file(entry_num, DATA_FILE_PATH)

        return False
    else:
        print("No entry for website '%s'" % (website))
        return False

# TODO: fetch function: get the password for the specified website

def fetch(website):
    
    if not website:
        return False
    
    website = sanitize_string(website)
    results = fetch_in_file(website, DATA_FILE_PATH)

    if(len(results) > 0):
        results_display = []
        c = Crypto()

        for row in results:
            l = row[1:-2]
            l.append(c.decrypt((row[-2], row[-1])))
            results_display.append(l)

        display_data(results_display, ["Website", "Email", "Password"])
        return True
    else:
        print("No entry for website '%s'" % (website))
        return False