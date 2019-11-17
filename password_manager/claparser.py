#!/usr/bin/env python3

import sys, argparse
from password_manager.core import *

DESCRIPTION = """ 

Password Manager: you can generate, change, delete, save and view password.

"""

PROGRAM_NAME = "pam"

class CLAParser:

    """
    Parser for command line arguments

    When running ./fakegit.py command [options] it will call the method associated with command and handle the options

    command can be "generate", "update", "delete", "save" or "fetch"


    """

    def __init__(self):
        parser = argparse.ArgumentParser(prog=PROGRAM_NAME,description=DESCRIPTION, usage="%(prog)s command [options]")
        parser.add_argument('command', help="'fetch', 'generate', 'update', 'delete' or 'save'")
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
        
        usage = "%s %s -w WEBSITE -e EMAIL [-n LENGTH] [-s] [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Generate a new password for a given website and email', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website')
        parser.add_argument('-e', dest='email', nargs=1, type=str, required=True, help='specify the email')
        parser.add_argument('-n', dest='length', nargs=1, type=int, default=16, help='specify the length of the password to generate (min 16)')
    
        parser.add_argument('-s', '--save', action='store_true', default=False)

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))
        
        # Send arguments to generate(website, email, length, save)
        website = args['website'][0]
        email = args['email'][0]
        length = args['length']
        save = args['save']

        generate(website, email, length, save)
    
    def save(self):
        # filename save -w -e -p

        usage = "%s %s -w WEBSITE -e EMAIL -p PASSWORD [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Save a new entry with website, email and password specified', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website')
        parser.add_argument('-e', dest='email', nargs=1, type=str, required=True, help='specify the email')
        parser.add_argument('-p', dest='password', nargs=1, type=str, required=True, help='specify the password')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))
        
        # Send arguments to save(website, email, password)
        website = args['website'][0]
        email = args['email'][0]
        password = args['password'][0]

        save(website, email, password)

    def update(self):
        # filename change -w

        usage = "%s %s -w WEBSITE [-e EMAIL] [-p PASSWORD] [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Update a website, email, and/or a password for a specified website', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website')
        parser.add_argument('-e', dest='email', nargs=1, type=str, required=False, help='specify the email')
        parser.add_argument('-p', dest='password', nargs=1, type=str, required=False, help='specify the password')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))
        
        # Send arguments to update(website, email, password)
        website = args['website'][0]
        email = args['email'][0] if args['email'] else None
        password = args['password'][0] if args['password'] else None

        update(website, email, password)

    def delete(self):
        # filename delete -w

        usage = "%s %s -w WEBSITE [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Delete one or multiple entries for a specified website', usage=usage)
        
        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        # Send arguments to delete(website)
        website = args['website'][0]
        delete(website)

    def fetch(self):
        #filename fetch -w

        usage = "%s %s -w WEBSITE [-h]" % (PROGRAM_NAME, sys.argv[1])
        parser = argparse.ArgumentParser(description='Show passwords for website', usage=usage)

        parser.add_argument('-w', dest='website', nargs=1, type=str, required=True, help='specify the website between quotes')

        #Parse arguments starting after command and converting to dict
        args = vars(parser.parse_args(sys.argv[2:]))

        # Sending argument to fetch(website)
        website = args['website'][0]
        fetch(website)