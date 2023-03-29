# Password-cheak

Password Security Checker

This script checks if a password has been previously compromised in a data breach. It does this by sending a hashed version of the password to the Pwned Passwords API, which returns a list of hashes that match the first 5 characters of the hash of the password. The script then checks if the hash of the password matches any of the returned hashes, and if so, returns the number of times the password has been compromised.

Installation
To use this script, you will need to have Python 3 installed on your system, as well as the requests module. 
You can install the module using pip: pip install requests

Usage
To use the script, run the following command in your terminal: python password_checker.py [password1] [password2] ...

Replace [password1] and [password2] with the passwords you want to check. You can check multiple passwords at once by separating them with a space.

If a password has been compromised, the script will print a warning message that includes the number of times the password has been compromised. If a password has not been compromised, the script will print a message indicating that it is secure.


Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.
