import re, string, os
from tabulate import tabulate

def sanitize_string(s):
    unwanted_chars = string.punctuation
    s = s.replace(' ', '')
    for c in unwanted_chars:
        s = s.replace(c, '')
    return s

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
        return True

def update_line_in_file(n, data, filename):
    # data is a tuple: (website, email, pair)
    # pair is a tuple: (key, password)
    new_filename = "data_update.txt"
    try:
        # while reading each line in the data file
        # write in a new file
        # write the updated line
        # delete old file
        # rename new file
        # TODO: look for a better way

        with open(filename, 'r+', encoding='utf-8') as f:
            with open(new_filename, 'a', encoding='utf-8') as f_update:
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
        os.rename(new_filename, filename)
        display_msg('Info', 'Updated line %d in `%s`' % (n, filename))
        return True

def delete_line_in_file(n, filename):
    # copy lines that are different from the line to delete, in a new file
    # remove the old file and rename the new
    new_filename = "data_delete.txt"
    try:
        with open(filename, 'r+', encoding='utf-8') as f:
            try:
                with open(new_filename, 'a', encoding='utf-8') as f_del:
                    for i, line in enumerate(f):
                        if i+1 != n:
                            f_del.write(line)
            except FileExistsError:
                return False
    except FileNotFoundError:
        return False
    else:
        os.remove(filename)
        os.replace(new_filename, filename)
        display_msg("Info", "Deleted line %d in `%s`." % (n, filename))
        return True

def fetch_in_file(website, filename):

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