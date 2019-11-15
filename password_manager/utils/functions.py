import re, string
from tabulate import tabulate

def sanitize_string(s):
    unwanted_chars = string.punctuation
    s.strip()
    for c in unwanted_chars:
        s = s.replace(c, '')
    return s

def is_email_valid(email):
    email_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    return re.fullmatch(email_regex, email)

def display_msg(type, msg):
    s = "[%s] %s" % (type, msg)

    print(s)

def save_to_file(data):
    filename = "data.txt"

    s = data[0] + " " + data[1] + " " + data[2][0] + " " + data[2][1] + "\n"

    try:
        with open(filename, 'a') as f:
            f.write(s)
    except FileNotFoundError:
        return False
    else:
        return True

def delete_line_in_file(n, filename):
    with open(filename, 'r+') as f:
        for i, line in enumerate(f):
            if i+1 == n:
                f.truncate(len(line))

def handle_user_input(msg):
    res = sanitize_string(str(input(msg)))

    return res

def display_data(data, headers):
    t = tabulate(data, headers)
    print(t)