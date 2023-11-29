import random
import sys
import json
import string
import secrets

class Constants:
    def __init__(self):
        self.length = None
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
        self.password_count = 3
    
    def to_dict(self):
        return {
            "length": self.length,
            "min_special_chars": self.min_special_chars,
            "min_digits": self.min_digits,
            "min_letters": self.min_letters,
            "min_uppercase": self.min_uppercase,
            "min_lowercase": self.min_lowercase,
            "max_special_chars": self.max_special_chars,
            "max_digits": self.max_digits,
            "max_letters": self.max_letters,
            "max_uppercase": self.max_uppercase,
            "max_lowercase": self.max_lowercase,
            "password_count": self.password_count,
        }

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

def validate_input(constants):
    # TODO: Finish this
    min_length = constants.min_special_chars + \
        constants.min_digits + \
        constants.min_letters + \
        constants.min_uppercase + \
        constants.min_lowercase
    max_length = constants.max_special_chars + \
        constants.max_digits + \
        constants.max_letters + \
        constants.max_uppercase + \
        constants.max_lowercase
    if max_length < min_length:
        return "Maximum length is less than minimum length"
    if constants.length is None:
        constants.length = random.randint(min_length, max_length)
    if min_length > constants.length:
        return "Minimum length is greater than specified length"
    if max_length < constants.length:
        return "Maximum length is less than specified length"

def validate_password(password, constants):
    return True

def main():
    constants = Constants()
    error = validate_input(constants)
    if error:
        pass
    alphabet = string.ascii_letters + string.digits
    special_chars = "!()-.?[]_~;:#$%^&*+=@"
    bag = alphabet + special_chars
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