import re, string, os, csv
from tabulate import tabulate
from definitions import *
from password_manager.utils.crypto import Crypto

def sanitize_string(s):
    unwanted_chars = string.punctuation.replace('*', '')
    s = s.replace(' ', '')
    for c in unwanted_chars:
        s = s.replace(c, '')
    return s

def sanitize_path(p):
    path_regex = "^(.*/)([^/]*)$"

    return re.fullmatch(path_regex, p)


def handle_user_input(msg):
    res = sanitize_string(str(input(msg)))

    return res

def is_email_valid(email):
    email_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    return re.fullmatch(email_regex, email)

def display_msg(type, msg):
    s = "[%s] %s" % (type, msg)

    print(s)

def display_data(data, headers):
    t = tabulate(data, headers)
    print(t)

def save_to_file(data, filename):
    
    s = data[0] + " " + data[1] + " " + data[2][0] + " " + data[2][1] + "\n"

    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(s)
    except FileNotFoundError:
        return False
    else:
        print("Data successfuly saved.")
        return True

def update_line_in_file(n, data, filename):
    # data is a tuple: (website, email, pair)
    # pair is a tuple: (key, password)
    new_filename = "data_update.txt"
    new_file_path = os.path.join(ROOT_DIR_PATH, new_filename)

    try:
        # while reading each line in the data file
        # write in a new file
        # write the updated line
        # delete old file
        # rename new file
        # TODO: look for a better way

        with open(filename, 'r+', encoding='utf-8') as f:
            with open(new_file_path, 'a', encoding='utf-8') as f_update:
                for i, line in enumerate(f):
                    if i+1 == n:
                        line_list = line.split()

                        website = line_list[0] if not data[0] else data[0]
                        email = line_list[1] if not data[1] else data[1]
                    
                        key = line_list[2] if not data[2][0] else data[2][0]
                        password = line_list[3] if not data[2][1] else data[2][1]

                        new_data = (website, email, key, password)
                        line = ' '.join(new_data) + "\n"

                    f_update.write(line)

    except FileNotFoundError:
        return False
    else:
        os.remove(filename)
        os.rename(new_file_path, filename)
        print('Successfully updated line %d in `%s`' % (n, DEFAULT_DATA_FILENAME))
        return True

def delete_line_in_file(n, filename):
    # copy lines that are different from the line to delete, in a new file
    # remove the old file and rename the new
    new_filename = "data_delete.txt"
    new_file_path = os.path.join(ROOT_DIR_PATH, new_filename)

    try:
        with open(filename, 'r+', encoding='utf-8') as f:
            try:
                with open(new_file_path, 'a', encoding='utf-8') as f_del:
                    for i, line in enumerate(f):
                        if i+1 != n:
                            f_del.write(line)
            except FileExistsError:
                return False
    except FileNotFoundError:
        return False
    else:
        os.remove(filename)
        os.replace(new_file_path, filename)
        print("Successfully deleted line %d in `%s`." % (n, DEFAULT_DATA_FILENAME))
        return True

def fetch_in_file(website, filename):

    website = sanitize_string(website)

    result = []

    with open(filename, 'r') as f:
        i = 0
        for line in f:
            l = line.split()

            if (l[0].lower() == website.lower()) or (website == '*') or (website.lower() in l[0].lower()):
                l.insert(0, i+1)
                result.append(l)
            i += 1

    return result


def export_to_csv(file_path):

    filename = "exports.csv"

    if file_path[len(file_path)-1] != '/':
        file_path += "/"

    if file_path[0] == '~':
        home_path = os.path.expanduser("~")
        full_path = home_path + file_path[1:] + filename
    else:
        full_path = os.path.abspath(file_path + filename)
    
    c = Crypto()

    try:
        with open(full_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Website", "Email", "Password"])

            with open(DATA_FILE_PATH, 'r') as data_file:
                for line in data_file:
                    line_list = line.split(' ')
                    website = line_list[0]
                    email = line_list[1]
                    decrypted_password = c.decrypt(
                        (line_list[2], line_list[3]))
                    writer.writerow([website, email, decrypted_password])
    except:
        print("Couldn't export data")
        return False
    else:
        print("Data exported to %s" % full_path)
        return True