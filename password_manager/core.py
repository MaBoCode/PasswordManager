import string
import random

class PasswordGenerator:
    UPPER_CASE_LETTERS = string.ascii_uppercase
    LOWER_CASE_LETTERS = string.ascii_lowercase
    DIGITS = string.digits
    SYMBOLS = string.punctuation

    CHARS = list(UPPER_CASE_LETTERS + LOWER_CASE_LETTERS + DIGITS)
    random.shuffle(CHARS)
    CHARS = ''.join(CHARS)

    def __init__(self, length = 8, containsSymbols = False):
        self.length = length
        self.containsSymbols = containsSymbols
        self.password = ""

        self.generate()


    def pickRandomChar(self):
        return random.choice(PasswordGenerator.CHARS)

    def generate(self):

        if self.length < 8:
            print("Password length must be >= 8")
            return;

        if self.containsSymbols:
            PasswordGenerator.CHARS = list(PasswordGenerator.CHARS + PasswordGenerator.SYMBOLS)
            random.shuffle(PasswordGenerator.CHARS)
            PasswordGenerator.CHARS = ''.join(PasswordGenerator.CHARS)

        i = 0

        while i < self.length:
            self.password += self.pickRandomChar()
            i += 1
        
    def getPassword(self):
        return self.password

    def setLength(self, length):
        self.length = length
