import random
import sys
import json
import string
import secrets
import argparse
import os
from dotenv import load_dotenv
from icecream import ic

ic.disable()
load_dotenv()

# Examples:
# I am not sure if keyword is needed but let's try with it first
# (tz) {datetime/time/date} (from)* {timezone} (to)* {timezone} - Straight converter
# (tz) {datetime/time/date} in {timezone} - Convert from local timezone to another
# (tz) (datetime/time/date) from {timezone} - Convert from another timezone to local
# (tz) (datetime/time/date) (+,-) (datetime/time/date) - Find time difference between 


def wrap_error(error):
    return {
        "items": [
            {
                "title": "Error",
                "subtitle": error,
            }   
        ]
    }

def wrap_results(passwords):
    results = []
    for i, password in enumerate(passwords):
        results.append({
            "arg": password,
            "title": password,
            "subtitle": f"Press Enter to copy password {i+1}"
        })
    result = {"items": results}
    return result

parser = argparse.ArgumentParser(description="Timezone converter")
parser.add_argument("query", type=str, help="Query to parse")

def parse_parameters(query):
    pass

def parse_env_vars():
    pass 

def perform_operation(operation):
    pass

def main():
    args = ic(parser.parse_args())
    operations = parse_parameters(args.query)
    results = map(perform_operation, operations)
    print(json.dumps(wrap_results(results)))

if __name__ == "__main__":
    main()