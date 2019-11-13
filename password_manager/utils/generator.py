import string, random

CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
AMBIGUOUS_CHARS = "({}[]()\/'\"`~,;:.<>)"

for char in AMBIGUOUS_CHARS:
    CHARS = CHARS.replace(char, "")

class Generator:

    def __init__(self):
        self.password = None

    # chars is a list
    def pick_random_char(self, chars):
        return random.choice(chars)

    def shuffle_string(self, s):
        s_list = list(s)
        random.shuffle(s_list)

        return ''.join(s_list)

    def generate(self, length = 16):
        self.password = ""

        chars = CHARS

        if length < 16:
            return None

        i = length
        while i > 0 :
            char_list = self.shuffle_string(chars)
            self.password += self.pick_random_char(char_list)
            i -= 1
        return self.password