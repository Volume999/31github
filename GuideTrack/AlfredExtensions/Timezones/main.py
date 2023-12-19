import random
import sys
import json
import string
import secrets
import argparse
import os
from dotenv import load_dotenv
from icecream import ic
import re

# MODE = "RUN"
MODE = "TEST"
DEBUG = True

ic.disable()
load_dotenv()

class TimezoneConverter:
    def __init__(self, datetime, timezone1):
        self.datetime = datetime
        self.timezone1 = timezone1

    def convert(self, timezone2):
        pass

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

    convert_match = ic(re.match(convert_pattern, query))
    if convert_match:
        ic(convert_match.groupdict())
    difference_match = ic(re.match(difference_pattern, query))
    if difference_match:
        ic(difference_match.groupdict())
    return []

def parse_env_vars():
    pass 

def perform_operation(operation):
    pass

def main():
    args = ic(parser.parse_args())
    operations = parse_parameters(args.query)
    results = map(perform_operation, operations)
    print(json.dumps(wrap_results(results)))

def test():
    # Test regex patterns
    queries = [
        "01-01-2001 12:55 PM from CET to ET",
        "13:20 in CET",
        "13:20 from CET",
        "13:20 + 14:20"
    ]

    for query in queries:
        res = parse_parameters(query)
    
    # Test converter 
    print("Initial time: 01-01-2001 12:55 PM CET")
    t = TimezoneConverter("01-01-2001 12:55 PM", "CET")
    print(f"Convert to CET: {t.convert('ET')}")
    print(f"Convert to UTC: {t.convert('UTC')}")

if __name__ == "__main__":
    if DEBUG:
        ic.enable()
    if MODE == "RUN": main()
    elif MODE == "TEST": test()