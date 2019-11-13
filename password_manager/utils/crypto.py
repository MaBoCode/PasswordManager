from cryptography.fernet import Fernet

class Crypto:

    def __init__(self):
        pass

    def encrypt(self, plain_password):
        key = Fernet.generate_key()
        f = Fernet(key)
        enc_password = f.encrypt(plain_password.encode())

        return (key, enc_password)

    def decrypt(self, pair):
        key, password = pair
        f = Fernet(key)
        dec_password = f.decrypt(password)

        return dec_password.decode()