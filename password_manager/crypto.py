from cryptography.fernet import Fernet
import os
import pwd
import grp
import stat
from backup import *
#from sendFile import *

class PasswordCrypto:

    FILENAME = ".keys.key"
    FILEPATH = os.getcwd() + "/" + FILENAME
    BACKUP_FOLDER = "backups/keys"

    def __init__(self):
        pass

    def encrypt(self, plain_password):
        key = Fernet.generate_key()
        self.saveKey(key)
        fer = Fernet(key)
        return fer.encrypt(plain_password.encode())

    def decrypt(self, key, cipher):
        if key != None:
            fer = Fernet(key)
            decrypted_password = fer.decrypt(cipher)
            return decrypted_password.decode()

    def saveKey(self, key):
        try:
            f = open(PasswordCrypto.FILEPATH, 'ab')
            f.write(key + b'\n')
            f.close()

            self.changeFileOwner(PasswordCrypto.FILEPATH)
            self.changeFilePermissions(PasswordCrypto.FILEPATH)

            backup([PasswordCrypto.FILENAME], [PasswordCrypto.BACKUP_FOLDER])
            #sendFile(PasswordCrypto.FILENAME)

            return True
        except FileNotFoundError:
            f = open(PasswordCrypto.FILEPATH, 'wb')
            f.write(key + b'\n')
            f.close()

            self.changeFileOwner(PasswordCrypto.FILEPATH)
            self.changeFilePermissions(PasswordCrypto.FILEPATH)

            backup([PasswordCrypto.FILENAME], [PasswordCrypto.BACKUP_FOLDER])
            #sendFile(PasswordCrypto.FILENAME)

            return True

    def changeFileOwner(self, path):
        uid = pwd.getpwnam("root").pw_uid
        gid = grp.getgrnam("root").gr_gid
        os.lchown(path, uid, gid)
    
    def changeFilePermissions(self, path):
        mode = (stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP) & ~(stat.S_IRWXO)
        os.chmod(path, mode)

    def getKeyFromFile(self):
        try:
            with open(PasswordCrypto.FILEPATH, 'rb') as f:
                for line in f:
                    pass
                return line
        except FileNotFoundError:
            print("Can't get key.")
            return None

    def getFileLength(self):
        fileLength = 0
        with open(PasswordCrypto.FILEPATH, 'r') as f:
            for line in f:
                fileLength += 1
        return fileLength

    def getKeyAt(self, i):
        if self.getFileLength() == 0:
            print("File is empty.")
            return None
        count = 1
        with open(PasswordCrypto.FILEPATH, 'rb') as f:
            for line in f:
                if count == i:
                    return line[:-1]
                count += 1
        return None
