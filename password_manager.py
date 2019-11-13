import sys, argparse

def main():
    #print('Arguments: ' + str(sys.argv))
    options = ['-g', '-c', '-d', '-s', '-w', '-e', '-n', '-p', '-y']

    parser = argparse.ArgumentParser(description="Managing your passwords.")

    parser.add_argument('-g', dest='generate', action='store_true', help='generate a new password for a given website and email')
    parser.add_argument('-c', dest='change', action='store_true', help='change a website, email, and/or a password for a specified website')
    parser.add_argument('-d', dest='delete', action='store_true', help='delete one or multiple entries for a specified website')
    parser.add_argument('-s', dest='save', action='store_true', help='save a new entry with website, email and password specified')

    parser.add_argument('-w', dest='website', nargs=1, type=str, help='specify the website between quotes')
    parser.add_argument('-e', dest='email', nargs=1, type=str, help='specify the email between quotes')
    parser.add_argument('-n', dest='length', nargs=1, type=int, default=16, help='specify the length of the password to generate (min 16)')
    parser.add_argument('-p', dest='password', nargs=1, type=str, help='specify the password to save')

    parser.add_argument('-y', '--yes', action='store_true')

    #print(parser.parse_args(sys.argv[1:]))
    print(parser.print_help())

if __name__ == '__main__':
    main()