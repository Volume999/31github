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
# 01-01-2001 12:55 PM from CET to ET
# (tz) {datetime/time/date} in {timezone} - Convert from local timezone to another
# 13:20 in CET
# (tz) (datetime/time/date) from {timezone} - Convert from another timezone to local
# 13:20 from CET
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
    convert_pattern = r"(?P<datetime>[\d\-\:\s\w]+)\s+(?P<op>in|from)\s+(?P<timezone1>[\w\/]+)\s*(?:(?:to)*\s+(?P<timezone2>[\w\/]+))?"
    difference_pattern = r"(?P<datetime1>[\d\-\:\s\w]+)\s+(?P<op>[+,-])\s+(?P<datetime2>[\d\-\:\s\w]+)"

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