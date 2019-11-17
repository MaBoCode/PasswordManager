# Command-line based Password Manager

You can:
  * Generate a new password:
    * Your new password will be by default **16 characters** long and will include digits, letters (lowercase and uppercase), and symbols for **maximum safety**.
    * Your password is carefully encrypted using **AES-GCM encryption**
    * Your password is saved locally
  * Save a password you already had with the corresponding email and website name
  * Change your password and/or email for a specific website
  * Delete your password for a particular website
  * View the password and email for a website

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Inspiration](#inspiration)

## Technologies
* python3 - version 3.7.3

## Setup
Clone the repo.
Run `pip3 install -r password_manager/requirements.txt` in your terminal.
Create a symbolic link named `pma` to `main.py`.
Create a symbolic link named `/bin/pma` to `pma`. (the symlink you created earlier)
Run `pma` in your terminal.

## Code Examples
Generate a new password for 'Google' with myemail@gmail.com and save it.
`pma generate -w Google -e myemail@gmail.com -s`

Generate a password of 32 characters for 'Oracle'
`pma generate -w Oracle -e myemail@oracle.com -n 32 -s`

Update the email for 'Google'
`pma update -w Google -e newemail@gmail.com`

Change the password for 'Oracle'
`pma update -w Oracle -p newOraclePasswordThatIsNotVerySecure`

Delete the entry for 'Google'
`pma delete -w Google`

Show the password and email for 'Oracle'
`pma fetch -w Oracle`

## Inspiration
I don't like that Google stores my passwords.
