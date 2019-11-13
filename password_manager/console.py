#!/usr/bin/python3

from PasswordGenerator import PasswordGenerator
from PasswordCrypto import PasswordCrypto
import os
import re
import pwd
import grp
import stat
import time
import sys
from tabulate import tabulate
from backup import *
#from sendFile import *

class PasswordGeneratorConsole:
    FILENAME = ".data"
    FILEPATH = os.getcwd() +  "/" + FILENAME
    EMAIL_REGEX = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    BACKUP_FOLDER = "backups/passwords"

    def __init__(self):
        try:
            os.mkdir("backups")
        except FileExistsError:
            #print("[Error] Dir %s already exists" % dirname)
            pass

        self.start()



    def start(self):
        choice = input("What do you want to do: [1] save a password, [2] generate a new password or [3] search a password: ")

        if choice == "1":
            if self.savePassword():
                print("Password saved.")
        elif choice == "2":
            self.generatePassword()
        elif choice == "3":
            self.searchPassword()
        else:
            print("Please enter '1' or '2'")
            self.start()
    
    def searchPassword(self):
        website = input("Website ?: ")
        website = website.replace(" ", "_")
        data_list = []
        try:
            with open(PasswordGeneratorConsole.FILEPATH, 'r') as f:
                for line in f:
                    line_list = line.split(' ')

                    if website == '*':
                        data_list.append(line_list)

                    if (line_list[1].lower() == website.lower() or website.lower() in line_list[1].lower()) and website != '*':
                        data_list.append(line_list)

            if len(data_list) == 0:
                print()
                print("No match found.")
                self.searchPassword()
                return;
            else:
                print()
                if len(data_list) == 1:
                    print("Found 1 match.")
                else:
                    print("Found %d matches." % len(data_list))
                    time.sleep(1)
        except FileNotFoundError:
            print("[Error] File %s not found" % PasswordGeneratorConsole.FILENAME)
            return;

        #Remove the new line char for each password element
        for pass_list in data_list:
            pass_list[3] = pass_list[3][:-1]
        
        pc = PasswordCrypto()

        print()
        #print("Website\t\t\t\t\tEmail\t\t\t\t\tPassword")
        for pass_list in data_list:
            key = pc.getKeyAt(int(pass_list[0]))
            #print(pass_list[1].replace("_", " ") + "\t\t\t\t" + pass_list[2] + "\t\t" + pc.decrypt(key, pass_list[3].encode()) + "\n")
            pass_list[3] = pc.decrypt(key, pass_list[3].encode())
            pass_list.pop(0)
            pass_list[0] = pass_list[0].replace("_", " ")

        t = tabulate(data_list, headers=['Website', 'Email', 'Password'])
        print(t)
        
    
    def savePassword(self, password = None):
        website = input("Website: ")
        website = website.replace(" ", "_")
        email = input("Email: ")

        if re.fullmatch(PasswordGeneratorConsole.EMAIL_REGEX, email) == None:
            print("Email is invalid.")
            self.savePassword(password)
            return False

        if password == None:
            password = input("Password: ")
            pc = PasswordCrypto()
            password = pc.encrypt(password).decode()
        data = (website, email, password)
        return self.writeToFile(data)

    def generatePassword(self):
        length = input("Password length: ")

        if not length.isdigit():
            print("Enter a number.")
            self.generatePassword()

        if int(length) < 8:
            print("Password should be more than 8 chars.")
            self.generatePassword()


        toSave = input("Do you want to save it ? Y/n: ")
        
        if toSave.lower() == "y":
            pg = PasswordGenerator(int(length))
            pc = PasswordCrypto()
            encrypted_password = pc.encrypt(pg.getPassword())
            
            print("Encrypting password", end="")
            i = 0
            while True:
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(1)
                i += 1
                if i == 5:
                    break
            print("")
            if self.savePassword(encrypted_password.decode()):
                print("Password saved to file %s." % PasswordGeneratorConsole.FILEPATH)
            else:
                print("Error while saving password")
        elif toSave == "n":
            pg = PasswordGenerator(int(length))
            print("Password unsaved. Your password: %s" % pg.getPassword())
        else:
            print("Please enter 'Y' or 'n'")
            self.generatePassword()
        
    def writeToFile(self, data):
        try:
            if not self.passwordAlreadyExists(data[2]):
                fd = open(PasswordGeneratorConsole.FILEPATH, 'a')
                fd.write(str(self.getFileLength() + 1) + " " + data[0] + " " + data[1] + " " + data[2] + "\n")
                fd.close()

                self.changeFileOwner(PasswordGeneratorConsole.FILEPATH)
                self.changeFilePermissions(PasswordGeneratorConsole.FILEPATH)

                backup([PasswordGeneratorConsole.FILENAME], [PasswordGeneratorConsole.BACKUP_FOLDER])
                #sendFile(PasswordGeneratorConsole.FILENAME)

                return True
            else:
                print("Password already exists, choose another one")
                return False
        except FileNotFoundError:
            fd = open(PasswordGeneratorConsole.FILEPATH, 'w')
            fd.write(str(self.getFileLength() + 1) + " " + data[0] + " " + data[1] + " " + data[2] + "\n")
            fd.close()

            self.changeFileOwner(PasswordGeneratorConsole.FILEPATH)
            self.changeFilePermissions(PasswordGeneratorConsole.FILEPATH)

            backup([PasswordGeneratorConsole.FILENAME], [PasswordGeneratorConsole.BACKUP_FOLDER])
            #sendFile(PasswordGeneratorConsole.FILENAME)

            return True

    def passwordAlreadyExists(self, password):
        #Check if the given password to encrypt already exists
        #To do it: encrypt the password with all the keys in the key file
        #Check if there is a match with the corresponding already encrypted password
        with open(PasswordGeneratorConsole.FILEPATH, 'r') as f:
            for line in f:
                if password in line:
                    return True
        
        f.close()
        return False

    def changeFileOwner(self, path):
        uid = pwd.getpwnam("root").pw_uid
        gid = grp.getgrnam("root").gr_gid
        os.lchown(path, uid, gid)
    
    def changeFilePermissions(self, path):
        mode = (stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP) & ~(stat.S_IRWXO)
        os.chmod(path, mode)

    def getFileLength(self):
        fileLength = 0
        with open(PasswordGeneratorConsole.FILEPATH, 'r') as f:
            for line in f:
                fileLength += 1
        return fileLength

pgc = PasswordGeneratorConsole()
