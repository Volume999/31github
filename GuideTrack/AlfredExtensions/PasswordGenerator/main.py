import random
import sys
import json
import string
import secrets
import argparse

# OUTPUT EXAMPLE

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

ALPHABET = string.ascii_letters + string.digits
SPECIALCHARS = "!()-.?[]_~;:#$%^&*+=@"
BAG = ALPHABET + SPECIALCHARS

class Constants:
    def __init__(self, args=None):
        self.length = 16
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
                # TODO: Handle this error
                # print(e)
                pass
        try:
            self.validate()
        except Exception as e:
            # TODO: Handle this error
            # print(e)
            pass
    
    def to_dict(self):
        return {
            "length": self.length,
            "min_special_chars": self.min_special_chars,
            "min_digits": self.min_digits,
            "min_letters": self.min_letters,
            "password_count": self.password_count,
        }
    
    def validate(self):
        if any(map(lambda x: x < 0, self.to_dict().values())):
            return "Negative values are not allowed"
        
        min_length = self.min_special_chars + \
            self.min_digits + \
            self.min_letters
        
        if min_length > self.max_length:
            return "Minimum length is greater than maximum length"
        if self.length < min_length:
            self.length = random.randint(min_length, self.max_length)

def validate_password(password, constants):
    return True

parser = argparse.ArgumentParser(description="Generate random passwords")
# parser.add_argument("-l", "--length", type=int, help="Length of the password", default=None, required=False)
# parser.add_argument("-md", "--min-digits", type=int, help="Minimum number of digits", default=None, required=False)
# parser.add_argument("-ml", "--min-letters", type=int, help="Minimum number of letters", default=None, required=False)
# parser.add_argument("-msc", "--min-special-chars", type=int, help="Minimum number of special characters", default=None, required=False)

parser.add_argument("length", type=str, help="Length of the password", default="_", nargs="?")
parser.add_argument("min_digits", type=str, help="Minimum number of digits", default="_", nargs="?" )
parser.add_argument("min_letters", type=str, help="Minimum number of letters", default="_", nargs="?")
parser.add_argument("min_special_chars", type=str, help="Minimum number of special characters", default="_", nargs="?")


def main():
    # args = parser.parse_args()
    args = parser.parse_args()
    constants = Constants(args)
    # print(constants.to_dict())
    # error = validate_input(constants)
    # if error:
    #     result = {"items": [
    #         {
    #             "title": "Error",
    #             "subtitle": error,
    #         }   
    #     ]}
    passwords = []
    while len(passwords) < constants.password_count:
        password = ''.join(secrets.choice(BAG) for i in range(constants.length))
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