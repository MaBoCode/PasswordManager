from setuptools import setup, find_packages

setup(
    name="PasswordManager",
    version="2.0",
    packages=find_packages()
	
	install_requires=['cryptography==2.6.1', 'tabulate==0.8.5']

	# Metadata
	author="Matthias Brown"
	author_email="matthias.brown@etu.univ-tours.fr"
	description="Best command line Password Manager!"
	keywords="password manager"
)
