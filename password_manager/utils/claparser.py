#!/usr/bin/env python3

import sys, argparse

DESCRIPTION = """ 

Password Manger: you can generate, change, delete, save and view password.

"""

PROGRAM_NAME = "pam"

class CLAParser:

    """
    Parser for command line arguments

    When running ./fakegit.py command [options] it will call the method associated with command and handle the options

    command can be "generate", "change", "delete", "save"


    """

    def __init__(self):
        parser = argparse.ArgumentParser(prog=PROGRAM_NAME,description=DESCRIPTION, usage="%(prog)s command [options]")
        parser.add_argument('command', help="'generate', 'change', 'delete' or 'save'")
        parser.add_argument('--version', action='version', version='%(prog)s 2.0')
        
        args = parser.parse_args(sys.argv[1:2])

        #Check if the command has a method associated to it
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        # Invoke method associated with command
        getattr(self, args.command)()

    def generate(self):
        # filename generate -w -e [-n] [-y]
        
        usage = "%s %s -w WEBSITE -e EMAIL [-n LENGTH] [-y] [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Generate a new password for a given website and email', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')
        parser.add_argument('-e', dest='email', nargs=1, type=str, required=True, help='specify the email between quotes')
        parser.add_argument('-n', dest='length', nargs=1, type=int, default=16, help='specify the length of the password to generate (min 16)')
    
        parser.add_argument('-y', '--yes', action='store_true')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        #TODO: send args dictionary to the PM engine

    def change(self):
        # filename change -w

        usage = "%s %s -w WEBSITE [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Change a website, email, and/or a password for a specified website', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        #TODO: send args dictionary to the PM engine

    def delete(self):
        # filename delete -w

        usage = "%s %s -w WEBSITE [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Delete one or multiple entries for a specified website', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        #TODO: send args dictionary to the PM engine

    def save(self):
        # filename save -w -e -p

        usage = "%s %s -w WEBSITE -e EMAIL -p PASSWORD [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Save a new entry with website, email and password specified', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')
        parser.add_argument('-e', dest='email', nargs=1, type=str, required=True, help='specify the email between quotes')
        parser.add_argument('-p', dest='password', nargs=1, type=str, required=True, help='specify the password to save')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))
        
        #TODO: send args dictionary to the PM engine

    def fetch(self):
        #filename fetch -w

        usage = "%s %s -w WEBSITE [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Show passwords for website', usage=usage)

        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        #TODO: send args dictionary to the PM engine

if __name__ == '__main__':
    CLAParser()
