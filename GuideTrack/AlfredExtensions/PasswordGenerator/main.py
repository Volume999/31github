import random
import sys
import json
import string
import secrets
import argparse
from icecream import ic

ic.disable()

ALPHABET = string.ascii_letters + string.digits
SPECIALCHARS = "!()-.?[]_~;:#$%^&*+=@"
BAG = ALPHABET + SPECIALCHARS

class Constants:
    def __init__(self, args=None):
        self.length = None
        self.min_special_chars = 1
        self.min_digits = 1
        self.min_letters = 1
        self.max_length = 64
        self.password_count = 3
        if args:
            try:
                self.length = int(args.length) if args.length != "_" else self.length
                self.min_special_chars = int(args.min_special_chars) if args.min_special_chars != "_" else self.min_special_chars
                self.min_digits = int(args.min_digits) if args.min_digits != "_" else self.min_digits
                self.min_letters = int(args.min_letters) if args.min_letters != "_" else self.min_letters
            except ValueError as e:
                ic(e)
                raise Exception("Input must be positive integers or _")
        err = self.validate()
        ic(err)
        if err:
            raise Exception(err)
    
    def to_dict(self):
        return {
            "length": self.length,
            "min_special_chars": self.min_special_chars,
            "min_digits": self.min_digits,
            "min_letters": self.min_letters,
            "password_count": self.password_count,
        }
    
    def validate(self):
        if any(map(lambda x: isinstance(x, int) and x < 0, self.to_dict().values())):
            return "Negative values are not allowed"
        
        min_length = self.min_special_chars + \
            self.min_digits + \
            self.min_letters
        
        if min_length > self.max_length:
            return "Minimum length is greater than maximum length"
        if self.length is None:
            self.length = random.randint(min_length, self.max_length)
        if self.length < min_length:
            return "Specified length is less than minimum length"
        if self.length > self.max_length:
            return "Specified length is greater than maximum length"
        return None

def validate_password(password, constants):
    length = len(password)
    special_chars = len(list(filter(lambda x: x in SPECIALCHARS, password)))
    digits = len(list(filter(lambda x: x in string.digits, password)))
    letters = len(list(filter(lambda x: x in string.ascii_letters, password)))
    ic(length, special_chars, digits, letters)
    if length == constants.length and \
        special_chars >= constants.min_special_chars and \
        digits >= constants.min_digits and \
        letters >= constants.min_letters:
        return True
    return False

def generate_password(constants):
    password = []
    for _ in range(constants.min_letters):
        password.append(random.choice(string.ascii_letters))
    for _ in range(constants.min_digits):
        password.append(random.choice(string.digits))
    for _ in range(constants.min_special_chars):
        password.append(random.choice(SPECIALCHARS))
    for _ in range(constants.length - len(password)):
        password.append(random.choice(BAG))
    random.shuffle(password)
    if (ic(validate_password(password, constants))) == True:
        return password
    return generate_password(constants)

def wrap_error(error):
    return {
        "items": [
            {
                "title": "Error",
                "subtitle": error,
            }   
        ]
    }

parser = argparse.ArgumentParser(description="Generate random passwords")
parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")
parser.add_argument("length", type=str, help="Length of the password", default="_", nargs="?")
parser.add_argument("min_digits", type=str, help="Minimum number of digits", default="_", nargs="?" )
parser.add_argument("min_letters", type=str, help="Minimum number of letters", default="_", nargs="?")
parser.add_argument("min_special_chars", type=str, help="Minimum number of special characters", default="_", nargs="?")


def main():
    args = parser.parse_args()
    if args.debug:
        ic.enable()
    ic("Debug mode enabled")
    ic(args)
    try:
        constants = Constants(args)
    except Exception as e:
        ic(e)
        sys.stdout.write(json.dumps(wrap_error(str(e))))
        return
    ic(constants.to_dict())
    passwords = set()
    while len(passwords) < constants.password_count:
        password = generate_password(constants)
        passwords.add("".join(password))
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