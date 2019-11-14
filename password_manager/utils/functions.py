import re, string

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
    finally:
        f.close()