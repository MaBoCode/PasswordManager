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

```bash
# Clone this repo.
$ git clone https://github.com/MaBoCode/PasswordManager.git

# cd in the repo
$ cd password_manager

# Install the requirements
$ pip3 install -r requirements.txt

# Change file permissions
$ chmod 700 main.py

# Create a symbolic link named `pma` to `main.py`.
$ ln -s $(pwd)/main.py /usr/local/bin/pma

# You're good to go
$ pma -h
```

## Code Examples
* Generate a new password for 'Google' with myemail@gmail.com.

&nbsp;&nbsp;&nbsp;&nbsp;`pma generate -w Google -e myemail@gmail.com`

* Generate a password of 32 characters for 'Oracle'

&nbsp;&nbsp;&nbsp;&nbsp;`pma generate -w Oracle -e myemail@oracle.com -n 32`

* Generate a password containing only letters and digits

&nbsp;&nbsp;&nbsp;&nbsp;`pma generate -w Oracle -e myemail@oracle.com -n 18 --no-symbols`

* Update the email for 'Google'

&nbsp;&nbsp;&nbsp;&nbsp;`pma update -w Google -e newemail@gmail.com`

* Change the password for 'Oracle'

&nbsp;&nbsp;&nbsp;&nbsp;`pma update -w Oracle -p newOraclePasswordThatIsNotVerySecure`

* Delete the entry for 'Google'

&nbsp;&nbsp;&nbsp;&nbsp;`pma delete -w Google`

* Get the password and email for 'Oracle'

&nbsp;&nbsp;&nbsp;&nbsp;`pma fetch -w Oracle`

* Export all passwords (to csv by default)

&nbsp;&nbsp;&nbsp;&nbsp;`pma export -l ~/Downloads/`
