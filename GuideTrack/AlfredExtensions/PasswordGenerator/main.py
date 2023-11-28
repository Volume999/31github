import sys
import json
import string
import secrets

class Constants:
    def __init__(self):
        self.length = 16
        self.min_special_chars = 0
        self.min_digits = 0
        self.min_letters = 0
        self.min_uppercase = 0
        self.min_lowercase = 0
        self.max_special_chars = 0
        self.max_digits = 0
        self.max_letters = 0
        self.max_uppercase = 0
        self.max_lowercase = 0
        self.password_count = 1

# CONSTANTS = {
#     "length": 16,
#     "min_special_chars": 0,
#     "min_digits": 0,
#     "min_letters": 0,
#     "min_uppercase": 0,
#     "min_lowercase": 0,
#     "max_special_chars": 0,
#     "max_digits": 0,
#     "max_letters": 0,
#     "max_uppercase": 0,
#     "max_lowercase": 0,
# }

# result = {"items": [
#     {
#         "uid": "desktop",
#         "type": "file",
#         "title": "Desktop",
#         "subtitle": "~/Desktop",
#         "arg": "Hello!",
#         "autocomplete": "Desktop",
#     }
# ]}  

def validate_input():
    return True

def validate_password(password, constants):
    return True

def main():
    if not validate_input():
        pass
    alphabet = string.ascii_letters + string.digits
    special_chars = string.punctuation
    bag = alphabet + special_chars
    constants = Constants()
    passwords = []
    while len(passwords) < constants.password_count:
        password = ''.join(secrets.choice(bag) for i in range(constants.length))
        if (validate_password(password, constants)) == True:
            passwords.append(password)
    results = []
    for i, password in enumerate(passwords):
        results.append({
            "arg": password,
            "title": password,
            "subtitle": f"Password {i+1}"
        })
    result = {"items": results}
    sys.stdout.write(json.dumps(result))

if __name__ == "__main__":
    main()